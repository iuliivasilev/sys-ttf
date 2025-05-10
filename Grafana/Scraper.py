import constants as cnt
import os
import pandas as pd
import requests
import datetime
import shutil

from prometheus_api_client.utils import parse_datetime
from prometheus_api_client import PrometheusConnect, MetricsList, MetricSnapshotDataFrame
from tqdm import tqdm


start_time = parse_datetime("60d")
end_time = parse_datetime("now")
chunk_size = datetime.timedelta(hours=1)
parent_dir = os.path.join("D:", "SurvivalAnalysis", "TimeVarying", "CMCData")

if __name__ == "__main__":
    prom = PrometheusConnect(url=cnt.PROM_URL,
                             headers={"Authorization": f"Bearer {cnt.TOKEN}"}, disable_ssl=False)
    
    dirname = os.path.join(parent_dir, str(end_time.date()))
    os.makedirs(dirname, 0o774, exist_ok=True)
    for metric in tqdm(prom.all_metrics(), ncols=80, ascii=True, desc='Total'):
        if metric not in ["node_cpu_scaling_governor", "node_cpu_seconds_total", "node_nfs_requests_total",
                          "node_scrape_collector_duration_seconds", "node_scrape_collector_success"]:
            try:
                metric_data = prom.get_metric_range_data(
                    metric,
                    start_time=start_time,
                    end_time=end_time,
                    chunk_size=chunk_size,
                )
                metric_df = MetricSnapshotDataFrame(metric_data)
                metric_df.iloc[:, 1:].to_csv(os.path.join(dirname, f"{metric}.csv"))
            except Exception as err:
                print(f"Error in metric: {metric}")
                print(type(err))
                print(err)
            
    shutil.make_archive(dirname, 'zip', dirname)
    shutil.rmtree(dirname)
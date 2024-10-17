from win32evtlog import EVENTLOG_SEQUENTIAL_READ, EVENTLOG_FORWARDS_READ,EVENTLOG_INFORMATION_TYPE,EVENTLOG_ERROR_TYPE,EVENTLOG_WARNING_TYPE
from win32evtlog import ReadEventLog,OpenEventLog,CloseEventLog,GetNumberOfEventLogRecords
import csv

def Get_Event_Logs(server='localhost', log_type='Application'):
    #Get events from WinEventViewer
    log_handle = OpenEventLog(server, log_type)

    flags = EVENTLOG_FORWARDS_READ | EVENTLOG_SEQUENTIAL_READ
    events = []

    while True:
        records = ReadEventLog(log_handle, flags, 0)
        if not records:
            break
        for record in records:
            event = {
                'EventID': record.EventID,
                'ComputerName': record.ComputerName,
                'SourceName': record.SourceName,
                'TimeGenerated': record.TimeGenerated.Format(),
                'EventCategory': record.EventCategory,
                'EventType': record.EventType,
                'EventData': record.StringInserts,
                'Viewer': log_type
            }
            events.append(event)

    CloseEventLog(log_handle)
    return events

events = Get_Event_Logs(server='localhost', log_type='System')
with open('./events.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(events[0].keys()))
    writer.writeheader()
    for e in events:
        writer.writerow(e)
# Система мониторинга отказоустойчивости оборудования

## **I. Постановка задачи**

### **i. Введение**

### **ii. Актуальность**

**Решаемые задачи (сценарии использования):**

1. 

**Цели:**

1. 

**Антицели:**

1. 

**iii. Существующие системы**

## **II. Архитектура**

### **i. Схема взаимодействия**

### **ii. Программные компоненты**

1. Сборщик данных (демон)  
2. Хранилище \+ передача данных  
3. Аналитический модуль  
4. Frontend

## **III. Сбор данных**

### **0\. Примеры утилит**

1. Библиотеки: psutil, py\_sensors  
2. [HWMonitor](https://lumpics.ru/how-to-use-hwmonitor/), Speccy или Open Hardware Monitor  
3. \!\!\! [https://github.com/netdata/netdata](https://github.com/netdata/netdata)  
4. [Общая информация о системе](https://xakep.ru/2021/02/02/python-dni/)  
5. [Информация через windows\_tools.product\_key](https://codeby.net/threads/poluchaem-informaciju-o-sisteme-s-pomoschju-python-chast-2.79799/?ysclid=m0irh3unvg401792282)  
6. [https://remontka.pro/whea-logger-errors-windows/](https://remontka.pro/whea-logger-errors-windows/) (WHEA ошибки)  
7. Mind map: [https://socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/](https://socinvestigation.com/most-common-windows-event-ids-to-hunt-mind-map/) 

### **i. Метаданные (общее состояние системы)**

Собирается один раз или при каждом перезапуске/падении

1. Список всех устройств в системе  
2. Сохранение названий, идентификаторов и т.д  
3. [Характеристики компонент ПК](https://github.com/docyx/pc-part-dataset/tree/main)  
4. Коды событий [перезагрузки системы](https://www.shellhacks.com/windows-shutdown-reboot-event-ids-get-logs/) (41, 1074, 1076, 6005, 6006, 6008, 6009, 6013), [общий туториал](https://zomro.com/blog/faq/258-kak-posmotret-logi-shutdown-i-restart-v-windows-server)

### **ii. SSD/HDD**

1. [Показатели S.M.A.R.T.](https://habr.com/ru/articles/345502/) через **smartctl (работает)**  
2. [Показатели S.M.A.R.T.](https://www.geeksforgeeks.org/python-monitor-hard-disk-health-using-smartmontools/) через **smartmontools**  
3. Нужен smartctl (достаточно одного exe/obj/dll)

### **iii. Блок питания \+ охлаждение**

1. 

### **iv. CPU**

1. Общие сведения по сбору: [https://thepythoncode.com/article/get-hardware-system-information-python\#CPU\_info](https://thepythoncode.com/article/get-hardware-system-information-python#CPU_info)  
2. psutils (работает, но мало признаков)  
3. [platform](https://docs.python.org/3/library/platform.html) \- общие сведения по системе (входит в стандарт питона). [Гайд](https://stackforgeeks.com/blog/getting-processor-information-in-python)  
4. [Кастомный код для сбора информации по CPU](https://github.com/Hamdy/cpuinfo?tab=readme-ov-file) (очень много признаков, надо разбираться и убирать лишнее). Пишет, что нет сложных зависимостей.  
5. Дополнительные признаки: [https://habr.com/ru/companies/otus/articles/581796/](https://habr.com/ru/companies/otus/articles/581796/)

### **v. GPU**

1. psutils (работает, но мало признаков)  
2. GPUtil \- есть вопросы (не обновлялся с 2018\)  
3. Много разных библиотек (тег gpu-monitoring): [https://github.com/topics/gpu-monitoring?l=python\&ysclid=m27wc297ag238649781](https://github.com/topics/gpu-monitoring?l=python&ysclid=m27wc297ag238649781)

### **vi. RAM**

1. Классический Windows Memory Diagnostic Tool: [https://howtofixwindows.com/run-memory-diagnostic-tool/](https://howtofixwindows.com/run-memory-diagnostic-tool/), [Средство проверки RAM](https://remontka.pro/windows-memory-diagnostics/)  
2. Большой гайд (тесты: MATS+ INVC, SCHCKR): [https://www.technewstoday.com/how-to-test-ram/](https://www.technewstoday.com/how-to-test-ram/) 

### **vii. Внешние устройства**

1. Принтеры: [printer-monitoring](https://github.com/mvarrone/printer-monitoring) (win логи в [Microsoft-Windows-PrintService/Admin](https://answers.microsoft.com/en-us/windows/forum/all/printer-fails-with-event-id-372-on-win-10/eac09c3d-ea5c-4874-b911-41be51124bc7))  
2. WiFi: [wifiinfo](https://github.com/keithweaver/wifiinfo), [WiFi analyzer](https://github.com/piyk/wifi), 

### **viii. Разметка данных**

1. Linux:  
   1. Простая обработка событий: [https://www.xanthium.in/operating-system-signal-handling-in-python3](https://www.xanthium.in/operating-system-signal-handling-in-python3), [pyudev](https://pypi.org/project/pyudev/) (можно смотреть события по отдельному [устройству](https://avilpage.com/2016/09/detecting-device-events-in-ubuntu-with-python.html))  
   2. Системные журналы: [syslog.conf или rsyslog](https://wiki.merionet.ru/articles/logirovanie-sobytij-v-linux?ysclid=m24ixlu7jo782784369), [ausearch и auditd](https://selectel.ru/blog/audit-sistemnyx-sobytij-v-linux/?ysclid=m24j26dfwx508564593)  
   3. Классификация событий: [https://habr.com/ru/companies/ruvds/articles/533918/](https://habr.com/ru/companies/ruvds/articles/533918/)  
2. Win  
   1. Простая обработка событий: (62 типа) [https://www.xanthium.in/operating-system-signal-handling-in-python3](https://www.xanthium.in/operating-system-signal-handling-in-python3), [winevt](https://github.com/bannsec/winevt?ysclid=m24jjaf5pw361369449), [sys.monitoring](https://translated.turbopages.org/proxy_u/en-ru.ru.f20410e8-6708f3c2-36c20e2f-74722d776562/https/docs.python.org/3/library/sys.monitoring.html)  
   2. Системные журналы: [https://bisv.ru/blog/kak-prosmotret-zhurnaly-sboev-i-oshibok-windows](https://bisv.ru/blog/kak-prosmotret-zhurnaly-sboev-i-oshibok-windows) (Hardware Events)  
   3. Классификация ошибок: [https://bisv.ru/blog/kak-prosmotret-zhurnaly-sboev-i-oshibok-windows](https://bisv.ru/blog/kak-prosmotret-zhurnaly-sboev-i-oshibok-windows), [https://habr.com/ru/companies/galssoftware/articles/447522/](https://habr.com/ru/companies/galssoftware/articles/447522/)  
   4. Общий список EventID (возможно, не полный): [https://learn.microsoft.com/en-us/defender-endpoint/event-error-codes](https://learn.microsoft.com/en-us/defender-endpoint/event-error-codes)   
3. Автономные службы: [SOSreport](https://yandex.ru/search?clid=1906725&text=SOSreport&lr=213), 

## **IV. Интеграция**

## **V. Этапы работы**

### **i. Разработка ядра**

### **ii. Разработка хранилища**

### **iii. Разработка API и Viewer**

### **iv. Разработка веб\-сервера, сборщика и хранилища**

## **Список литературы**

**Обзорные статьи и сборники:**

1. Репозиторий статей/бенчмарков/направлений: [Cloud Incident Literature](https://github.com/yinfangchen/cloud-incident-lit?tab=readme-ov-file)  
2. (2024\! Обзорная статья по анализу отказов AI систем): [A Survey on Failure Analysis and Fault Injection in AI Systems](https://arxiv.org/pdf/2407.00125)  
3. (Обзорная статья): [Machine Learning for Survival Analysis: A Survey](https://arxiv.org/pdf/1708.04649)  
4. Можно ещё посмотреть здесь (TTF, run-to-fail, Degradation-threshold-shock models): [https://consensus.app/results/?q=time%20to%20failure%20hardware%20datasets\&synthesize=on\&copilot=on](https://consensus.app/results/?q=time%20to%20failure%20hardware%20datasets&synthesize=on&copilot=on)  
5. Теоретический обзор подходов анализа отказов (hardware-software): [Survey of combined hardware–software reliability prediction approaches](https://link.springer.com/article/10.1007/s13198-019-00811-y#Tab1)…  
6. Обзор практического использования ML и DL (анализ HDD, RAM and CPU): [A Survey on Hardware Failure Prediction of Servers Using Machine Learning and Deep Learning](https://ieeexplore.ieee.org/abstract/document/9493360?casa_token=PCeDii6TSfkAAAAA:lvBFcpuPoC3238W0B8kFNvxl3cC-kjCdA4ysdwMB_hpUf4MnqxYzBAkfIuw_0E2hHFvUA-4qoKBV)

Статьи:

1. (Объяснение ошибок оборудования): [Fail-Slow at Scale: Evidence of Hardware Performance Faults in Large Production Systems](https://ucare.cs.uchicago.edu/pdf/fast18-failSlowHw.pdf) (запрос на получение набора **отправлен**)  
2. (Анализ времени между отказами HPC, **нужен набор**): [What Can We Learn from Four Years of Data Center Hardware Failures?](https://people.iiis.tsinghua.edu.cn/~weixu/Krvdro9c/dsn17-wang.pdf)  
3. (Анализ SMART, Backblaze): [System-level hardware failure prediction using deep learning](https://picture.iczhiku.com/resource/ieee/WhigduGHwQarTMnC.pdf)  
4. (Анализ HPC систем, есть данные): [A large-scale study of failures in high-performance computing systems](https://cs.uwaterloo.ca/~kdaudjee/courses/cs848/papers/schro06.pdf). Данные: [https://www.pdl.cmu.edu/FailureData/index.shtml](https://www.pdl.cmu.edu/FailureData/index.shtml) и [https://www.usenix.org/cfdr](https://www.usenix.org/cfdr)

Необработанные материалы:

1. Набор Bosch: [https://www.kaggle.com/competitions/bosch-production-line-performance/data](https://www.kaggle.com/competitions/bosch-production-line-performance/data)  
2. Набор AWS Device Failure Test: [https://github.com/jmiguel99/device\_failure](https://github.com/jmiguel99/device_failure)  
3. Public data sets for testing and prototyping: [https://learn.microsoft.com/en-us/azure/azure-sql/public-data-sets?view=azuresql](https://learn.microsoft.com/en-us/azure/azure-sql/public-data-sets?view=azuresql)   
4. Формулировка направления: [https://en.m.wikipedia.org/wiki/Failure\_mode,\_effects,\_and\_criticality\_analysis](https://en.m.wikipedia.org/wiki/Failure_mode,_effects,_and_criticality_analysis)  
5. Подборки ссылок: [https://www.researchgate.net/post/Datasets-on-Hardware-Failures](https://www.researchgate.net/post/Datasets-on-Hardware-Failures), [https://www.researchgate.net/post/Where\_to\_find\_datasets\_for\_failure\_prediction](https://www.researchgate.net/post/Where_to_find_datasets_for_failure_prediction)   
6. Сгенерированный набор мониторинга состояния системы: [https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification)   
7. Анализ деградации батарей (странный набор): [https://github.com/rpglab/Battery-Degradation-Neural-Network-Codes-Datasets/tree/main](https://github.com/rpglab/Battery-Degradation-Neural-Network-Codes-Datasets/tree/main) 

# **Приложение**

## **Таблицы событий Windows**

Тип ошибки \- критическая/некритическая программная/аппаратная \+ конкретизация (cpu, disk, ram, gpu, …)

Первая таблица \- практическая (на основе данных)

| EventID | SourceName | EventType | Тип ошибки | Описание (кратко) | Ссылки (если есть) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 10016 | DCOM | 1 | программная | не хватает прав | [Ссылка](https://winitpro.ru/index.php/2015/04/07/parametry-razreshenij-dlya-konkretnogo-dcom-10016/) |
| 10010 | DCOM | 1 | программная | работа с сетью | [Ссылка](https://ugetfix.com/ask/how-to-fix-event-id-10010-distributedcom-error-in-windows/) |
| 36874, 36887, 36888 | Schannel | 1 | программная | ошибки http | [Ссылка](https://blog.bissquit.com/mail-servers/exchange-server/error-schannel-36874-36887-36888/?ysclid=m2t7ucaot6843770684) |
|  |  |  |  |  |  |

Вторая таблица \- теоретическая (на основе литературы)

| EventID | SourceName | EventType | Тип ошибки | Описание (кратко) | Ссылки (если есть) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Microsoft-Windows-WHEA-Logger | 1 | аппаратная (CPU) | Неустранимая аппаратная ошибка | [Ссылка](https://learn.microsoft.com/en-us/answers/questions/148579/a-fatal-hardware-error-occured-whea-logger-event-i) |
| 7 | disk | 1 | аппаратная (disk) | Неисправный блок | [Ссылка 1](https://answers.microsoft.com/en-us/windows/forum/all/event-id-7-the-device-deviceharddisk0dr0-has-a-bad/810ffed4-6d5a-48f5-988b-447df36cbb44), [Ссылка 2](https://www.wintips.org/fix-event-7-disk-has-a-bad-block-at-device-harddisk/) |
| 11, 154 | disk | 1 | аппаратная (disk) | Ошибка контроллера | [Ссылка](https://www.tenforums.com/drivers-hardware/170928-event-id-11-disk-event-viewer-frontal-usb-ports-acting-weird.html) 1, [Ссылка 2](https://www.thewindowsclub.com/event-id-154-the-io-operation-failed-due-to-a-hardware-error) |
| 12, 15, 14, 17 | TPM | 1 | аппаратная (disk) | Невосстановимая ошибка | [Ссылка](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/tpm-device-driver-error-log) 1, [Ссылка 2](https://community.amd.com/t5/pc-processors/windows-10-event-id-12-and-15-tpm-device-driver-errors/td-p/235297) |
| 14, 4019, 4041 | nvlddmkm, display | 1 | аппаратная/программная (gpu/ram) | Ошибка драйвера или устройства | [Ссылка 1](https://answers.microsoft.com/en-us/windows/forum/all/event-id14-nvlddmkm-error/739daa77-96c2-4859-918e-28aff9994a49), [Ссылка 2](https://answers.microsoft.com/ru-ru/windows/forum/all/видеодра/e279fa51-00ff-47fa-8126-d9eee3184d2f), [Ссылка 3](https://www.elevenforum.com/t/event-id-4101-amdkmdag-and-amdwddmg-keeps-crashing.6614/) |
| 17 | Advanced Error Reporting | 3 (warning) | аппаратная (CPU/power) | Устранимая аппаратная ошибка  | [Ссылка 1](https://community.medion.com/t5/ERAZER-Gaming/Thousands-of-event-log-Warnings-from-source-WHEA-Logger-Event-ID/td-p/103589),  [Ссылка 2](https://www.elevenforum.com/t/whea-logger-id-17-warnings.2313/) |
| 18 | Microsoft-Windows-WHEA-Logger | 1 | аппаратная | Фатальное аппаратное событие | [Ссылка](https://learn.microsoft.com/en-us/answers/questions/899735/random-reboots-event-id-18) |
| 19 | Microsoft-Windows-WHEA-Logger | 2 | аппаратная (CPU/power) | Устранимая аппаратная ошибка (blue screen). | [Ссылка 1](https://yandexwebcache.net/yandbtm?fmode=inject&tm=1730134351&tld=ru&lang=ru&la=1729197312&text=Microsoft-Windows-WHEA-Logger+19&url=https%3A//answers.microsoft.com/ru-ru/windows/forum/all/whea-logger-19/bae8d36e-36f6-4e92-95bc-aef5e8c4b5f2&l10n=ru&mime=html&sign=6b402e701d9cbe8d1e987856ba3e992a&keyno=0), [Ссылка 2](https://forum.ixbt.com/topic.cgi?id=4:133165) |
| 20 | Microsoft-Windows-WindowsUpdateClient | 1 | программная (общая) | Ошибка установки/обновления | [Ссылка](https://answers.microsoft.com/en-us/windows/forum/all/event-id-20/a3e32833-53df-4fdd-a7a2-43d02acadcc8) |
| 37, 55 | Kernel-Processor-Power | 2 | аппаратная (disk) | Отключение диска | [Ссылка](https://www.thewindowsclub.com/fix-event-id-55-kernel-processor-power-error-on-windows-pc) 1 |
| 41 | Microsoft-Windows-Kernel-Power | 1 | аппаратная (CPU/power) | Перезагрузка без предварительного завершения | [Ссылка](https://learn.microsoft.com/ru-ru/troubleshoot/windows-client/performance/event-id-41-restart) |
| 45, 46, 49, 161 | volmgr | 1 | программная(disk) | Сбой загрузки/ инициализации/создания дампа | [Ссылка](https://learn.microsoft.com/ru-ru/troubleshoot/windows-server/performance/event-id-46-start-a-computer) 1, [Ссылка 2](https://www.eightforums.com/threads/no-hibernate-and-volmgr-error-with-event-id-45-in-system-log.9499/), [Ссылка 3](https://windowsreport.com/event-id-161-volmgr/) |
| 51, 153 | disk | 2 | программная/аппаратная | Ошибка загрузки (153 \- предвестник скорой поломки) | [Ссылка](https://www.wintips.org/how-to-fix-disk-event-51-an-error-detected-on-device-during-paging-operation/) 1,[Ссылка 2](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/event-id-51-information)[Ссылка 3](https://www.windowsphoneinfo.com/threads/event-viewer-constant-disk-warning-event-153-followed-by-bsod-and-going-into-bios-after-restart.1083041/) |
| 55, 98, 140 | Ntfs | 1 | аппаратная (диск) | Требуется осмотр или изменение в структуре Ntfs | [Ссылка](https://answers.microsoft.com/en-us/windows/forum/all/about-error-of-event-id-98/379e8aa5-dd2c-490b-a74f-0cfe4a82770b) 1, [Ссылка 2](https://superuser.com/questions/1144117/windows-10-event-id-55-a-corruption-was-discovered-in-the-file-system-structu), [Ссылка 3](https://www.wintips.org/fix-speed-of-processor-in-group-is-being-limited-by-system-firmware-event-id-37-solved/) |
| 1000 | Application Error (?) | 1 | аппаратная (CPU) | Высокая загрузка процессора | [Ссылка](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) |
| 1001, 1002 | Windows Error Reporting | 1 | аппаратная (фактор CPU) | Высокая мощность, затраты процессора(BSOD) | [Ссылка 1](https://keysswift.com/blogs/computer-hardware/understanding-event-id-for-high-cpu-utilization-a-comprehensive-guide), [Ссылка 2](https://geekflare.com/ways-fix-event-id-1001-in-windows/) |
| 1003 | [Много разных](https://www.computer-administrator.com/event-id-1003/) | 1 | аппаратная | Ошибка ядра/драйвера | [**Ссылка 1**](https://www.computer-administrator.com/event-id-1003/),  [Ссылка 2](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) |
| 10010, 10016, 10021 | DCOM | 1 | программная (факторCPU) | Коллизии в компонентах (BSOD) | [Ссылка](https://winitpro.ru/index.php/2015/04/07/parametry-razreshenij-dlya-konkretnogo-dcom-10016/) 1, [Ссылка 2](https://keysswift.com/blogs/computer-hardware/understanding-event-id-for-high-cpu-utilization-a-comprehensive-guide), [Ссылка 3](https://learn.microsoft.com/en-us/answers/questions/1376716/blue-screen-of-death-event-id-10010) |
| **1020**, 1031, 1032 | SMB-Server | 1 | программная/аппаратная (CPU, Disk) | Ошибки файлового сервера SMB | [Ссылка 1](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-event-id-1020-warnings-file-server), [Ссылка 2](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) |
| 2001, 2003, 2007 | Зависит от устройства (ex, PerfDisk) | 2? | аппаратная (разное) | Превышение порога (disk/cpu) | [Ссылка 1,](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) [Ссылка 2](https://www.bleepingcomputer.com/forums/t/407849/event-id-2001-source-perfdisk/) |
| 2004 | Microsoft-Windows-Resource-Exhaustion-Detector | 2 | аппаратная (CPU) | Исчерпание виртуальной памяти | [Ссылка](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) 1, [Ссылка 2](https://morgantechspace.com/2013/12/event-id-2004-resource-exhaustion-diagnosis-events.html) |
| 2019, 2020 | Srv | 1 | аппаратная (CPU) | Исчерпание non-paged памяти | [Ссылка](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) 1, [Ссылка 2](https://www.a6n.co.uk/2008/04/eventid-2020-pool-consumption-exhausted.html) |
| 6006, 6008 | EventLog | 1 | программная/аппаратная | Неожиданная перезагрузка (\~18) | [**Ссылка**](https://homeautotechs.com/How-do-I-fix-error-6008/) **1,** [Ссылка 2](https://www.thewindowsclub.com/fix-event-id-6008-unexpected-shutdown-in-windows) |
| 7000, 7001, 7009, **7011**, 7023, 7031, 7034, 7043 | Service Control Manager | 1 | программная (фактор аппаратной, CPU) | Увеличение задержки, замедление работы (фактор деградации) | [Ссылка 1,](https://remontka.pro/service-control-manager-errors-windows-10/?ysclid=m2umqaf3t913204818) [Ссылка 2](https://keysswift.com/blogs/computer-hardware/understanding-event-id-for-high-cpu-utilization-a-comprehensive-guide) |
| 3639, **7011,** 9952, 20920 | Cisco Unified Communications Manager, Microsoft Exchange | 1? | программная (фактор аппаратной, CPU) | Редкие сетевые события, активно используется CPU | [Ссылка](https://softwareg.com.au/blogs/computer-hardware/event-id-for-high-cpu-utilization) |


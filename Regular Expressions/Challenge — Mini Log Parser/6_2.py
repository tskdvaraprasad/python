import re

log = """2024-06-01 08:15:32 ERROR user=john msg=Disk full
2024-06-01 08:16:10 WARN user=alice msg=High memory
2024-06-01 08:17:45 INFO user=john msg=Backup completed"""

pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|WARN|INFO) user=(?P<user>\w+) msg=(?P<msg>.*)'

entries = []

for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print(entries)
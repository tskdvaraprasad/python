import re

log = "2024-06-01 08:15:32 ERROR user=john msg=Disk full"

pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|WARN|INFO) user=(?P<user>\w+) msg=(?P<msg>.*)'

match = re.search(pattern, log)

print(match.group("timestamp"))
print(match.group("level"))
print(match.group("user"))
print(match.group("msg"))
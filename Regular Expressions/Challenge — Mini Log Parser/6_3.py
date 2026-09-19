import re

log = """2024-06-01 08:15:32 ERROR user=john msg=Disk full
2024-06-01 08:16:10 WARN user=alice msg=High memory usage
2024-06-01 08:17:45 INFO user=john msg=Backup completed
2024-06-01 08:18:20 ERROR user=alice msg=Connection failed"""

# 1. Regex pattern with named groups
pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>ERROR|WARN|INFO) user=(?P<user>\w+) msg=(?P<msg>.*)'

# 2. Use finditer() and groupdict()
entries = []

for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print("Parsed entries:")
for entry in entries:
    print(entry)
print("ERROR:", sum(1 for entry in entries if entry["level"] == "ERROR"))
print("WARN:", sum(1 for entry in entries if entry["level"] == "WARN"))
print("INFO:", sum(1 for entry in entries if entry["level"] == "INFO"))
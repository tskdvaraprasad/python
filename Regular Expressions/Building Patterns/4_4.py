import re

log = "2024-06-01 08:15:32 ERROR Disk full"

pattern = (
    r'(?P<date>\d{4}-\d{2}-\d{2}) '
    r'(?P<time>\d{2}:\d{2}:\d{2}) '
    r'(?P<level>\w+) '
    r'(?P<message>.*)'
)

match = re.fullmatch(pattern, log)

print("Date:", match.group("date"))
print("Time:", match.group("time"))
print("Level:", match.group("level"))
print("Message:", match.group("message"))
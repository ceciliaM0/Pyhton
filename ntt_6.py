import re

errors_by_interval = {'morning': 0, 'afternoon': 0, 'evening': 0}

log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[ERROR\] - (\w+) has (failed) after (\d+)ms.*$')

with open('output.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    match = log_pattern.match(line)
    if match:
        timestamp, app_type, status, _ = match.groups()

        hour = int(timestamp[:2])

#morning-00:00:00 - 07:59:59/
#afternoon-08:00:00-15:59:59/
# evening-16:00:00-23:59:59

        if 0 <= hour < 8:
            errors_by_interval['morning'] += 1
        elif 8 <= hour < 16:
            errors_by_interval['afternoon'] += 1
        else:
            errors_by_interval['evening'] += 1

max_interval = max(errors_by_interval, key=errors_by_interval.get)

print(f"The part of the day with the most errors: {max_interval}")

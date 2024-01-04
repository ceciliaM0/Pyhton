from collections import defaultdict
import re

app_runtimes = defaultdict(lambda: {'total_runtime': 0, 'count': 0})


log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[([A-Z]+)\] - (\w+) has (started|ran successfully) in (\d+)ms.*$')


with open('output.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    match = log_pattern.match(line)
    if match:
        timestamp, log_level, app_type, status, runtime = match.groups()

        if status == 'ran successfully':
            app_runtimes[app_type]['total_runtime'] += int(runtime)
            app_runtimes[app_type]['count'] += 1

for app_type, data in app_runtimes.items():
    if data['count'] > 0:
        average_runtime = data['total_runtime'] / data['count']
        print(f"Average successful runtime for {app_type}: {average_runtime:.2f} ms")

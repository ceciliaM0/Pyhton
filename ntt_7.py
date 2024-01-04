import re

longest_runtime = {'time': None, 'value': float('-inf')}
shortest_runtime = {'time': None, 'value': float('inf')}

log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[INFO\] - (\w+) has ran successfully in (\d+)ms.*$')


with open('output.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    match = log_pattern.match(line)
    if match:
        timestamp, app_type, runtime_str = match.groups()
        runtime = int(runtime_str)

        if runtime > longest_runtime['value']:
            longest_runtime['time'] = timestamp
            longest_runtime['value'] = runtime

        if runtime < shortest_runtime['value']:
            shortest_runtime['time'] = timestamp
            shortest_runtime['value'] = runtime

print(f"Longest successful run time: {longest_runtime['value']} ms at timestamp {longest_runtime['time']}")
print(f"Shortest successful run time: {shortest_runtime['value']} ms at timestamp {shortest_runtime['time']}")

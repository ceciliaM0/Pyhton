from collections import defaultdict
import re

def read_log_file():
    file = open("C:\\Users\\EMUSTECJN\\Downloads\\output.txt", mode='r')
    info = {'BackendApp': {'ERROR': 0, 'DEBUG': 0, 'INFO': 0},
            'FrontendApp': {'ERROR': 0, 'DEBUG': 0, 'INFO': 0},
            'API': {'ERROR': 0, 'DEBUG': 0, 'INFO': 0},
            'SYSTEM': {'ERROR': 0, 'DEBUG': 0, 'INFO': 0}}

    for line in file.readlines():
        words = line.split()
        log_type = words[2][1:-1:]
        app = words[4]
        if log_type != 'INFO':
            info[app][log_type] += 1
        else:
            info[app][log_type] += 0.5

    file.close()
    return info


def ex1(info):
    for app, logs in info.items():
        if app != 'SYSTEM':
            print(f'Pentru {app} avem cifrele:')
            for log_type, count in logs.items():
                print(log_type, count)
    return info

def ex2():
    app_runtimes = defaultdict(lambda: {'total_runtime': 0, 'count': 0})

    log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[([A-Z]+)\] - (\w+) has (started|ran successfully) in (\d+)ms.*$')

    with open("C:\\Users\\EMUSTECJN\\Downloads\\output.txt", 'r') as file:
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


def ex3(info):
    rez={}
    for app, logs in info.items():
        for log_type, count in logs.items():
            if log_type == 'ERROR':
                print(f'Aplicatia {app} a avut {count} erori')
                rez[app]=count
    return rez

def ex4(info):
    max_errors = 0
    app_with_errors = ''
    for app, logs in info.items():
        for log_type, count in logs.items():
            if log_type == 'ERROR' and count > max_errors:
                max_errors = count
                app_with_errors = app
    print(f'Cele mai multe erori au fost în aplicatia {app_with_errors}, adică {max_errors} erori')
    tr=(app_with_errors,max_errors)
    return tr

def ex5(info):
    max_info_count = 0
    app_with_max_info = ''
    for app, logs in info.items():
        for log_type, count in logs.items():
            if log_type == 'INFO' and count > max_info_count:
                max_info_count = count
                app_with_max_info = app
    print(f'Cele mai multe rulări cu succes au fost în aplicatia {app_with_max_info}, adică {max_info_count} rulări cu succes')
    return (app_with_max_info,max_info_count)

def ex6():
    errors_by_interval = {'morning': 0, 'afternoon': 0, 'evening': 0}

    log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[ERROR\] - (\w+) has (failed) after (\d+)ms.*$')

    with open("C:\\Users\\EMUSTECJN\\Downloads\\output.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        match = log_pattern.match(line)
        if match:
            timestamp, app_type, status, _ = match.groups()

            hour = int(timestamp[:2])

            # morning-00:00:00 - 07:59:59/
            # afternoon-08:00:00-15:59:59/
            # evening-16:00:00-23:59:59

            if 0 <= hour < 8:
                errors_by_interval['morning'] += 1
            elif 8 <= hour < 16:
                errors_by_interval['afternoon'] += 1
            else:
                errors_by_interval['evening'] += 1

    max_interval = max(errors_by_interval, key=errors_by_interval.get)

    print(f"The part of the day with the most errors: {max_interval}")

def ex7():
    app_runtimes = defaultdict(lambda: {'longest': {'time': None, 'value': float('-inf')},
                                         'shortest': {'time': None, 'value': float('inf')}})

    log_pattern = re.compile(r'^(\d{2}:\d{2}:\d{2}) - \[INFO\] - (\w+) has ran successfully in (\d+)ms.*$')

    with open("output.txt", 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                timestamp, app_type, runtime_str = match.groups()
                runtime = int(runtime_str)

                if runtime > app_runtimes[app_type]['longest']['value']:
                    app_runtimes[app_type]['longest'] = {'time': timestamp, 'value': runtime}

                if runtime < app_runtimes[app_type]['shortest']['value']:
                    app_runtimes[app_type]['shortest'] = {'time': timestamp, 'value': runtime}

    for app_type, runtimes in app_runtimes.items():
        print(f"{app_type} - Longest successful run time: {runtimes['longest']['value']} ms at timestamp {runtimes['longest']['time']}")
        print(f"{app_type} - Shortest successful run time: {runtimes['shortest']['value']} ms at timestamp {runtimes['shortest']['time']}")
        print()


def ex8(file_path):
    hourly_activity = {}
    results = []  # Lista pentru a stoca rezultatele

    with open(file_path, 'r') as file:
        logs = file.readlines()

    for log in logs:
        log_parts = log.split(" - ")
        timestamp_parts = log_parts[0].split(":")
        hour = int(timestamp_parts[0])

        activity_type = log_parts[1][1:-1]
        app_type = log_parts[2].split()[0]

        if app_type == 'SYSTEM':
            continue  # Ignorăm tipul de aplicație 'SYSTEM'

        if hour not in hourly_activity:
            hourly_activity[hour] = {app_type: 0}
        elif app_type not in hourly_activity[hour]:
            hourly_activity[hour][app_type] = 0

        hourly_activity[hour][app_type] += 1

    max_activities = {}

    for hour, activities in hourly_activity.items():
        for app_type, count in activities.items():
            if app_type not in max_activities or count > max_activities[app_type][1]:
                max_activities[app_type] = (hour, count)

    for app_type, (hour, count) in max_activities.items():
        result = f"{app_type} had the most activities at hour {hour} with a total of {count} activities"
        results.append(result)  
        print(result)  

    return results


def ex9(file_path):
    app_logs = {}

    with open(file_path, 'r') as file:
        logs = file.readlines()

    for log in logs:
        log_parts = log.split(" - ")
        activity_type = log_parts[1][1:-1]
        app_type = log_parts[2].split()[0]

        if app_type not in app_logs:
            app_logs[app_type] = {'ERROR': 0, 'TOTAL': 0}

        app_logs[app_type]['TOTAL'] += 1

        if activity_type == 'ERROR':
            app_logs[app_type]['ERROR'] += 1

    results = []
    for app_type, counts in app_logs.items():
        error_count = counts['ERROR']
        total_count = counts['TOTAL']

        failure_rate = (error_count / total_count) * 100 if total_count != 0 else 0
        results.append(f"Failure rate for {app_type}: {failure_rate:.2f}%")
        
    print(results)
    return results

if __name__ == "__main__":
    ex8()

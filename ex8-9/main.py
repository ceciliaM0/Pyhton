def ex8():
    hourly_activity = {}

    with open("C:\\Users\\EMUSTECJN\\Downloads\\output.txt", 'r') as file:
        logs = file.readlines()

    for log in logs:
        log_parts = log.split(" - ")
        timestamp_parts = log_parts[0].split(":")
        hour = int(timestamp_parts[0])

        activity_type = log_parts[1][1:-1]
        app_type = log_parts[2].split()[0]

        if hour not in hourly_activity:
            hourly_activity[hour] = {}

        if (app_type, activity_type) not in hourly_activity[hour]:
            hourly_activity[hour][(app_type, activity_type)] = 0

        hourly_activity[hour][(app_type, activity_type)] += 1

    for hour, activities in hourly_activity.items():
        print(f"Hour {hour:02d}:")
        for (app_type, activity_type), count in activities.items():
            print(f"{app_type} had most {activity_type} activities: {count} times")
        print()

def ex9():
    app_logs = {}

    with open("C:\\Users\\EMUSTECJN\\Downloads\\output.txt", 'r') as file:
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

    for app_type, counts in app_logs.items():
        error_count = counts['ERROR']
        total_count = counts['TOTAL']

        failure_rate = (error_count / total_count) * 100 if total_count != 0 else 0
        print(f"Failure rate for {app_type}: {failure_rate:.2f}%")

if __name__ == "__main__":
    ex8()
    ex9()
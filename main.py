def read_log_file():
    file = open("C:\\Users\\EBOLOTTI5\\Downloads\\output.txt", mode='r')
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

info = read_log_file()

def ex1():
    for app, logs in info.items():
        if app != 'SYSTEM':
            print(f'Pentru {app} avem cifrele:')
            for log_type, count in logs.items():
                print(log_type, count)
    return info

def ex3():
    rez={}
    for app, logs in info.items():
        for log_type, count in logs.items():
            if log_type == 'ERROR':
                print(f'Aplicatia {app} a avut {count} erori')
                rez[app]=count
    return rez

def ex4():
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

def ex5():
    max_info_count = 0
    app_with_max_info = ''
    for app, logs in info.items():
        for log_type, count in logs.items():
            if log_type == 'INFO' and count > max_info_count:
                max_info_count = count
                app_with_max_info = app
    print(f'Cele mai multe rulări cu succes au fost în aplicatia {app_with_max_info}, adică {max_info_count} rulări cu succes')
    return (app_with_max_info,max_info_count)

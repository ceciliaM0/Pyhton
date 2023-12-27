def counter(exercitiu):
    file=open("C:\\Users\\EBOLOTTI5\\Downloads\\output.txt", mode='r');
    no_a1 = {'ERROR': 0, 'DEBUG': 0, 'INFO': 0}
    no_a2 = {'ERROR': 0, 'DEBUG': 0, 'INFO': 0}
    no_a3 = {'ERROR': 0, 'DEBUG': 0, 'INFO': 0}
    no_a4 = {'ERROR': 0, 'DEBUG': 0, 'INFO': 0}
    info={'BackendApp':no_a1,'FrontendApp':no_a2,'API':no_a3, 'SYSTEM':no_a4}

    for a in file.readlines():
        cuv=a.split()
        type=cuv[2][1:-1:]
        app=cuv[4]
        if type!= 'INFO':
         info[app][type]+=1
        else:
            info[app][type] += 0.5
       # print(f'Pt {app} am {info[app][type]} pt {type}')


    if exercitiu==1:
        for z, x in info.items():
            if z!='SYSTEM':
             print(f'Pentru {z} avem cifrele:')
             for y in x.items():
                print(y)
             else:
                 pass
    elif exercitiu==3:
        for z, x in info.items():
            for y in x.items():
                if y[0]=='ERROR':
                    print(f'Aplicatia {z} a avut {y[1]} erori')
    elif exercitiu==4:
        nrm=0
        for z, x in info.items():
            for y in x.items():
                if y[0]=='ERROR' and y[1]>nrm:
                    nrm=y[1]
                    app=z
        print(f'Cele mai multe erori au fost in aplicatia {app},adica {nrm} erori')
    elif exercitiu==5:
        nrm=0
        for z, x in info.items():
            for y in x.items():
                if y[0]=='INFO' and y[1]>nrm:
                    nrm=y[1]
                    app=z
        print(f'Cele mai multe rulari cu succes au fost in aplicatia {app},adica {nrm} rulari')

    else:
     for z,x in info.items():
        print(f'Pentru {z} avem cifrele:')
        for y in x.items():
            print(y)

counter(5)

import psutil

name = 'docky'        

for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        if pinfo['name'] == name :
            pid = pinfo['pid']
            print(pid)            
            p = psutil.Process(pid)
            p.terminate()
            print('proces was terminated')
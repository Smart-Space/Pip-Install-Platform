"""
/lib/operate/pip_uninstall.py
卸载第三方库
"""
import subprocess
import threading

def __uninstall(name,msgfunc,endfunc):
    cmd="pip uninstall -y "+name
    msgfunc(cmd+'\n')
    result=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    for line in iter(result.stdout.readline, b''):
        msgfunc(line.decode("utf-8"))
    endfunc()

def uninstall(name,msgfunc,endfunc):
    thread=threading.Thread(target=__uninstall,args=(name,msgfunc,endfunc,))
    thread.daemon=True
    thread.start()

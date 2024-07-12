"""
/lib/operate/pip_install.py
升级和安装的第三方库
"""
import subprocess
import threading

def __install(update,name,msgfunc,endfunc):
    if update:#已安装，升级
        cmd="pip install --upgrade "+name
    else:#安装
        cmd="pip install "+name
    msgfunc(cmd+'\n')
    result=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    for line in iter(result.stdout.readline, b''):
        msgfunc(line.decode('utf-8'))
    endfunc()

def install(update,name,msgfunc,endfunc):
    thread = threading.Thread(target=__install,args=(update,name,msgfunc,endfunc,))
    thread.setDaemon(True)
    thread.start()

def __update(func):
    result=subprocess.run('pip list --outdated',stdout=subprocess.PIPE,shell=True)
    packages=[]
    for s in result.stdout.decode('utf-8').split("\n")[2:-1]:
        packages.append(s.split(" ")[0])
    func(packages)
def update(func):
    thread=threading.Thread(target=__update,args=(func,))
    thread.setDaemon(True)
    thread.start()

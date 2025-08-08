"""
/lib/operate/pip_install.py
升级和安装的第三方库
"""
import subprocess
from json import loads
from sys import executable
from lib.operate.pip_threads import pipthreads

def __install(update,name,msgfunc,endfunc):
    if update:#已安装，升级
        cmd=f"{executable} -m pip install --upgrade {name}"
    else:#安装
        cmd=f"{executable} -m pip install {name}"
    msgfunc(cmd+'\n')
    result=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    for line in iter(result.stdout.readline, b''):
        msgfunc(line.decode('utf-8'))
    endfunc()

def install(update,name,msgfunc,endfunc):
    pipthreads.submit(__install,update,name,msgfunc,endfunc)

def __update(func):
    result=subprocess.run(f'{executable} -m pip list --outdated --format=json',stdout=subprocess.PIPE,shell=True)
    packages=loads(result.stdout.decode('utf-8'))
    func(packages)
def update(func):
    pipthreads.submit(__update,func)

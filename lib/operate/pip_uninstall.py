"""
/lib/operate/pip_uninstall.py
卸载第三方库
"""
import subprocess
from sys import executable
from lib.operate.pip_threads import pipthreads


def __uninstall(name,msgfunc,endfunc):
    cmd=f"{executable} -m pip uninstall -y {name}"
    msgfunc(cmd+'\n')
    result=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    for line in iter(result.stdout.readline, b''):
        msgfunc(line.decode("utf-8"))
    endfunc()

def uninstall(name,msgfunc,endfunc):
    pipthreads.submit(__uninstall,name,msgfunc,endfunc)

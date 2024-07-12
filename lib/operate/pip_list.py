"""
/lib/operate/pip_list.py
获取安装的第三方库
"""
import subprocess
import threading
import re

def __get_list(func):
    result=subprocess.run("pip list",stdout=subprocess.PIPE,shell=True)
    packages=[]
    for s in result.stdout.decode('utf-8').split("\n")[2:-1]:
        packages.append(s.split(" ")[0]+"\t\t\tv"+s.split(" ")[-1])
    path=get_pkgs_path()
    func(packages,path)

def get_list(func):
    thread = threading.Thread(target=__get_list,args=(func,))
    thread.setDaemon(True)
    thread.start()

def get_pkgs_path():#以tinui为参考，获取第三方库安装路线
    result=subprocess.run('pip show tinui',stdout=subprocess.PIPE,shell=True).stdout
    m=re.match(b'.*?Location: (.*?)[\r\n]',result,re.S|re.M|re.I)
    try:
        return m.groups()[0].decode()
    except AttributeError:
        from tkinter import messagebox
        messagebox.showerror("依赖缺失", "需要下载第三方库：tinui\n`pip install tinui`")

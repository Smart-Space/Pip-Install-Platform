"""
/lib/gui/gui_list.py
负责对安装的第三封库进行检索并呈现
"""
import webbrowser
import os
import re

import pipmode

nowlib=None#当前选定的库名称
#pkgs_path=None#第三方库安装路径，通过tinui位置确认

def initialize(_listbox,_listboxfunc):#初始化
    global listbox, listboxfunc, waitframe, waitframefunc
    listbox=_listbox
    listboxfunc=_listboxfunc
    listbox.update()
    listbox.bind('<<LoadedEvent>>',load_ui)#绑定子线程触发的加载事件
    width=listbox.winfo_width()
    height=listbox.winfo_height()
    waitframe,_,_,waitframefunc,_=listbox.add_waitframe((0,0),width,height)
    waitframefunc.start()

def start():#接受main.py调控，运行启动
    text=waitframe.add_paragraph((5,5),text='第三方库搜索中...')
    pipmode.get_list(initial_list)

def initial_list(_pkgs:list,_path):#从/lib/operate/pip_list.py子线程回调函数
    global pkgs, pkgs_path
    pkgs=_pkgs
    pkgs_path=_path
    listbox.event_generate('<<LoadedEvent>>')#触发加载事件

def load_ui(e):
    waitframefunc.end()
    for i in pkgs:#由pip_list.py通过initial_list()传递的_pkgs列表
        listboxfunc.add(i)
    listboxfunc.delete(0)

#以下为接受/gui.py调用方法
def sel_libs(lib):#选定库
    global nowlib
    nowlib=lib.split('\t')[0]
    return nowlib

def opendoc():#打开库在资源管理器中的位置
    if nowlib==None:#未选定
        return
    #在pip管理目录中，项目的元信息所在文件夹一般为项目本名，而非调用名称，即便二者大多数情况下一样
    namepath=''
    for fp in os.listdir(pkgs_path):
        if nowlib.replace('-','_') in fp and fp.endswith('dist-info'):
            namepath=fp
            break
    with open(pkgs_path+f'/{namepath}/top_level.txt',encoding='utf-8') as f:
        #从top_level.txt获取库主体文件夹的名称
        name=f.read()[:-1]
    if os.path.isfile(pkgs_path+'/'+name+'.py'):
        os.startfile(pkgs_path)
    else:
        os.startfile(pkgs_path+'/'+name)


def pypidoc():#打开主页(Home-page)
    if nowlib==None:#未选定
        return
    #在pip管理目录中，项目的元信息所在文件夹一般为项目本名，而非调用名称，即便二者大多数情况下一样
    namepath=''
    for fp in os.listdir(pkgs_path):
        if nowlib.replace('-','_') in fp and fp.endswith('dist-info'):
            namepath=fp
            break
    with open(pkgs_path+f'/{namepath}/METADATA',encoding='utf-8') as f:
        r=f.read()
    m=re.match('.*?Home-page: (.*?)[\r\n]',r,re.S|re.M|re.I).group(1)
    webbrowser.open(m)

def uninstall():#卸载选中项目
    if nowlib==None:
        return
    ...

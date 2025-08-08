"""
/lib/gui/gui_list.py
负责对安装的第三封库进行检索并呈现
"""
from tkinter import ttk
from importlib import metadata
import webbrowser
import os

from lib.gui.gui_uninstall import uninstall
import pipmode

nowlib=None#当前选定的库名称
selected=None#当前选定的库

def initialize(frame:ttk.Frame):#初始化
    global listbox, page
    page=frame
    topframe=ttk.Frame(frame)
    listbox=ttk.Treeview(topframe,columns=('name','version','description'),show='headings',selectmode='browse')
    listbox.heading('name',text='名称')
    listbox.heading('version',text='版本')
    listbox.heading('description',text='描述')
    listbox.column('name',width=220,anchor='center')
    listbox.column('version',width=100,anchor='center')
    listbox.column('description',width=450,anchor='center')
    listbox.pack(side='left',fill='both',expand=True)
    scroller=ttk.Scrollbar(topframe,orient='vertical',command=listbox.yview)
    listbox.configure(yscrollcommand=scroller.set)
    scroller.pack(side='right',fill='y')
    topframe.pack(side='top',fill='both',expand=True)
    bottomframe=ttk.Frame(frame)
    ttk.Button(bottomframe,text='打开文件位置',command=opendoc).pack(side='left',padx=5)
    ttk.Button(bottomframe,text='打开项目页面',command=pypidoc).pack(side='left',padx=5)
    ttk.Button(bottomframe,text='卸载',command=__uninstall).pack(side='left',padx=5)
    ttk.Button(bottomframe,text='重新检索',command=start).pack(side='left',padx=5)
    ttk.Button(bottomframe,text='检查全部可更新项目').pack(side='left',padx=5)
    bottomframe.pack(side='bottom',anchor='n',pady=5)
    listbox.bind('<<TreeviewSelect>>',sel_libs)#绑定选中事件
    listbox.bind('<Double-Button-1>',opendoc)#绑定双击事件
    listbox.bind('<<LoadedEvent>>',load_ui)#绑定子线程触发的加载事件
    start()#启动子线程

def start():#接受main.py调控，运行启动
    pipmode.get_list(initial_list)

def initial_list(_pkgs:list):#从/lib/operate/pip_list.py子线程回调函数
    global pkgs, pkgs_path
    pkgs=_pkgs
    listbox.event_generate('<<LoadedEvent>>')#触发加载事件

def load_ui(e):
    global nowlib
    nowlib=None
    listbox.delete(*listbox.get_children())
    for i in pkgs:
        listbox.insert('','end',values=(i['name'],i['version'],i['summary']))

#以下为接受/gui.py调用方法
def sel_libs(e):#选定库
    global nowlib, selected
    selected=listbox.selection()
    if not selected:
        return
    nowlib=listbox.item(selected[0])['values'][0]

def opendoc(e=None):#打开库在资源管理器中的位置
    if not nowlib:#未选定
        return
    meta=metadata.distribution(nowlib)
    toplevel=meta.read_text('top_level.txt')
    if toplevel:
        path=toplevel.split('\n')[0]
    else:
        fils=meta.read_text('RECORD').split('\n')
        path=None
        for i in fils:
            if '.dist-info' not in i:
                path=i.split('/',1)[0]
                break
    if path:
        namepath=meta.locate_file('').__str__()+'\\'+path
    else:
        namepath=meta.locate_file('').__str__()+'\\'+nowlib+'.py'
    if not os.path.exists(namepath):
        return
    os.startfile(namepath)

def pypidoc():#打开主页(Home-page)
    if nowlib==None:#未选定
        return
    url=metadata.metadata(nowlib).get('Home-page', None)
    if url:
        webbrowser.open(url)

def __uninstall():#卸载选中项目
    if nowlib==None:
        return
    page.event_generate('<<UninstallEvent>>')
    uninstall(nowlib)

def __check_update():#检查全部可更新项目
    page.event_generate('<<CheckUpdateEvent>>')

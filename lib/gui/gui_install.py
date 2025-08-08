"""
/lib/gui/gui_install.py
负责安装和升级第三方库
"""
from tkinter import ttk, Text, BooleanVar

import pipmode

update=None#是否升级，用于调整pip参数

def initialize(frame:ttk.Frame):
    #初始化
    global entry, textbox, check, button, page, update
    update=BooleanVar()
    page=frame
    topframe=ttk.Frame(frame)
    topframe.pack(anchor='n',pady=5)
    ttk.Label(topframe,text='第三方库名：').pack(side='left',padx=5)
    entry=ttk.Entry(topframe,width=30)
    entry.pack(side='left',padx=5)
    check=ttk.Checkbutton(topframe,text='升级',variable=update)
    check.pack(side='left',padx=5)
    button=ttk.Button(topframe,text='安装',command=install)
    button.pack(side='left',padx=5)
    textframe=ttk.Frame(frame)
    textframe.pack(fill='both',expand=True)
    textbox=Text(textframe,font=('Consolas',12),highlightthickness=1,wrap='word',state='disabled',relief='flat')
    textbox.pack(fill='both',side='left',expand=True)
    scroll=ttk.Scrollbar(textframe,orient='vertical',command=textbox.yview)
    scroll.pack(side='right',fill='y')
    textbox['yscrollcommand']=scroll.set
    textbox.bind('<<NewMsg>>',_add_msg)
    textbox.bind('<<End>>',_end)

def install():
    #开始下载（执行pip命令，不判断正误）
    name=entry.get()
    if name=='':
        return
    entry.configure(state='disabled')
    check.configure(state='disabled')
    button.configure(state='disabled')
    pipmode.install(update.get(),name,add_msg,end)

def add_msg(_msg:str):
    #接受pip_install的信息
    global msg
    msg=_msg
    textbox.event_generate('<<NewMsg>>')
def _add_msg(e):
    #接受pip_install调用add_msg传递的信息
    textbox.config(state='normal')
    textbox.insert('end',msg)
    textbox.see('end')
    textbox.config(state='disabled')

def end():#接受pip_install停止操作
    textbox.event_generate('<<End>>')
def _end(e):#操作结束，按钮恢复
    entry.config(state='normal')
    check.config(state='normal')
    button.config(state='normal')
    textbox.config(state='normal')
    textbox.insert('end','====================\n\n')
    textbox.config(state='disabled')


update_selected=None#升级选中的库
update_name=None#升级选中的库名
def checkupdate_initialize(frame:ttk.Frame):
    #初始化升级检测页面
    global page2, upbutton, listbox
    page2=frame
    topframe=ttk.Frame(frame)
    topframe.pack(anchor='n',pady=5)
    ttk.Button(topframe,text='更新选中的库',command=update_selected).pack(side='left',padx=5)
    ttk.Separator(topframe,orient='vertical').pack(side='left',padx=5,fill='y')
    upbutton=ttk.Button(topframe,text='检测更新',command=checkupdate)
    upbutton.pack(side='left',padx=5)
    listframe=ttk.Frame(frame)
    listframe.pack(fill='both',expand=True)
    listbox=ttk.Treeview(listframe,columns=('name','version','update'),show='headings',selectmode='browse')
    listbox.heading('name',text='名称')
    listbox.heading('version',text='版本')
    listbox.heading('update',text='更新')
    listbox.column('name',anchor='center')
    listbox.column('version',anchor='center')
    listbox.column('update',anchor='center')
    listbox.pack(fill='both',side='left',expand=True)
    scroller=ttk.Scrollbar(listframe,orient='vertical',command=listbox.yview)
    scroller.pack(side='right',fill='y')
    listbox['yscrollcommand']=scroller.set
    listbox.bind('<<TreeviewSelect>>',_select)
    page2.bind("<<CheckEnd>>", __checkshow)

def _select(e):
    #选中项目
    global update_selected, update_name
    update_selected=listbox.selection()
    if not update_selected:
        return
    update_selected=update_selected[0]
    update_name=listbox.item(update_selected)['values'][0]

def update_selected():
    #升级选中的库
    global update_name, update_selected
    if not update_name:
        return
    update.set(True)
    page2.event_generate('<<DoUpdate>>')
    entry.delete(0,'end')
    entry.insert(0,update_name)
    install()
    listbox.delete(update_selected)
    update_selected=None
    update_name=None

def __checkupdate(pkgs):
    #接受pip_install.py的更新检测回调
    global check_show_pkgs
    check_show_pkgs=pkgs
    page2.event_generate('<<CheckEnd>>')
def checkupdate():
    #检测所有可更新项目
    upbutton.config(text='检测中...',state='disabled')
    pipmode.check_update(__checkupdate)
def __checkshow(e):
    #显示检测更新的结果
    upbutton.config(text='检测更新',state='normal')
    listbox.delete(*listbox.get_children())
    for pkg in check_show_pkgs:
        listbox.insert('','end',values=(pkg['name'],pkg['version'],pkg['latest_version']))

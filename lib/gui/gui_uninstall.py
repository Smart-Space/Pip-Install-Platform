"""
/lib/gui/gui_uninstall.py
负责卸载第三方库
"""
from tkinter import ttk, Text
import pipmode

def initialize(frame:ttk.Frame):#初始化
    global entry, textbox, button
    topframe=ttk.Frame(frame)
    topframe.pack(anchor='n',pady=5)
    ttk.Label(topframe,text='要卸载的库：').pack(side='left',padx=5)
    entry=ttk.Entry(topframe,width=30)
    entry.pack(side='left',padx=5)
    button=ttk.Button(topframe,text='开始卸载',command=uninstall)
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

def uninstall(name=None):#卸载项目
    if name:
        entry.delete(0,'end')
        entry.insert(0,name)
    else:
        name=entry.get()
    if name=='':
        return
    entry.config(state='disabled')
    button.config(state='disabled')
    pipmode.uninstall(name,add_msg,end)

def add_msg(_msg:str):
    #接受pip_uninstall的信息
    global msg
    msg=_msg
    textbox.event_generate('<<NewMsg>>')
def _add_msg(e):
    #接受pip_uninstall调用add_msg传递的信息
    textbox.config(state='normal')
    textbox.insert('end',msg)
    textbox.see('end')
    textbox.config(state='disabled')

def end():#接受pip_uninstall停止操作
    textbox.event_generate('<<End>>')
def _end(e):#操作结束，按钮恢复
    entry.config(state='normal')
    button.config(state='normal')
    textbox.config(state='normal')
    textbox.insert('end','====================\n\n')
    textbox.config(state='disabled')

# 在unintsall模块中，由gui.py直接在本身操作本模块控件，
# 填入需要卸载的库名。
# 而在install(update)模块中，gui.py调用了该模块的一个
# 函数接口，由该模块自行根据命令操控该模块的对应控件。

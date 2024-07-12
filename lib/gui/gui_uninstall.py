"""
/lib/gui/gui_uninstall.py
负责卸载第三方库
"""
from os import pipe
import pipmode

def initialize(_entry,_entryfunc,_button,_textbox,_textboxfunc):#初始化
    global entry, entryfunc, button, textbox, textboxfunc
    entry=_entry
    entryfunc=_entryfunc
    button=_button
    textbox=_textbox
    textboxfunc=_textboxfunc
    textbox.config(state='disabled')
    textbox.bind('<<NewMsg>>',_add_msg)
    textbox.bind('<<End>>',_end)

def uninstall():#卸载项目
    name=entryfunc.get()
    entryfunc.disable()
    button.disable()
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
    entryfunc.normal()
    button.active()
    textbox.config(state='normal')
    textbox.insert('end','====================\n\n')
    textbox.config(state='disabled')

# 在unintsall模块中，由gui.py直接在本身操作本模块控件，
# 填入需要卸载的库名。
# 而在install(update)模块中，gui.py调用了该模块的一个
# 函数接口，由该模块自行根据命令操控该模块的对应控件。

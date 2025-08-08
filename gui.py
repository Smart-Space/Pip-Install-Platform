"""
/gui.py
负责PIP的图形界面部分
结构上，作为/lib/gui/...的中枢
"""
from tkinter import Tk
from tkinter import ttk
import os

from lib.gui import gui_list, gui_install, gui_uninstall

path=os.getcwd()


#库列表
selectlib=None
def sel_libs(lib):#选定库
    global selectlib
    selectlib=gui_list.sel_libs(lib)
def opendoc(e):
    gui_list.opendoc()
def pypidoc(e):
    gui_list.pypidoc()
def update(e):
    #直接调用gui_install
    gui_install.checkupdate(book)
def refind(e):
    #刷新
    p1x.clean()
    book.showpage(p1)#786(785)x545
    p1x.environment({'sel_libs':sel_libs,'opendoc':opendoc,'pypidoc':pypidoc,'update':update,
        'uninstall':uninstall,'refind':refind})
    p1x.loadxml(open(path+r'\pages\p1_libs.xml',encoding='utf-8').read())
    p1_listbox,p1_listboxfunc,_=p1x.tags['lsbox']#获取列表框以及函数接口
    gui_list.initialize(p1_listbox,p1_listboxfunc)
    gui_list.start()

#升级&安装
def update_switch(check):
    #是否升级
    gui_install.update_switch(check)
def install(e):
    #开始下载
    ...


# 创建主窗口
root = Tk()
root.title("Pip Integration Platform")
root.minsize(1000, 600)
# 计算居中的位置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - 1000 / 2)
center_y = int(screen_height / 2 - 700 / 2)
root.geometry(f"1000x600+{center_x}+{center_y}")

book=ttk.Notebook(root)
book.pack(fill='both', expand=True)

p1=ttk.Frame(book)
p1.pack(fill='both', expand=True)
book.add(p1, text="库列表")
gui_list.initialize(p1)
p1.bind("<<UninstallEvent>>", lambda e: book.select(p3))
# p1.bind("<<CheckUpdateEvent>>", lambda e: book.select(p4))

p2=ttk.Frame(book)
p2.pack(fill='both', expand=True)
book.add(p2, text="升级&安装")
gui_install.initialize(p2)

p3=ttk.Frame(book)
p3.pack(fill='both', expand=True)
book.add(p3, text="卸载")
gui_uninstall.initialize(p3)

#
#
#升级&安装
# p2=book.addpage('升级&安装',cancancel=False)
# p2x=book.getuis(p2)[1]
# p2x.environment({'update_switch':update_switch,'install':install})
# p2x.loadxml(open(path+r'\pages\p2_install.xml',encoding='utf-8').read())
# p2_entry,p2_entryfunc,_=p2x.tags['entry']
# p2_checkbutton=p2x.tags['check'][-2]
# p2_button=p2x.tags['button'][-2]
# p2_textbox,p2_textboxfunc,_=p2x.tags['textbox']
# gui_install.initialize(p2_entry,p2_entryfunc,p2_checkbutton,p2_button,p2_textbox,p2_textboxfunc,p2)
#


if __name__=="__main__":
    root.mainloop()

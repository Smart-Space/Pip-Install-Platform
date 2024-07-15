"""
/gui.py
负责PIP的图形界面部分
结构上，作为/lib/gui/...的中枢
"""
import tkinter as tk
import os
from TinUI import BasicTinUI, TinUIXml

from lib.gui import gui_list, gui_install, gui_search, gui_uninstall

path=os.getcwd()


#库列表↓
selectlib=None
def sel_libs(lib):#选定库
    global selectlib
    selectlib=gui_list.sel_libs(lib)
def opendoc(e):
    gui_list.opendoc()
def pypidoc(e):
    gui_list.pypidoc()
def uninstall(e):
    #直接调用gui_uninstall
    if selectlib!=None:
        book.showpage(p4)
        p4_entry.delete(0,'end')
        p4_entry.insert(0,selectlib.split(' ')[0])
        gui_uninstall.uninstall()
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
#库列表↑

#升级&安装↓
def update_switch(check):
    #是否升级
    gui_install.update_switch(check)
def install(e):
    #开始下载
    gui_install.install()
#升级&安装↑

#卸载↓
def uninstall2(e):
    #卸载
    gui_uninstall.uninstall()
#卸载↑


# 创建主窗口
root = tk.Tk()
root.title("Pip Integration Platform")
# 设置窗口大小和不可伸缩属性
root.geometry("800x700")
root.resizable(width=False, height=False)
# 计算居中的位置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - 800 / 2)
center_y = int(screen_height / 2 - 700 / 2)
root.geometry(f"800x600+{center_x}+{center_y}")

main=BasicTinUI(root)
main.pack(fill='both',expand=True)
main.config(background='#f0f0f0')

mainx=TinUIXml(main)
mainx.loadxml(open(path+r'\pages\main.xml',encoding='utf-8').read())

book=mainx.tags['ntbook'][3]

#库列表
p1=book.addpage('库列表',cancancel=False)
p1x=book.getuis(p1)[1]
book.showpage(p1)#786(785)x545
p1x.environment({'sel_libs':sel_libs,'opendoc':opendoc,'pypidoc':pypidoc,'update':update,
    'uninstall':uninstall,'refind':refind})
p1x.loadxml(open(path+r'\pages\p1_libs.xml',encoding='utf-8').read())
p1_listbox,p1_listboxfunc,_=p1x.tags['lsbox']#获取列表框以及函数接口
gui_list.initialize(p1_listbox,p1_listboxfunc)

#升级&安装
p2=book.addpage('升级&安装',cancancel=False)
p2x=book.getuis(p2)[1]
p2x.environment({'update_switch':update_switch,'install':install})
p2x.loadxml(open(path+r'\pages\p2_install.xml',encoding='utf-8').read())
p2_entry,p2_entryfunc,_=p2x.tags['entry']
p2_checkbutton=p2x.tags['check'][-2]
p2_button=p2x.tags['button'][-2]
p2_textbox,p2_textboxfunc,_=p2x.tags['textbox']
gui_install.initialize(p2_entry,p2_entryfunc,p2_checkbutton,p2_button,p2_textbox,p2_textboxfunc,p2)

#搜索

#卸载
p4=book.addpage('卸载',cancancel=False)
p4x=book.getuis(p4)[1]
p4x.environment({'uninstall2':uninstall2})
p4x.loadxml(open(path+r'\pages\p4_uninstall.xml',encoding='utf-8').read())
p4_entry,p4_entryfunc,_=p4x.tags['entry']
p4_button=p4x.tags['button'][-2]
p4_textbox,p4_textboxfunc,_=p4x.tags['textbox']
gui_uninstall.initialize(p4_entry,p4_entryfunc,p4_button,p4_textbox,p4_textboxfunc)



if __name__=="__main__":
    root.mainloop()

"""
/lib/gui/gui_install.py
负责安装和升级第三方库
"""
from tkinter import Event

from tinui import BasicTinUI
import pipmode

update=False#是否升级，用于调整pip参数
update_page=False#升级检测页面是否打开
update_page_id=None#升级检测页面对应到TinUI.notebook的页面id
book=None#标签页控件
ui=None#标签页中对应的BasicTinUI

def initialize(_inputbox,_entry,_check,_button,_textbox,_textboxfunc,_pageid):
    #初始化
    global inputbox, entry, check, button, textbox, textboxfunc, pageid
    inputbox=_inputbox#entry所代表的实体控件
    entry=_entry
    check=_check
    button=_button
    textbox=_textbox
    textboxfunc=_textboxfunc
    pageid=_pageid
    textbox.config(state='disabled')
    textbox.bind('<<NewMsg>>',_add_msg)
    textbox.bind('<<End>>',_end)


def update_switch(check):
    #是否升级
    global update
    update=check

def install():
    #开始下载（执行pip命令，不判断正误）
    name=entry.get()
    entry.disable()
    check.disable()
    button.disable()
    pipmode.install(update,name,add_msg,end)

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
    entry.normal()
    check.active()
    button.active()
    textbox.config(state='normal')
    textbox.insert('end','====================\n\n')
    textbox.config(state='disabled')

def __checkupdate(pkgs):
    #接受pip_install.py的更新检测回调
    global check_show_pkgs
    check_show_pkgs=pkgs
    ui.event_generate('<<CheckEnd>>')
def checkupdate(_book):
    #检测所有可更新项目
    #在新临时标签页中展示，但是用户不可关闭
    #book为主程序标签控件
    global update_page, update_page_id, book, ui
    if update_page==False:#尚未创建该标签页
        book=_book
        update_page=True
        update_page_id=book.addpage('检测更新',cancancel=False)
        ui=book.getuis(update_page_id)[0]
        ui.add_paragraph((5,5),text='检测更新中……')
        ui.add_waitbar3((5,30),width=750)[-1]
    else:
        ui.delete('all')
        ui.add_paragraph((5,5),text='检测更新中……')
        ui.add_waitbar3((5,30),width=750)[-1]
    ui.bind('<<CheckEnd>>',__checkshow)
    book.showpage(update_page_id)
    pipmode.check_update(__checkupdate)
def __checkshow(e):
    #显示检测更新的结果
    ui.delete('all')
    num=len(check_show_pkgs)
    listitem=ui.add_listview((5,5),width=760,height=530,linew=40,num=num)[2]
    for i in range(0,num):
        listitem[i][0].add_paragraph((5,20),text=check_show_pkgs[i],anchor='w')
        listitem[i][0].add_button2((650,20),text='更新',anchor='w',command=lambda event,name=check_show_pkgs[i]:go2update(name))
def go2update(name):#根据选择的名字去install主界面升级
    book.showpage(pageid)
    inputbox.delete(0,'end')
    inputbox.insert(0,name)
    check.on()
    install()

"""
Pip Integration Platform (PIP)
python第三方包管理平台

Copyright 2024 Smart-Space<smart-space@qq.com>|<tsan-zane@outlook.com>

第三方依赖：tinui(GUI), setuptools(not used now)
"""
from gui import root, xpage
from pipmode import *
from lib.gui import gui_list, gui_install, gui_search

def start():#启动实用部分
    gui_list.start()


root.after(500,start)
root.mainloop()

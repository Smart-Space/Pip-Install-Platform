"""
Pip Integration Platform (PIP)
python第三方包管理平台

Copyright 2024-Present Smart-Space<smart-space@qq.com>|<tsan-zane@outlook.com>
Licensed: MIT

第三方依赖：sv-ttk
"""
import sv_ttk
from tkinter import ttk
from gui import root
from lib.operate import setting
from pipmode import *


if setting.get_theme() == 1:
    sv_ttk.set_theme("light")
else:
    sv_ttk.set_theme("dark")

style=ttk.Style()
style.configure("TNotebook.Tab", font=('微软雅黑',12))
style.configure("TButton", font=('微软雅黑',12))
style.configure("Treeview", font=('微软雅黑',12))
style.configure("TLabel", font=('微软雅黑',12))
style.configure("TEntry", font=('微软雅黑',12))
style.configure("Heading", font=('微软雅黑',12))
style.configure("TCheckbutton", font=('微软雅黑',12))

root.mainloop()

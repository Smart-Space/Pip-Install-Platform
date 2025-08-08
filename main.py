"""
Pip Integration Platform (PIP)
python第三方包管理平台

Copyright 2024 Smart-Space<smart-space@qq.com>|<tsan-zane@outlook.com>

第三方依赖：tinui(GUI), setuptools(not used now)
"""
import sv_ttk
from tkinter import ttk
from gui import root
from pipmode import *


sv_ttk.set_theme("light")

style=ttk.Style()
style.configure("TNotebook.Tab", font=('微软雅黑',12))
style.configure("TButton", font=('微软雅黑',12))
style.configure("Treeview", font=('微软雅黑',12))
style.configure("TLabel", font=('微软雅黑',12))
style.configure("TEntry", font=('微软雅黑',12))
style.configure("Heading", font=('微软雅黑',12))
style.configure("TCheckbutton", font=('微软雅黑',12))

root.mainloop()

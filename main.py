"""
Pip Integration Platform (PIP)
python第三方包管理平台

Copyright 2024-Present Smart-Space<smart-space@qq.com>|<tsan-zane@outlook.com>
Licensed: MIT

第三方依赖：sv-ttk
"""
import sv_ttk
from tkinter import ttk
import os
import platform
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from gui import root
from lib.operate import setting
from pipmode import *


if setting.get_theme() == 1:
    sv_ttk.set_theme("light")
else:
    sv_ttk.set_theme("dark")
    if platform.platform().startswith('Windows') and platform.release() >= '11':
        import ctypes
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        policy = ctypes.c_int(1)
        result = ctypes.windll.dwmapi.DwmSetWindowAttribute(
            ctypes.windll.user32.GetParent(root.winfo_id()),
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(policy),
            ctypes.sizeof(policy)
        )
    root.iconbitmap("logoD.ico")

style=ttk.Style()
style.configure("TNotebook.Tab", font=('微软雅黑',12))
style.configure("TButton", font=('微软雅黑',12))
style.configure("Treeview", font=('微软雅黑',12))
style.configure("TLabel", font=('微软雅黑',12))
style.configure("TEntry", font=('微软雅黑',12))
style.configure("Heading", font=('微软雅黑',12))
style.configure("TCheckbutton", font=('微软雅黑',12))
style.configure("TRadiobutton", font=('微软雅黑',12))

root.mainloop()

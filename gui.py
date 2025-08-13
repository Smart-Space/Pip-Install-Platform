"""
/gui.py
负责PIP的图形界面部分
结构上，作为/lib/gui/...的中枢
"""
from tkinter import Tk
from tkinter import ttk

from lib.gui import gui_list, gui_install, gui_uninstall, gui_search, gui_setting
from lib.operate.pip_threads import pipthreads
from i18n import _, set_language
from lib.operate import setting
set_language(setting.get_lang())


def _quit():
    """
    退出程序
    """
    pipthreads.shutdown()
    root.quit()
    root.destroy()

# 创建主窗口
root = Tk()
root.title("Pip Integration Platform")
root.minsize(1000, 600)
root.iconbitmap("logo.ico")
root.protocol("WM_DELETE_WINDOW", _quit)

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
book.add(p1, text=_("库列表"))
gui_list.initialize(p1)
p1.bind("<<UninstallEvent>>", lambda e: book.select(p3))
p1.bind("<<CheckDependencyEvent>>", lambda e: book.select(p5))
p1.bind("<<CheckUpdateEvent>>", lambda e: (book.select(p4), gui_install.checkupdate()))

p2=ttk.Frame(book)
p2.pack(fill='both', expand=True)
book.add(p2, text=_("升级&安装"))
gui_install.initialize(p2)

p3=ttk.Frame(book)
p3.pack(fill='both', expand=True)
book.add(p3, text=_("卸载"))
gui_uninstall.initialize(p3)

p4=ttk.Frame(book)
p4.pack(fill='both', expand=True)
book.add(p4, text=_("检查更新"))
gui_install.checkupdate_initialize(p4)
p4.bind("<<DoUpdate>>", lambda e: book.select(p2))

p5=ttk.Frame(book)
p5.pack(fill='both', expand=True)
book.add(p5, text=_("依赖分析"))
gui_search.initialize(p5)

p6=ttk.Frame(book)
p6.pack(fill='both', expand=True)
book.add(p6, text=_("设置"))
gui_setting.initialize(p6)

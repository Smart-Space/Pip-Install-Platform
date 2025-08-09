"""
/lib/gui/gui_search.py
负责分析第三方库的依赖关系并展示出来
"""
from tkinter import ttk
import pipmode


selected = None
name = None
name2 = None

def initialize(frame:ttk.Frame):
    global page, entry, listbox, depbutton, delbutton, clbutton, listbox2, nodepbutton
    page = frame
    leftframe = ttk.Frame(page)
    leftframe.pack(side="left",fill="both",expand=True)
    ltopframe = ttk.Frame(leftframe)
    ltopframe.pack(side="top",pady=5)
    ttk.Label(ltopframe,text="第三方库名：").pack(side="left",padx=5)
    entry = ttk.Entry(ltopframe,width=30)
    entry.pack(side="left",padx=5)
    depbutton = ttk.Button(ltopframe,text="分析",command=search_dependencies)
    depbutton.pack(side="left",padx=5)
    delbutton = ttk.Button(ltopframe,text="删除选中",command=delete_item)
    delbutton.pack(side="left",padx=5)
    clbutton = ttk.Button(ltopframe,text="清空",command=clear_list)
    clbutton.pack(side="left",padx=5)
    listbox = ttk.Treeview(leftframe,selectmode="browse",show="tree")
    listbox.pack(side="left",fill="both",expand=True)
    scroller = ttk.Scrollbar(leftframe,orient="vertical",command=listbox.yview)
    scroller.pack(side="right",fill="y")
    listbox.configure(yscrollcommand=scroller.set)
    listbox.bind("<<TreeviewSelect>>",on_select)
    listbox.bind("<Double-Button-1>",put_in_entry)
    listbox.bind("<<DependencySearchMsg>>", _search_msg)
    ttk.Separator(page,orient="vertical").pack(side="left",fill="y",padx=5)
    rightframe = ttk.Frame(page)
    rightframe.pack(side="right",fill="both")
    nodepbutton = ttk.Button(rightframe,text="列出所有顶层库",command=list_no_dep)
    nodepbutton.pack(side="top",pady=5)
    listbox2 = ttk.Treeview(rightframe,selectmode="browse",show="tree")
    listbox2.pack(side="left",fill="y",expand=True)
    scroller2 = ttk.Scrollbar(rightframe,orient="vertical",command=listbox2.yview)
    scroller2.pack(side="right",fill="y")
    listbox2.configure(yscrollcommand=scroller2.set)
    listbox2.bind("<<TreeviewSelect>>",on_select2)
    listbox2.bind("<Double-Button-1>",put_in_entry2)
    listbox2.bind("<<SearchTopPackagesMsg>>", _show_top_packages)

def entry_input_focus(string):
    entry.delete(0,"end")
    entry.insert(0,string)
    entry.icursor("end")
    entry.select_range(0,"end")
    entry.focus_set()

def on_select(e):
    global selected
    selected = listbox.selection()
    if not selected:
        return
    selected = selected[0]

require_string=("依赖项","被依赖项")
def put_in_entry(e):
    if not selected:
        return
    name = listbox.item(selected,"text")
    if not name or name in require_string:
        return
    entry_input_focus(name)

def search_dependencies(_name=None):
    global name
    name = _name
    if name:
        entry.delete(0,"end")
        entry.insert(0,name)
    else:
        name = entry.get()
    if not name:
        return
    entry.config(state="disabled")
    depbutton.config(state="disabled")
    delbutton.config(state="disabled")
    clbutton.config(state="disabled")
    pipmode.search_dependency(name,search_msg)

def delete_item():
    global selected
    if not selected:
        return
    parent = listbox.parent(selected)
    while parent != "":
        selected = parent
        parent = listbox.parent(selected)
    listbox.delete(selected)
    selected = None

def clear_list():
    listbox.delete(*listbox.get_children())

def search_msg(_dependencymsg):
    global dependencymsg
    dependencymsg = _dependencymsg
    listbox.event_generate("<<DependencySearchMsg>>")
def _search_msg(e):
    entry.config(state="normal")
    depbutton.config(state="normal")
    delbutton.config(state="normal")
    clbutton.config(state="normal")
    root=listbox.insert("",'end',text=name,open=True)
    reqnode=listbox.insert(root,'end',text="依赖项",open=True)
    for item in dependencymsg[0]:
        listbox.insert(reqnode,'end',text=item.strip())
    reqednode=listbox.insert(root,'end',text="被依赖项",open=True)
    for item in dependencymsg[1]:
        listbox.insert(reqednode,'end',text=item.strip())
    listbox.yview_moveto(1)

def list_no_dep():
    nodepbutton.config(state="disabled")
    pipmode.search_top_packages(show_top_packages)

def on_select2(e):
    global name2
    selected = listbox2.selection()
    if not selected:
        return
    name2 = listbox2.item(selected[0],"text")

def put_in_entry2(e):
    if not name2:
        return
    entry_input_focus(name2)

def show_top_packages(pkgs):
    global top_pkgs
    top_pkgs = pkgs
    listbox2.event_generate("<<SearchTopPackagesMsg>>")
def _show_top_packages(e):
    nodepbutton.config(state="normal")
    listbox2.delete(*listbox2.get_children())
    for item in top_pkgs:
        listbox2.insert("",'end',text=item.strip())

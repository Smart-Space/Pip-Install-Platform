"""
/lib/gui/gui_setting.py
负责展示用户设置界面
"""
from tkinter import PhotoImage, StringVar, IntVar
from tkinter import ttk
from webbrowser import open as webopen
from sys import executable
from lib.operate import setting
from i18n import _


def initialize(frame:ttk.Frame):
    global theme_var
    if setting.get_theme() == 1:
        photo = PhotoImage(file='./logoS.png')
    elif setting.get_theme() == 2:
        photo = PhotoImage(file='./logoDarkS.png')
    naviframe = ttk.Frame(frame)
    naviframe.pack(side='left', fill='y')
    label = ttk.Label(naviframe, image=photo)
    label.image = photo
    label.pack(side='top')
    ttk.Label(naviframe, text="Pip Integration Platform (PIP)" \
    "\n\nAuthor: Smart-Space" \
    "\n\nLicense: MIT").pack(side='top',pady=10)
    ttk.Button(naviframe, text="Source Code", command=lambda: webopen("https://github.com/Smart-Space/Pip-Integration-Platform")).pack(side='top',pady=10)

    frame1 = ttk.Frame(frame)
    frame1.pack(side='left', fill='both', expand=True)
    ttk.Label(frame1, text=_("修改后重启生效")).grid(row=0, columnspan=2, sticky='w', padx=10, pady=10)
    ttk.Label(frame1, text=_("语言")).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    lang_var = StringVar()
    if setting.get_lang() == "zh":
        lang_var.set("中文")
    else:
        lang_var.set("English")
    lang_combo = ttk.Combobox(frame1, textvariable=lang_var, state="readonly", font=("微软雅黑",12))
    lang_combo.option_add('*TCombobox*Listbox.font', ('微软雅黑', 12))
    lang_combo['values'] = ["中文", "English"]
    lang_combo_dict = {"中文": "zh", "English": "en"}
    lang_combo.grid(row=1, column=1)
    lang_combo.bind("<<ComboboxSelected>>", lambda e: set_language(lang_combo_dict[lang_var.get()]))
    ttk.Label(frame1, text=_("当前环境：")+executable).grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=10)
    ttk.Label(frame1, text=_("外观")).grid(row=3, column=0, padx=10, pady=10, sticky='w')
    theme_radio_frame = ttk.Frame(frame1)
    theme_radio_frame.grid(row=3, column=1)
    theme_var = IntVar()
    theme_var.set(setting.get_theme())
    theme_light_radio = ttk.Radiobutton(theme_radio_frame, text=_("明亮"), variable=theme_var, value=1, command=set_theme)
    theme_light_radio.pack(side='left', padx=10)
    theme_dark_radio = ttk.Radiobutton(theme_radio_frame, text=_("暗黑"), variable=theme_var, value=2, command=set_theme)
    theme_dark_radio.pack(side='left', padx=10)

def set_language(lang_code):
    setting.set_lang(lang_code)

def set_theme():
    setting.set_theme(theme_var.get())
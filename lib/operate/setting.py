"""
./lib/operate/setting.py
PIP的设置程序
"""
import subprocess
import os
import json
from sys import executable

setting = {
    'lang': 'zh',
    'theme': 1,
}

def save_setting():
    with open('./setting.json', 'w', encoding='utf-8') as f:
        json.dump(setting, f, ensure_ascii=False, indent=4)

if not os.path.exists('./setting.json'):
    save_setting()
else:
    with open('./setting.json', 'r', encoding='utf-8') as f:
        setting.update(json.load(f))

def get_lang():
    return setting['lang']

def set_lang(lang):
    setting['lang'] = lang
    save_setting()

def get_theme():
    return setting['theme']

def set_theme(theme):
    setting['theme'] = theme
    save_setting()

def clear_cache():
    cmd = f'{executable} -m pip cache purge'
    subprocess.Popen(cmd, shell=True)
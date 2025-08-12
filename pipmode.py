"""
./pipmode.py
负责总调控与pip相关的功能
"""
from lib.operate import pip_list, pip_install, pip_uninstall, pip_search

def get_list(func):#获取已安装的第三方库
    return pip_list.get_list(func)

def check_update(func):#检测更新
    return pip_install.update(func)

def install(update,name,msgfunc,endfunc):
    pip_install.install(update,name,msgfunc,endfunc)

def uninstall(name,msgfunc,endfunc):
    pip_uninstall.uninstall(name,msgfunc,endfunc)

def search_dependency(name,msgfunc):
    pip_search.search_dependency(name,msgfunc)

def search_top_packages(msgfunc):
    pip_search.search_top_packages(msgfunc)

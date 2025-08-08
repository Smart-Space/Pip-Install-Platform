"""
/lib/operate/pip_list.py
获取安装的第三方库
"""
from importlib import metadata
from lib.operate.pip_threads import pipthreads

def __get_list(func):
    packages = []
    for dist in metadata.distributions():
        # dist 对象包含了丰富的元数据
        package_info = {
            "name": dist.name,
            "version": dist.version,
            "summary": dist.metadata["Summary"],
        }
        packages.append(package_info)
    func(packages)

def get_list(func):
    pipthreads.submit(__get_list,func)

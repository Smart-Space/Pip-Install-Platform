"""
/lib/operate/pip_search.py
依赖分析
"""
import subprocess
from sys import executable
from json import loads
from lib.operate.pip_threads import pipthreads


def __search_dependency(name,msgfunc):
    cmd = f"{executable} -m pip show {name}"
    require = []
    requireBy = []
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        output = result.stdout.decode('utf-8')
        for line in output.split('\n'):
            if line.startswith('Requires:'):
                require = line.split(':')[1].split(',')
            elif line.startswith('Required-by:'):
                requireBy = line.split(':')[1].split(',')
    msgfunc((require,requireBy))

def search_dependency(package_name,msgfunc):
    pipthreads.submit(__search_dependency,package_name,msgfunc)

def __search_top_packages(msgfunc):
    cmd = f"{executable} -m pip list --not-required --format=json"
    top_packages = []
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        output = result.stdout.decode('utf-8')
        data = loads(output)
        top_packages = [item['name'] for item in data]
    msgfunc(top_packages)

def search_top_packages(msgfunc):
    pipthreads.submit(__search_top_packages,msgfunc)

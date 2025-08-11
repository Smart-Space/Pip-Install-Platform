@rem launch.example.bat 是 PIP 的一个示例启动文件，全是注释。
@rem
@rem PIP 设计为通过运行的 python 解释器来确定管理的第三方库环境，
@rem 并不提供（暂且不计划）软件内的环境切换，因为即使有设置文件，
@rem 每次启动一个 PIP 软件实例，都是一个确定的环境，环境列表没有意义，
@rem 从设置切换环境不如一开始就指定 python 解释器。
@rem
@rem 此外，如果只靠设置提供具体环境，则无法使用 importlib.metadata，
@rem 而 pip 命令行操作的速度要慢于内置实现。
@rem
@rem 因此，可以给需要的环境编写启动文件。比如给系统python的启动文件命名
@rem "launch.system.bat"，添加：
@rem python "path_to_PIP/main.py"
@rem
@rem 独立环境也可以直接编写启动文件，命名如"launch.python310.bat"，添加：
@rem path_to_python310/python "path_to_PIP/main.py"
@rem
@rem 然后将启动文件放到你想要放的任何位置。
@rem
@rem PIP is designed to determine the managed third-party library environment through
@rem the running python interpreter. Environment switching within the software is not
@rem provided (not planned for the time being), because even if there are setting files,
@rem each time a PIP software instance is started, it is a definite environment. 
@rem The environment list is meaningless. Switching environments from Settings is not
@rem as good as specifying the python interpreter from the very beginning.
@rem
@rem Furthermore, if the specific environment is only provided through Settings,
@rem importlib.metadata cannot be used. However, the speed of pip command-line operations
@rem is slower than that of the built-in implementation.
@rem
@rem Therefore, startup files can be written for the required environment. For example,
@rem name the python startup file of the system "launch.system.bat", add:
@rem python "path_to_PIP/main.py"
@rem
@rem An independent environment can also directly write a startup file, named as
@rem "launch.python310.bat", and add:
@rem path_to_python310/python "path_to_PIP/main.py"
@rem
@rem Then place the startup file wherever you want.
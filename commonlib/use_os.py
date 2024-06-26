import os

path = ''

os.getcwd() #获取当前工作目录，即当前python脚本工作的目录路径

os.chdir() 

os.chdir("dirname")  #改变当前脚本工作目录；相当于shell下cd    os.chdir(r"c:\Users")
os.curdir  #返回当前目录: ('.')，相当于shell下cd.

os.pardir # 获取当前目录的父目录字符串名：('..')，相当于shell下cd.. 返回上一层目录

os.makedirs('dirname1/dirname2')    #可生成多层递归目录      os.makedirs(r"c:\a\b\c")

os.removedirs('dirname1')    #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推      os.removedirs(r"c:\a\b\c")

os.mkdir('dirname')    #生成单级目录；相当于shell中mkdir dirname

os.rmdir('dirname')   # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname

os.listdir('dirname')    #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印        os.listdir("c:\\test")

os.remove()  #删除一个文件                  os.remove(r"c:\oldboy.txt")

os.rename("oldname","newname")  #重命名文件/目录      os.rename("c:\\test","c:\\test2")                    

os.stat('path/filename') # 获取文件/目录信息          os.stat("c:\\test2")

os.sep    #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

os.linesep    #输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"

os.pathsep    #输出用于分割文件路径的字符串 

os.name    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

os.system("bash command")  #运行shell命令，直接显示

os.environ  #获取系统环境变量

os.path.abspath(path)  #返回path规范化的绝对路径

os.path.split(path)  #将path分割成目录和文件名二元组返回

os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素

os.path.basename(path) # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False
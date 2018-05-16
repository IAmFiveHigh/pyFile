import os
from xpinyin import Pinyin

path = input("输入文件夹路径") # 文件目录

files_list = os.listdir(path)

p = Pinyin()

for file in files_list:
    os.rename(path + "/" + str(file), path + "/" + p.get_pinyin(str(file), ""))


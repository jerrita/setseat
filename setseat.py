import random

import os

import seatlib.name as name
import seatlib.seat as seat
import seatlib.getfilepath as getfilepath
import seatlib.savefile
from seatlib.method import *

print('------随机排位系统------\n\n')
path = getfilepath.selectclass()
if path == 0:
    print('未找到此班级\n')
    end()

print('\n数据加载中...')

namelist = name.read(path)
if type(namelist) != list:
    print('姓名文件有误，请检查后重试！')
    end()
classdata = seat.getseat(path)
if type(classdata) != list:
    print('座次文件有误，请检查后重试！')
    end()

#检查人数是否匹配
t = 0
for i in classdata:
    t += i
print('目前有%d人，%d座位\n' %(len(namelist),t))
if len(namelist) > t:
    print('人数大于座位，无法进行排位，请修改班级数据后再试！')
    end()
if len(namelist) < t:
    print('人数小于座位数，暂时无法进行排位，请修改班级数据后再试！')
    end()


#开始排位，排位方式：从第一排往后
random.shuffle(namelist)
seattable = []
n = 0
#储存结果
for i in classdata:
    seattable.append([])
    num = int(i)
    for i in range(num):
        seattable[n].append(namelist.pop())
    n += 1

t = path.split('/')[1].split('-')
if not os.path.isdir('output'): os.mkdir('output')
seatlib.savefile.savefile('output/高%s（%s）班坐次表.xls'%(ntc(t[0]),t[1]),seattable)
end()
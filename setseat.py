import seatlib.name as name
import seatlib.seat as seat
import seatlib.getfilepath as getfilepath
from seatlib.method import *

print('------随机排位系统------\n\n')
path = getfilepath.selectclass()
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
if len(namelist) != t:
    print('bupipei')
else:
    print('asjdfahdfahsg')
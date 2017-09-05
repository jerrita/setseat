import os.path
import seatlib.method

gr = input('-----座位数据生成器-----\n\n请输入年级(1,2,3):')

if gr not in ['1','2','3']:
    while True:
        gr = input('数据输入错误，请重新输入:')
        if gr in ['1','2','3']: break

cls = input('请输入班级(阿拉伯数字):')
if len(cls) == 0:
    while True:
        cls = input('请输入班级(阿拉伯数字):')
        if len(cls) != 0: break

print('\n您选择的班级是：高%s（%s）班，正在加载数据...\n'%(seatlib.method.ntc(gr),cls))

if os.path.exists('data/' + gr + '-' + cls):
    if os.path.exists('data/' + gr + '-' + cls + '/seat.txt'):
        pass
    else:
        pass
else:
    pass
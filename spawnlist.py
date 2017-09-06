import os
from seatlib.method import *

def setseatdata(classname,classdir):
    print('程序开始运行，即将生成的是 %s 的座位数据，请根据提示输入数据\n'%classname)
    x = int(input('请输入列数（阿拉伯数字）：'))
    fp = open(classdir,'w')
    t = 1
    for i in range(x):
        k = input('请输入第%d列人数：' % t)
        fp.write(('0' if len(k) == 0 else k) + ' ')
        t += 1
    print('录入完成！运行setseat即可随机排位')
    fp.close()

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

print('\n您选择的班级是：高%s（%s）班，正在加载数据...\n'%(ntc(gr),cls))

if os.path.exists('data/' + gr + '-' + cls):
    if os.path.exists('data/' + gr + '-' + cls + '/seat.txt'):
        choice = input('座位数据已存在，是否覆盖(y/n)？')
        if choice == 'y':
            setseatdata('高%s（%s）班'%(ntc(gr),cls),'data/' + gr + '-' + cls + '/seat.txt')
            end()
        else:
            end()
else:
    if not os.path.exists('data'): os.mkdir('data')
    os.mkdir('data/' + gr + '-' + cls)
    setseatdata('高%s（%s）班' % (ntc(gr), cls), 'data/' + gr + '-' + cls + '/seat.txt')
    end()
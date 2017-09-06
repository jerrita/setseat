import glob
import os.path
import seatlib.method

def selectclass():
    pathlist = glob.glob('data\\*')
    result = []
    classlist = []
    for i in pathlist:
        if os.path.isdir(i):
            classlist.append(i)
            tmp = i.split('\\')[-1].split('-')
            result.append('高%s（%s）班'%(seatlib.method.ntc(tmp[0]),tmp[1]))

    count = 0
    print('班级列表\n-------------------')
    for i in result:
        print(count,':   ',i)
        count += 1
    put = int(input('\n请选择班级（序号）：'))
    return classlist[put] if put <= count-1 and put >= 0 else 0

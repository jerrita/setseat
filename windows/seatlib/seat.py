def getseat(path):
    fp = open(path + '\\seat.txt')
    txt = fp.read().split(' ')
    ret = []
    for i in txt:
        if len(i) == 0:continue
        ret.append(int(i))
    return ret if len(ret) != 0 else 0

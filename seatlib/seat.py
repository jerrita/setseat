def getseat(cls):
    fp = open('data/' + cls + '/seat.txt')
    txt = fp.read().split(' ')
    ret = []
    for i in txt:
        if len(i) == 0:continue
        ret.append(int(i))
    return ret
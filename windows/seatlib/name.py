import os.path

def read(name):
    filepath = name + '\\name.txt'
    if os.path.exists(filepath):
        fp = open(filepath,'r')
        txt = fp.read()
        fp.close()

        #处理文件，返回列表
        tmp = txt.split('\n')
        result = []
        for i in tmp:
            if len(i) == 0: continue
            result.append(i)
        return result if len(result) != 0 else 0
    else: return 0


import xlwt
def savefile(filename,seattable):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('seat')
    x = 0
    y = 0
    for i in seattable:
        for j in i:
            sheet.write(y,x,j)
            y += 1
        x += 1
        y = 0
    wbk.save(filename)
    print('\n生成成功！生成文件保存在',filename.split('/')[1])
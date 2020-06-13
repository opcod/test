# -*- coding: utf-8 -*-
import xlrd
import xlwt
import datetime
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'/home/op/Desktop/demo.xlsx')
    # 获取所有sheet的名字
    #print(workbook.sheet_names())
    # sheet1索引从0开始，得到sheet1表的句柄
    sheet1 = workbook.sheet_by_index(0)
    # rowNum = sheet1.nrows
    # colNum = sheet1.ncols
    # s = sheet1.cell(1,0).value.encode('utf-8')
    s = sheet1.cell(2, 0).value
    # print(s)
    # 获取某一个位置的数据
    # 1 ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    # print(sheet1.cell(2,0).ctype)
    # print(s.decode('utf-8'))
    # 获取整行和整列的数据
    # 第二行数据
    row2 = sheet1.row_values(1)
    #print(row2)
    # 第一列数据
    global cols1
    cols1 = sheet1.col_values(0,2)
    # print(cols1)
    # 查看cols1的类型
    # print(type(cols1))
    # 新建一个变量i在列表cols1里面循环
    # global i,date
    for i in cols1:
        # 得到i的值，打印值和值的类型
        # print(i,type(i))
        #将得到的字符串为日期类型，参数%Y.%m.%d'表示原字符串的格式
        date =datetime.datetime.strptime(i,'%Y.%m.%d')
        # print(date,type(date))
read_excel()
#写入数据
def write_excel():
    f = xlwt.Workbook()
#创建sheet1
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    # 创建一个空列表
    a = list()
    # 创建一个变量在列表cols1循环
    for i in cols1:
        # 将i格式化到时间类型
        date = datetime.datetime.strptime(i,'%Y.%m.%d')
        # print("这里是date",date,type(date),id(date))
        # 将时间类型转为字符串
        str_time= date.strftime('%Y-%m-%d %H:%M:%S')
        # 将字符串添加到列表里面
        a.append(str_time)
        # 创建一个循环在列表0值和最大值之间
    for o in range(0,len(a)):
           # 下面这行代码扩号内的意思是（从o行循环+起始行，列，写入的列表【循环行】）
        sheet1.write(o+2,0,a[o])
    else:
        print("程序已经完成")
    # print(a, type(a), id(a))
    f.save('datatest.xls')
write_excel()


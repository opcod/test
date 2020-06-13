def xc(a,b):
    '''测试形参和实际参数20200308'''
    if a>b:
        print("{0}和{1}比，{0}比较大".format(a,b))
    if a<b:
        print("{0}和{1}比，{1}比较大".format(a, b))
    if a==b:
        print("{0}和{1}比，他们相等".format(a,b))
    return
xc(23,34)
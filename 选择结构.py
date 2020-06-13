def op():
    try:
        age = int(input("您几岁了，请输入一个整数数字:"))
        if 0 < age <= 9:
            pr = "你还是个小孩儿"
            print(pr)
        elif 9 < age <= 20:
            pr = "前途无量啊年轻人"
            print(pr)
        elif 20 < age <= 30:
            pr = "年轻人好好工作"
            print(pr)
        elif age > 30 and age <= 100:
            pr = "您的年龄有点大额"
            print(pr)
        elif age > 100 and age <= 120:
            pr = "长命的人啊"
            print(pr)
        else:
            print("你不是地球的吧")
    except:
        print("您输入的不是数字,请重新输入！")
        return(op())
op()


#怎么是实现它可以循环输入的不是数字的话
#完成于20200306 18:40
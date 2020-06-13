import numpy as np #导入numpy并以np命名
import random #插入一个随机数组
import tkinter as tk
window = tk.Tk() #建立窗口
window.title("随机彩票")
window.geometry('400x400+800+200')  # 这里的乘是小x,设置窗口大小
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
var2= tk.StringVar()
l = tk.Label(window, textvariable=var, bg='white', fg='gray', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
#创建一个标签l
l.pack() #将标签放到窗口内
l1 =tk.Label(window,textvariable=var2, bg='white', fg='gray', font=('Arial', 12), width=30, height=2)
l1.pack()

def buy(): #随机彩票函数
    red = random.sample(range(1,33),6)
    blue = random.sample(range(1,16),1)
    print(np.sort(red),blue) #np.sort排序red
    var.set(np.sort(red)) #给var赋值
    var2.set(blue)
b=tk.Button(window,text='生成随机彩票',command=buy) #创建一个按钮
b.pack() #放置到窗口中
window.mainloop() #启动窗口






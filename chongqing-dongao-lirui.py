from threading import Timer
from selenium import webdriver
import time
from datetime import datetime

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'C:\chromedriver.exe')
# r表示“原始表示”，不转义
wd.implicitly_wait(5)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://chongqing.dongao.com/')


time.sleep(10)
username=wd.find_element_by_css_selector('input#idcard')
username.send_keys('320583199801130221')

password=wd.find_element_by_css_selector('input#realname')
password.send_keys('李睿')

time.sleep(60)

#弹窗处理
def alert():
    print('正在执行弹窗0')
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if 'http://jxjycwweb.dongao.com/' in wd.current_url:
            break
    print(wd.title,datetime.now())
    try:
        wd.find_element_by_css_selector('[value="A"]').click()
        print('找到弹窗0目标并执行',datetime.now())
        try:
            time.sleep(2)
            wd.find_element_by_css_selector('span.box-sure').click()
            tip=wd.find_element_by_css_selector('.no-ans-panel  > p')
            if '请选择正确的答案' in tip.text:
                print('A选项错误了，1秒后将执行弹窗1')
                time.sleep(2)
                wd.find_element_by_css_selector('.pop_all.pop-tip-panel span.box-sure').click()
                Timer(1.0, alert1).start()
            Timer(30.0, alert).start()
        except:
            wd.find_element_by_css_selector('span.box-sure').click()
            print('选项正确，将重新执行弹窗0')
            Timer(30.0, alert).start()
    except:
        print('未找到弹窗0目标，60秒重新执行')
        Timer(60.0,alert).start()
def alert1():
    print('正在执行弹窗1')
    try:
        wd.find_element_by_css_selector('[value="B"]').click()
        print('找到弹窗1目标并执行',datetime.now())
        try:
            time.sleep(2)
            wd.find_element_by_css_selector('span.box-sure').click()
            tip = wd.find_element_by_css_selector('.no-ans-panel  > p')
            if '请选择正确的答案' in tip.text:
                print('B选项错误了，1秒后将执行弹窗2')
                time.sleep(2)
                wd.find_element_by_css_selector('.pop_all.pop-tip-panel span.box-sure').click()
                Timer(1.0, alert2).start()
        except:
            wd.find_element_by_css_selector('span.box-sure').click()
            print('选项正确，将重新执行弹窗0')
            Timer(30.0, alert).start()
    except:
        print('未找到弹窗1目标，将执行弹窗0')
        Timer(30.0, alert).start()
def alert2():
    print('正在执行弹窗2')
    try:
        wd.find_element_by_css_selector('[value="C"]').click()
        print('找到弹窗2目标并执行',datetime.now())
        try:
            time.sleep(2)
            wd.find_element_by_css_selector('span.box-sure').click()
            tip = wd.find_element_by_css_selector('.no-ans-panel  > p')
            if '请选择正确的答案' in tip.text:
                print('C选项错误了，1秒后将执行弹窗3')
                time.sleep(2)
                wd.find_element_by_css_selector('.pop_all.pop-tip-panel span.box-sure').click()
                Timer(1.0, alert3).start()
        except:
            wd.find_element_by_css_selector('span.box-sure').click()
            print('选项正确，将重新执行弹窗0')
            Timer(30.0, alert).start()
    except:
        print('未找到弹窗2目标，将执行弹窗0')
        Timer(30.0, alert).start()
def alert3():
    print('正在执行弹窗3')
    try:
        wd.find_element_by_css_selector('[value="D"]').click()
        print('找到弹窗3目标并执行',datetime.now())
        try:
            time.sleep(2)
            wd.find_element_by_css_selector('span.box-sure').click()
            tip = wd.find_element_by_css_selector('.no-ans-panel  > p')
            if '请选择正确的答案' in tip.text:
                print('D选项错误了，1秒后将执行弹窗0 ')
                time.sleep(2)
                wd.find_element_by_css_selector('.pop_all.pop-tip-panel span.box-sure').click()
                Timer(1.0, alert).start()
        except:
            wd.find_element_by_css_selector('span.box-sure').click()
            print('选项正确，将重新执行弹窗0')
            Timer(30.0, alert).start()
    except:
        print('未找到弹窗3目标，将执行弹窗0')
        Timer(30.0, alert).start()
alert()

# 关闭
# wd.quit()
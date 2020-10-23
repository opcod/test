from threading import Timer
from selenium import webdriver
import time

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'E:\test\drive\chromedriver.exe')
# r表示“原始表示”，不转义
wd.implicitly_wait(5)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://kj.czt.gxzf.gov.cn:7005/txweb/commons/accountinglogin')
username=wd.find_element_by_id('username')
username.send_keys('450205198706190719')



password=wd.find_element_by_id('password')
password.send_keys('iwillBE2020')

checkCode=wd.find_element_by_id('checkCode')
code=checkCode.get_property('value')

yzm=wd.find_element_by_id('yzm')
yzm.send_keys(code)

login=wd.find_element_by_class_name('login_btn')
login.click()

time.sleep(1)

u1=wd.find_element_by_id('u1')
lis=u1.find_elements_by_tag_name('li')
for li in lis:
    if li.text=='网络继续教育学习':
        li.click()
wd.get('http://kj.czt.gxzf.gov.cn:7005/txweb/collection/toPage?type=edu3')

time.sleep(1)

buttoninfo=wd.find_element_by_class_name('buttoninfo')
bt1s=buttoninfo.find_elements_by_class_name('layui-btn')
for bt1 in bt1s:
    if bt1.text=='无修改和补充，需进行网络继续教育学习':
        bt1.click()


wd.get('http://kj.czt.gxzf.gov.cn:7005/gx-eams/Actions/Net/Internal/NetService/ApplyOnlineEduAction.do?method=getOnlinePayInfo&flag=201014085351416')

time.sleep(3)

wd.find_element_by_id('cb_only_show_selected').click()

wd.get('https://ce.esnai.net/c/accguangxi/study.jsp?tid=3736&code=ZFKJZZZDJJ')

wd.get('https://ce.esnai.net/c/public/showflashvideo.jsp?type=1&cwid=3659&tid=3736')

print(wd.title)

wd.find_element_by_css_selector('.pv-controls-left button').click()

wd.find_element_by_css_selector('.pv-controls-right .pv-volumebtn').click()
#弹窗处理
def alert():
    print('正在执行弹窗0')
    try:
        wd.find_element_by_css_selector('#examcontent label:nth-of-type(1) input').click()
        wd.find_element_by_css_selector('#examcontent [value=确定]').click()
        print('找到弹窗0目标并执行')
        try:
            wd.switch_to.alert.accept()
            print('第一个选项错误了，1秒后将执行弹窗1')
            Timer(1.0, alert1).start()
        except:
            print('弹窗确认出错')
    except:
        print('未找到弹窗0目标，30秒重新执行')
        Timer(30.0,alert).start()
def alert1():
    print('正在执行弹窗1')
    try:
        wd.find_element_by_css_selector('#examcontent label:nth-of-type(2) input').click()
        wd.find_element_by_css_selector('#examcontent [value=确定]').click()
    except:
        print('未找到弹窗1目标，将执行弹窗0')
        Timer(30.0, alert).start()
alert()

# 关闭
# wd.quit()
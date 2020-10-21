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

table=wd.find_elements_by_from_name('table')
tbody=table.find_element_by_tag_name('tbody')
trs=tbody.find_elements_by_tag_name('tr')
for tr in trs:
    print(tr.text)
# 关闭
wd.quit()
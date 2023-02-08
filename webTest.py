import selenium
from selenium import webdriver
import time
def open_url(driver,url):
    driver.get(url) #登入网站
    driver.maximize_window() #最大化窗口

# ———————————————通过id定位—————————————————————
def login_page(driver,username,password):
    page_text = driver.find_element('xpath', '//b[contains(text(),"柠檬")]').text
    page_title = driver.title
    print("page_title is {}".format(page_title))
    if page_text=='柠檬ERP':
        print("标题验证通过!")
    else:
        print("wrong page_text!")
    driver.find_element('id','username').send_keys(username) #寻找元素并发送关键字
    driver.find_element('xpath','//input[@id="password"]').send_keys(password)
    driver.find_element('id','btnSubmit').click()
# ————————————————通过元素定位——————————————————————
def search_key(url,driver,username,password,s_key):
    open_url(driver,url)
    login_page(driver,username,password)
    test_user=driver.find_element('xpath','//p[text()="测试用户"]').text
    if test_user=='测试用户':
        print('用户名称为：{}'.format(test_user))
    else:
        print('用户名称异常，测试用例不通过')
    # p_id=driver.find_element('xpath',"//span[text()='零售出库']/..").get_attribute("data-tab-id")
    # print(p_id)
    # F_id=p_id+'-frame'
    driver.find_element('xpath',"//span[text()='零售出库']").click()
    driver.switch_to.frame(1)
    driver.find_element('id','searchNumber').send_keys(s_key)
    driver.find_element('id','searchBtn').click()
    time.sleep(3)
    num=driver.find_element('xpath','//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num


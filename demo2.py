#切换ifame

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://login.anjuke.com/login/form')
#定位到登录框的frame元素
webIframe=driver.find_element_by_id("iframeLoginIfm")
#切换到iframe
driver.switch_to.frame(webIframe)
#输入手机号
driver.find_element_by_id('phoneIpt').send_keys('178384383')
#切换到上一级frame
driver.switch_to.parent_frame()
driver.find_element_by_link_text('关于安居客')

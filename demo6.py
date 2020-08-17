#聚合 登录

from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.juhe.cn/')

#time.sleep(13)
driver.implicitly_wait(30)   #设置元素的最长等待时间

frame=driver.find_element_by_xpath('//iframe[@id="layui-layer-iframe1"]')
driver.switch_to.frame(frame)
driver.find_element_by_xpath('//div[@class="inputWrap"]/input[@type="text"]').send_keys('17602125335')
driver.find_element_by_id('smsbtn').click()


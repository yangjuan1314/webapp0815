#百度首页图片搜索、

from  selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://www.baidu.com')

driver.find_element_by_xpath('//span[@class="soutu-btn"]').click()
time.sleep(2)
driver.find_element_by_xpath('//input[@type="file"]').send_keys(r'‪D:\111.jpg')
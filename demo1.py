#鼠标移动悬浮按钮
#浏览器窗口切换


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.baidu.com/')

mork_link=driver.find_element_by_xpath('//div/a[@class="s-bri c-font-normal c-color-t"]')

#实例化对象
actions=ActionChains(driver)
#把鼠标移动到元素上
actions.move_to_element(mork_link).perform()

#点击百度音乐
driver.find_element_by_xpath('//a[@name="tj_mp3"]').click()

#获得所有的浏览器窗口
all_hndle=driver.window_handles
#切换到最后一个浏览器窗口
driver.switch_to_window(all_hndle[-1])

#新打开的页面，输入内容
driver.find_element_by_id('kw').send_keys('hello')

#切换到上一级浏览器窗口
driver.switch_to_window(all_hndle[0])
driver.find_element_by_id('kw').send_keys('haohaoxuexi')
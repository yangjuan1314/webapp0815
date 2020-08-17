#自动登录并发布话题
from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://49.233.108.117:3000/')
driver.find_element_by_xpath('//div[@class="container"]//ul/li[6]').click()
#登录
driver.find_element_by_id('name').send_keys('test9')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_xpath('//div[@class="form-actions"]/input[@type="submit"]').click()

#点击发布话题的按钮
driver.find_element_by_xpath('//span[@class="span-success"]').click()
#选择框选择
driver.find_element_by_xpath('//select[@name="tab"]//option[2]').click()
#文本框输入内容
driver.find_element_by_id('title').send_keys('第一次测试这里。。')
#输入发布话题
md_div=driver.find_element_by_xpath('//div[@class="CodeMirror-scroll"]')
md_div.click()
#把鼠标移动到元素上
ActionChains(driver).move_to_element(md_div).send_keys('hello world')\
    .pause(2)\
    .send_keys(Keys.ENTER)\
    .send_keys(Keys.ENTER)\
    .pause(1).send_keys('### web自动化')\
    .send_keys(Keys.ENTER)\
    .send_keys('hahahhahaha')\
    .key_down(Keys.CONTROL).key_down(Keys.SHIFT).key_down(Keys.ARROW_LEFT)\
    .key_up(Keys.ARROW_LEFT).key_up(Keys.SHIFT).key_up(Keys.CONTROL)\
    .key_down(Keys.CONTROL).send_keys('b')\
    .key_up(Keys.CONTROL)\
    .pause(2)\
    .perform()        #pause停止等待几秒,

# driver.find_element_by_xpath('//div/a[@class="eicon-image"]').click()
# driver.find_element_by_xpath('//input[@type="file"]').send_keys(r'‪C:\Users\许晨晨\Desktop\111.jpg')

#点击话题发布提交按钮
driver.find_element_by_xpath('//input[@type="submit"]').click()

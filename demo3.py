#切换alert

from selenium import webdriver

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('http://49.233.108.117:3000/')
driver.find_element_by_xpath('//div[@class="container"]//ul/li[6]').click()
#登录
driver.find_element_by_id('name').send_keys('test9')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_xpath('//div[@class="form-actions"]/input[@type="submit"]').click()

#打开个人中心
driver.get('http://49.233.108.117:3000/user/test9')
#选择一个发布内容
driver.find_element_by_xpath('//a[@class="topic_title"]').click()

#定位到删除按钮
driver.find_element_by_xpath('//div[@id="manage_topic"]//i[@class="fa fa-lg fa-trash"]').click()

#切换到alert窗口
alerwindow=driver.switch_to.alert
#对话框的文本
print(alerwindow.text)
#点击alert确定
alerwindow.accept()
# #点击alert取消
# alerwindow.dismiss()





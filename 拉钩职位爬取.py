from  selenium import webdriver
import time


driver=webdriver.Chrome(executable_path='chromedriver.exe')

#打开拉钩网页
driver.get('https://www.lagou.com/')

#最大化窗口
driver.maximize_window()

#全屏窗口
driver.fullscreen_window()

# #选择城市，做个封装
def  choose_city(name):
    return  driver.find_element_by_xpath(f'//a[@data-city="{name}"]')

ele=choose_city("上海")
ele.click()

#定位输入框
driver.find_element_by_xpath('//input[@id="search_input"]').send_keys("自动化工程师")
driver.find_element_by_xpath('//input[@class="search_button"]').click()
#关闭搜索弹框
driver.find_element_by_xpath('//div[@class="body-btn"]').click()
#获取搜索结果
while True:
    time.sleep(4)
    #获取页面中的值
    els=driver.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
    for el in els:
        print(el.text)
    with open('lagou_data.txt',mode='a',newline='') as f:
        f.write(el.text)
    #获取下一页的属性
    next_but=driver.find_element_by_xpath('//span[@action="next"]')
    #将元素滚动到视图
    next_but.location_once_scrolled_into_view
    #获取属性值
    next_but_class=next_but.get_attribute('class')
    if 'pager_next pager_next_disabled' in next_but_class:
        break
    #点击下一页
    next_but.click()



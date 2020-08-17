from selenium  import  webdriver
import time


#创建浏览器实例
driver=webdriver.Chrome(executable_path='chromedriver.exe')

#打开百度浏览器
driver.get("http://www.jd.com")

# #通过id定位
# driver.find_element_by_id('kw').send_keys('helloworld')
# time.sleep(1)
#
# #清空输入框
# driver.find_element_by_id('kw').clear()
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys('fanmao')
# driver.find_element_by_id('su').click()

driver.find_element_by_xpath('//*[@id="key"]').send_keys('华为')
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
time.sleep(3)
#定位所有商品
goodslist=driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
print(type(goodslist),len(goodslist))

#输入每个商品的名称与价格
for i in range(1,len(goodslist)+1):
    good_price=driver.find_element_by_xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]//strong/i').text
    good_name=driver.find_element_by_xpath(f'//*[@id="J_goodsList"]/ul/li[{i}]//div[@class="p-name p-name-type-2"]//em').text
    print(f'{good_name},{good_price}')
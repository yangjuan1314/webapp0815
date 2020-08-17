#百度地图

from selenium import webdriver

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://map.baidu.com/')
driver.implicitly_wait(30)   #隐式等到最长30s

driver.find_element_by_xpath('//input[@id="sole-input"]').send_keys('宜川五村')
driver.find_element_by_id('search-button').click()

driver.find_element_by_xpath('//div[@class="BMap_Marker BMap_noprint"]').click()
driver.find_element_by_xpath('//div[@id="route-go"]//span[@class="generalHead-right-route-text time-delay animation-common"]').click()
driver.find_element_by_xpath('//div[@class="routebox-input route-start"]//input[@autocomplete="off"]').send_keys('嘉禾国际大厦')
driver.find_element_by_id('search-button').click()
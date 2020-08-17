#显示等待

from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.lagou.com/')

# try:
wait=WebDriverWait(driver,10)
wait.until(lambda driver:driver.find_element_by_id('cboxClose')).click()
driver.find_element_by_xpath('//input[@id="search_input"]').send_keys("测试工程师")
driver.find_element_by_xpath('//input[@id="search_button"]').click()
# except Exception:
#     wait=WebDriverWait(driver,10)
#     ele=wait.until(lambda driver:driver.find_element_by_id('cboxClose'))
#     ele.click()

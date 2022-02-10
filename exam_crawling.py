from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver',
                          options=options)

url = 'https://www.google.com/'
driver.get(url)

driver.find_element_by_name('q').send_keys('발라드')
driver.find_element_by_name('q').send_keys(Keys.ENTER)







# url = 'https://www.naver.com/'
# driver.get(url)
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# #driver.find_element_by_xpath('//*[@id="id"]').send_keys('scolpig')
# driver.find_element_by_name('id').send_keys('scolpig')
# driver.find_element_by_xpath('//*[@id="pw"]').send_keys('********')
# #driver.find_element_by_name('id').send_keys('********')
# driver.find_element_by_xpath('//*[@id="log.login"]').click()
# time.sleep(10)



# url = 'https://klyrics.net/category/korean/'
# driver.get(url)
# driver.find_element_by_xpath(
#     '//*[@id="tdi_66"]/article[1]/div/div[2]/header/h2/a').click()
# title1 = driver.find_element_by_xpath('//*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]').text
# print(title1)
# driver.back()
# driver.find_element_by_xpath(
#     '//*[@id="tdi_66"]/article[2]/div/div[2]/header/h2/a').click()
# title2 = driver.find_element_by_xpath('//*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]').text
# print(title2)
# driver.back()
# driver.find_element_by_xpath('//*[@id="tdi_61"]/div/div[1]/div/div[3]/div[2]/a[2]').click()
# //*[@id="tdi_66"]/article[1]/div/div[2]/header/h2/a
# //*[@id="tdi_66"]/article[2]/div/div[2]/header/h2/a
# //*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]
# //*[@id="tdi_63"]/div/div/div/div[1]/div/p[1]

#driver.close()
# //*[@id="pw"]









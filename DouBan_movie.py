from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from time import sleep
import random
import time
import re

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome('D:\My Programs\Python\Python38\Scripts\chromedriver.exe', options=chrome_options)

url_1 = 'https://www.douban.com'
url_2 = 'https://movie.douban.com/subject/26100958/comments?start=0&limit=20&sort=new_score&status=P'

# browser = webdriver.Chrome()
browser.get(url_1)

browser.implicitly_wait(10)

# 重点1要先切换到子框架
browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])

# 重点2要先点击用账号密码登录的按钮，不然会找不到输入账号和密码的地方
bottom1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
bottom1.click()

input1 = browser.find_element_by_id('username')
input1.clear()
input1.send_keys('17637946697')

input2 = browser.find_element_by_id('password')
input2.clear()
input2.send_keys('zxcvbnm4543')

time.sleep(3)

bottom = browser.find_element_by_class_name('account-form-field-submit')
bottom.click()
time.sleep(2)

browser.get(url_2)
wait = WebDriverWait(browser, 10)


for i in range(1, 26):
    html = browser.page_source
    doc = pq(html)
    items = doc('.comment').items()
    for item in items:
        data = item.find('.short').text()
        data = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", data)
        comment = re.sub('[\W_+]', "", data)
        with open('Avengers4.txt', 'a+', encoding='utf-8') as f:
            f.write(comment)
        # print(comment)
    sleep(random.uniform(1.0, 3.0))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.center .next')))
    submit.click()
    sleep(random.uniform(3.0, 5.0))
    print("第{}页评论下载完毕！".format(i))
    i += 1

print("下载完毕！")

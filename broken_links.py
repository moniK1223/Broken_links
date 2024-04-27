import time
import requests

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
driver.get('https://tutorialsninja.com/demo/')
time.sleep(2)

links_list = driver.find_elements('tag name', 'a')      ## [we1, we2, we3, we4, we5, we6, we7,...]

# for link in links_list:
#     url = link.get_attribute('href')
#     print(url)

for link in links_list:
    url = requests.head(link.get_attribute('href'))

    if url.status_code != 200:
        print(link.get_attribute('href'))




















# Запуск браузера в скрытом режиме

from selenium import webdriver
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=new')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://stepik.org/course/104774')
    element = browser.find_element(By.TAG_NAME, 'a')
    print(element.get_attribute('href'))
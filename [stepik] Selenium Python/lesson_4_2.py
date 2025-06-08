import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Закрытие браузера после выполнения скрипта

# Способ 1. Если произойдет ошибка до выполнения browser.quit() - браузре закрыт не будет

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, 'sale_button')
time.sleep(2)
button.click()
time.sleep(2)

browser.quit()


# Способ 2. Оборачиваем в try-finally. Код в finally будет выполнен всегда.

try:
    browser = webdriver.Chrome()
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = browser.find_element(By.ID, 'sale_button')
    time.sleep(2)
    button.click()
    time.sleep(2)
finally:
    browser.quit()


# Способ 3. Использование менеджера контекста

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = browser.find_element(By.ID, 'sale_button')
    time.sleep(2)
    button.click()
    time.sleep(2)

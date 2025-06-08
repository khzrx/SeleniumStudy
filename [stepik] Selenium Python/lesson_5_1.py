# Запуск браузера с расширениями

from selenium import webdriver
import time

# Расширение предварительно установить на основной браузер и упаковать
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--disable-features=DisableLoadExtensionCommandLineSwitch")
options_chrome.add_extension('../chrome_extensions/coordinates.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)

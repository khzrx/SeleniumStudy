from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://example.com')
time.sleep(5)
browser.quit()
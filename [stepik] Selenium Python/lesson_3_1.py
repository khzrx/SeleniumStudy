from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = 'https://parsinger.ru/2.1/DOM/index2.html'
browser.get(url)
element = browser.find_element(By.ID, 'text777')
print(element.text)
browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

#Получение всех данных из блочного элемента

browser = webdriver.Chrome()
browser.get('https://parsinger.ru/html/watch/1/1_5.html')

element = browser.find_element(By.CLASS_NAME, 'description')
text = element.text

browser.quit()

print(repr(text))

# Получение данных из строчных элементов

# <div class="product">
#     <span class="price">1000 ₽</span>
#     <a href="/product/1" class="title">Наушники Hoco EQ2 Black</a>
#     <span class="stock">В наличии: 21</span>
# </div>

browser = webdriver.Chrome()
browser.get('https://parsinger.ru/3.2/simple_product_page.html')

product =  browser.find_element(By.CLASS_NAME, 'product')

price = product.find_element(By.CLASS_NAME, 'price').text
title = product.find_element(By.CLASS_NAME, 'title').text
stock = product.find_element(By.CLASS_NAME, 'stock').text

print(price, title, stock, sep='\n')
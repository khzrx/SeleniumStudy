from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def tmp_1():
    url = 'http://parsinger.ru/selenium/3/3.html'
    browser = webdriver.Chrome()
    browser.get(url)
    elem = browser.find_element(By.CLASS_NAME, 'text')
    print(elem)
    browser.quit()


def task_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
        browser.find_element(By.ID, 'clickButton').click()
        code = browser.find_element(By.ID, 'codeOutput').text
        print('Код:', code)


def task_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
        browser.find_element(By.ID, 'codeInput').send_keys('Дрогон')
        browser.find_element(By.ID, 'clickButton').click()
        code = browser.find_element(By.ID, 'codeOutput').text
        print('Код:', code)


def task_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
        browser.find_element(By.ID, 'showTextBtn').click()
        password = browser.find_element(By.ID, 'text1').text
        browser.find_element(By.ID, 'userInput').send_keys(password)
        browser.find_element(By.ID, 'checkBtn').click()
        code = browser.find_element(By.ID, 'text2').text
        print('Код:', code)


def task_4():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
        element = browser.find_element(By.ID, 'secret-key-button')
        element.click()
        print(element.get_attribute('data'))

task_4()
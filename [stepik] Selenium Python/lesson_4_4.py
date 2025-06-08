from selenium import webdriver
from selenium.webdriver.common.by import By


def tmp_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/selenium/3/3.html')
        link = browser.find_element(By.CLASS_NAME, 'text')
        print(type(link))
        print(link.text)


def tmp_2():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/selenium/3/3.html')
        links = browser.find_elements(By.CLASS_NAME, 'text')
        print(links)


def tmp_3():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/selenium/3/3.html')
        link = browser.find_element(By.XPATH, '//div[@class="text"]/p[2]')
        print(link.text)


def tmp_4():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/selenium/3/3.html')
        links = browser.find_elements(By.XPATH, '//div[@class="text"]/p[2]')
        print(*[link.text for link in links], sep='\n')


def tmp_5():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/selenium/3/3.html')
        divs = browser.find_elements(By.CLASS_NAME, 'text')

        for i, div in enumerate(divs, start=1):
            first_p = div.find_element(By.XPATH, './p[1]').text
            third_p = div.find_element(By.XPATH, './p[3]').text

            print(f'Для div #{i} первый <p> = {first_p}, третий <p> = {third_p}.')


def task_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
        links = browser.find_elements(By.TAG_NAME, 'a')
        total = 0

        for link in links:
            attr_value = link.get_attribute('stormtrooper')
            total += int(attr_value) if attr_value.isdigit() else 0

        browser.find_element(By.ID, 'inputNumber').send_keys(str(total))
        browser.find_element(By.ID, 'checkBtn').click()
        print(browser.find_element(By.ID, 'feedbackMessage').text)


def task_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
        parent = browser.find_element(By.ID, 'parent_id')
        child = parent.find_element(By.CLASS_NAME, 'child_class')
        child.click()
        print(child.get_attribute('password'))


def task_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
        blocks = browser.find_elements(By.CLASS_NAME, 'block')

        for block in blocks:
            block.find_element(By.TAG_NAME, 'button').click()

        print(browser.find_element(By.TAG_NAME, 'password').text)


task_3()
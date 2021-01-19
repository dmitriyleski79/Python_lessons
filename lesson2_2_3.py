from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    

    num1 = browser.find_element_by_id('num1')
    x = num1.text
    num2 = browser.find_element_by_id('num2')
    y = num2.text
    #str(int(x)+int(y))
    sum_el = str(int(x)+int(y))

    #def cacl(a, b):
    #  return a + b
    print('xxxx' + x)
    print('yyyy' + y)
    print('!!!!!: ' + sum_el)
    

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(sum_el)

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

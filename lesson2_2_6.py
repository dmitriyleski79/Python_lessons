from selenium import webdriver
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    

    input_field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(calc(x))

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('[type="submit"]')
    
    

finally:
    time.sleep(7)
    
    browser.quit()

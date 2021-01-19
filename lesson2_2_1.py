from selenium import webdriver
import math
import time


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    time.sleep(1)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("!!!!!!!value of people radio: ", people_checked)

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    robot_checkbox.click()

    robots_rule_checkbox = browser.find_element_by_id('robotsRule')
    robots_rule_checkbox.click()

    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

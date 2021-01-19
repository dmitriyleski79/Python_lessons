from selenium import webdriver
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sheets = browser.find_element_by_id('treasure')
    sheets_attribute = sheets.get_attribute('valuex')

    ansver_field = browser.find_element_by_id('answer')
    ansver_field.send_keys(calc(sheets_attribute))

    check_robot = browser.find_element_by_id('robotCheckbox')
    check_robot.click()

    radio_button_robots = browser.find_element_by_id('robotsRule')
    radio_button_robots.click()

    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

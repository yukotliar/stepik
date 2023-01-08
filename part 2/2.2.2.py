from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    answer_element.send_keys(y)
    checkbox_element = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_element.click()
    radio_element = browser.find_element(By.ID, 'robotsRule')
    radio_element.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
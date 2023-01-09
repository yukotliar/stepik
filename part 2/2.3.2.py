from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    answer_element.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
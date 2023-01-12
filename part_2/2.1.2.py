from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    answer_element = browser.find_element(By.ID, 'answer')
    answer_element.send_keys(y)
    checkbox_element = browser.find_element(By.ID, 'robotCheckbox')
    checkbox_element.click()
    radio_element = browser.find_element(By.ID, 'robotsRule')
    radio_element.click()
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
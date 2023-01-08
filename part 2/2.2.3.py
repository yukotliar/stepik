from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys("Yurii")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input2.send_keys("Kotliar")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input3.send_keys("test@gmail.com")
    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_text.txt')
    file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
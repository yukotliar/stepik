from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, 'num1')
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = num2_element.text
    value = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(value))
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
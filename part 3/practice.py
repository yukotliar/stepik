from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys("Yurii")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Kotliar")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("test@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text isn't equal")

    def test_reg2(self):
        link1 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input1.send_keys("Yurii")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Kotliar")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("test@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text isn't equal")

if __name__ == "__main__":
    unittest.main()
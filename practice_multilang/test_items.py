import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_present(browser):
    browser.get(link)
    basket_button = browser.find_element(By.XPATH, "//button[contains(@class, 'btn-add-to-basked')]")
    time.sleep(5)
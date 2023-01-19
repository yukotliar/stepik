import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button_present(browser):
    browser.get(link)
    time.sleep(5)
    basket_button = browser.find_elements(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert len(basket_button) > 0, "Basket button isn't found"
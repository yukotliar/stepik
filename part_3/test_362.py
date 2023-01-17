import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

answer = int(math.log(int(time.time())))

links = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('link', links)
def test_parametrize(browser, link):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("login")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("password")
    submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit.click()
    pop_up = WebDriverWait(browser,5).until(
        EC.invisibility_of_element_located((By.ID, "ember84"))
    )
    text_field = browser.find_element(By.ID, "ember99")
    text_field.send_keys(answer)




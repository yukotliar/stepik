import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def answer():
    return str(math.log(int(time.time())))

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
    button_login = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button_login.click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("jacksinnerconflict@gmail.com")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("Zxc35711522")
    button_submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button_submit.click()
    pop_up = WebDriverWait(browser,3).until(
        EC.invisibility_of_element_located((By.ID, "ember84"))
    )
    text_field = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember-text-area"))
    )
    text_field.send_keys(answer())
    browser.implicitly_wait(5)
    button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
    button_send.click()
    hint = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    hint_text = hint.text
    assert hint_text == "Correct!", f"expected 'Correct!', got '{hint_text}"


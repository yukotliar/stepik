
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://stepik.org/lesson/236895/step/1"

def test_login(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
    )
    button.click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("jacksinnerconflict@gmail.com")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("Zxc35711522")
    submit = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    submit.click()
    pop_up = WebDriverWait(browser,5).until(
        EC.invisibility_of_element_located((By.ID, "ember84"))
    )
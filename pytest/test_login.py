from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os
import pytest

instance_url = "https://testhomer18.infocyte.com"
super_password = os.environ.get('HUNT_PASSWORD')
test_user = "homer.camacho3@gmail.com"

def test_app_login():
    # new instance of firefox webdriver
    pytest.driver.get(instance_url)

    # wait for element to be present with 30 sec timeout
    el = WebDriverWait(pytest.driver, 30).until(
        EC.presence_of_element_located((By.ID, "email"))
        )

    time.sleep(5)

    #fill in login form, then click submit
    pytest.driver.find_element(By.ID, "email").send_keys(test_user)
    pytest.driver.find_element(By.ID, "password").send_keys(super_password)
    pytest.driver.find_element(By.ID, "btn-login").click()

    time.sleep(30)

    #display current url post login. should always be dashboard
    expected_land_page = f"{instance_url}/dashboard"
    current_url = pytest.driver.current_url
    logging.info(current_url)
    
    assert current_url == expected_land_page, \
        f"Unexpected landing page url {current_url} post login"
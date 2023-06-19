#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import pytest
import time
import os
import logging
from selenium import webdriver

pytest.base_url = os.environ.get('HUNT_URL')
pytest.logged_in = False
pytest.chrome_driver = webdriver.Chrome()

@pytest.fixture(scope="module", autouse=True)
def setup_webdriver():
    logging.info(f"chrome driver initiated.\nOpening web url {pytest.base_url}")
    pytest.chrome_driver.get(pytest.base_url)
    time.sleep(10)
    email_user = pytest.chrome_driver.find_element('id' , 'form_username')
    logging.info(f"Username: {os.environ.get('USER_EMAIL')}")
    email_user.send_keys(os.environ.get('USER_EMAIL'))
    continue_button = pytest.chrome_driver.find_element('id', 'form_submit')
    continue_button.click()
    time.sleep(2)
    password_user = pytest.chrome_driver.find_element('id', 'form_password')
    password_user.send_keys(os.environ.get('HUNT_PASSWORD'))
    continue_button = pytest.chrome_driver.find_element('id', 'form_submit')
    continue_button.click()
    time.sleep(10)

    yield

    logging.info("closing web browser session")
    pytest.chrome_driver.close()
    
@pytest.fixture(scope="module")
def new_webdriver():
    driver = webdriver.Chrome()

    yield driver

    driver.close()

'''
@pytest.fixture
def instance_login_auth0():
    """legacy auth0 login

    going away with datto authweb push 
    """
    pytest.chrome_driver.get(os.environ.get('HUNT_URL'))
    time.sleep(10)
    email_user = pytest.chrome_driver.find_element('id' , 'email')
    email_user.send_keys(os.environ.get('USER_EMAIL'))
    password_user = pytest.chrome_driver.find_element('id', 'password')
    password_user.send_keys(os.environ.get('HUNT_PASSWORD'))
    login_button = pytest.chrome_driver.find_element('id', 'btn-login')
    login_button.click()
    pytest.logged_in = True
    time.sleep(10)

@pytest.fixture(scope="session")
def instance_login_authweb():
    """Big K authweb hotness
    """
    pytest.chrome_driver.get(os.environ.get('HUNT_URL'))
    time.sleep(10)
    email_user = pytest.chrome_driver.find_element('id' , 'form_username')
    email_user.send_keys(os.environ.get('USER_EMAIL'))
    continue_button = pytest.chrome_driver.find_element('id', 'form_submit')
    continue_button.click()
    time.sleep(2)
    password_user = pytest.chrome_driver.find_element('id', 'password')
    password_user.send_keys(os.environ.get('HUNT_PASSWORD'))
    login_button = pytest.chrome_driver.find_element('id', 'btn-login')
    login_button.click()
    pytest.logged_in = True
    time.sleep(10)

@pytest.fixture
def driver_find_element():
    def __loader(xpath):
        logging.info(f"finding element {xpath}")
        ui_element = pytest.chrome_driver.find_element('xpath', xpath)
        return ui_element
    return __loader

@pytest.fixture
def driver_click_element():
    def __loader(ui_element):
        logging.info("clicking element")
        ui_element.click()
        logging.info(f"current URL after click {pytest.chrome_driver.current_url}")
    return __loader
    '''
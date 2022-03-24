import pytest
import json
import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytest.web_driver = None
pytest.instance_url = os.environ.get('HUNT_URL')

@pytest.fixture(scope="session", autouse=True)
def new_session():
    logging.info("Starting new firefox webdriver session")
    pytest.driver = webdriver.Firefox()

    yield

    logging.info("Destroying webdriver session")
    pytest.driver.close()


@pytest.fixture
def wait_for_element_by_id():
    def __loader(elem_id):
        # wait for element to be present with 30 sec timeout
        logging.info(f"waiting for element {elem_id} to be displayed")
        el = WebDriverWait(pytest.driver, 30).until(
            EC.presence_of_element_located((By.ID, elem_id))
            )

    return __loader

@pytest.fixture
def login_ui():
    login_url = pytest.instance_url
    logging.info(f"accessing {login_url}")
    pytest.driver.get(login_url)
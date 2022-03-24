import pytest
import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytest.web_driver = None

@pytest.fixture(scope="session", autouse=True)
def new_session():
    pytest.driver = webdriver.Firefox()

    yield

    pytest.driver.close()

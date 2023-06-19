#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import pytest
import logging
from common.UI_elements.dashboard import DashboardPage

dashboard = DashboardPage(pytest.chrome_driver)

@pytest.fixture
def click_dash_topnav():
    dashboard.click_top_nav()

def test_new_alerts(click_dash_topnav):
    click_dash_topnav
    dashboard.click_new_alerts()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_new_hosts(click_dash_topnav):
    click_dash_topnav
    dashboard.click_new_hosts()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_new_admins(click_dash_topnav):
    click_dash_topnav
    dashboard.click_new_admins()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_new_applications(click_dash_topnav):
    click_dash_topnav
    dashboard.click_new_applications()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_threat_compromised_hosts(click_dash_topnav):
    click_dash_topnav
    dashboard.click_threat_compromised_hosts()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_threat_malicious_files(click_dash_topnav):
    click_dash_topnav
    dashboard.click_threat_malicious_files()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_threat_memory_injections(click_dash_topnav):
    click_dash_topnav
    dashboard.click_threat_memory_injections()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_threat_compromised_accounts(click_dash_topnav):
    click_dash_topnav
    dashboard.click_threat_compromised_accounts()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_vulns_risks_applications(click_dash_topnav):
    click_dash_topnav
    dashboard.click_vulns_risks_applications
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")
    
def test_vulns_risks_vulnerable_applications(click_dash_topnav):
    click_dash_topnav
    dashboard.click_vulns_risks_vulnerable_applications
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")

def test_vulns_risks_admin_accounts(click_dash_topnav):
    click_dash_topnav
    dashboard.click_vulns_risks_admin_accounts()
    time.sleep(2)
    logging.info(f"{pytest.chrome_driver.current_url}")
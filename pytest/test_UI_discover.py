#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pytest
from common.UI_elements.discover import DiscoverPage
import logging
import random

discover = DiscoverPage(pytest.chrome_driver)


@pytest.fixture
def click_discover_topnav():
    discover.click_top_nav()

@pytest.fixture
def create_new_target_group(click_discover_topnav):
    def __loader__(target_group_name):
        click_discover_topnav
        logging.info(f"Creating new target group: {target_group_name}")
        discover.click_add_target_group()
        discover.enter_target_group_name("test tg")
        discover.select_controller_group()
        discover.click_tg_save_button()

    return __loader__


def test_create_and_delete_target_group(click_discover_topnav, create_new_target_group):
    #navigate to discover tab after initial logina
    create_new_target_group(f"test_tg_{random.randint(0, 9999)}")
    discover.click_tg_action_menu_delete()
    logging.info(pytest.chrome_driver.current_url)
    assert pytest.chrome_driver.current_url == f"{pytest.base_url}/discover/target-group/list", \
            f"unexpected url after target group delete: {pytest.chrome_driver.current_url}"

def test_create_and_delete_query(create_new_target_group):
    create_new_target_group(f"test_tg_{random.randint(0, 9999)}")
    discover.click_target_group_query_tab()
    pass
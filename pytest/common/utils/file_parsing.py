#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import logging

def read_json_file(json_path):
    data_path = json_path
    with open(data_path) as i:
        json_data = json.load(i)
        logging.info(f"test data loaded from json file {data_path}")
        return json_data
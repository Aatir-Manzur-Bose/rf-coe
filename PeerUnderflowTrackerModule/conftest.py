#!/usr/bin/python
# -*- coding  utf-8 -*-
"""
Organization   BOSE CORPORATION
Copyright      COPYRIGHT 2020 BOSE CORPORATION ALL RIGHTS RESERVED.
               This program may not be reproduced, in whole or in part in any
               form or any means whatsoever without the written permission of
                   BOSE CORPORATION
                   The Mountain,
                   Framingham, MA 01701-9168
"""
from datetime import datetime
from WearableTestUtils.LoggerUtils.wearable_logger import logger
import pytest
import os
import sys
sys.path.insert(0, os.getcwd())
#from Tests.gen_spitfire_config import gen_spitfire_config

if os.environ.get('GENERATE_CONFIG', False) and os.environ['GENERATE_CONFIG'] == "True":
    logger.info("Generate spitfire config file...")
    gen_spitfire_config(config_file="config_template.toml")
    
pytest_plugins = (
    "pytester",
    "WearableTestUtils.ScriptUtils.pytest_plugins.session_fixture",
    "WearableTestUtils.ScriptUtils.pytest_plugins.function_fixture",
    "WearableTestUtils.DutUtils.pytest_plugins.dut_plugin",
    "WearableTestUtils.SpitfireMessagingUtils.pytest_plugins.messaging_plugin",
    "WearableTestUtils.SpitfireCommandUtils.pytest_plugins.spitfire_command_plugin",
    "BluetoothTestUtils.pytest_plugins.conftest_plugin"
)

def pytest_addoption(parser):
    """
    Add any custom options for these tests.
    """
    parser.addoption("--cmd_args", action="store", default="",
                     help="Enter the command line arguments. You need to use the inp_args fixture to extract cmd line args")
    parser.addoption("--stlink", action="store", default="",
                     help="Enter the command line arguments. You need to use the stlink fixture to extract cmd line args")
    parser.addoption("--topology",action="store",default="pair",
                     help="Enter the command line arguments. You need to use the profile fixture to extract cmd line args")

@pytest.fixture()
def inp_args(pytestconfig):
    ret_val = pytestconfig.getoption("cmd_args")
    return ret_val


@pytest.fixture()
def stlink(pytestconfig):
    ret_val = pytestconfig.getoption("stlink")
    return ret_val

@pytest.fixture(autouse=True, scope="function")
def time_info():
    """
    Date/time processing.
    """
    start_time = datetime.now()
    now = start_time.strftime("%d/%m/%Y %H:%M:%S")
    print("\n")
    print_str = "="*20 + "Starting Test @ "+ str(now) + "="*20
    print(print_str)
    yield
    end_time = datetime.now()
    total_time = end_time - start_time
    now = end_time.strftime("%d/%m/%Y %H:%M:%S")
    print("\n")
    print_str = "="*20 + "Ending Test @ " + str(now) + f"Total time = {total_time}" + "="*20
    print(print_str)

@pytest.fixture(scope="function")
def connect_buds(messaging_list):
    helper.verify_buds_connected(messaging_list)

@pytest.fixture()
def topology_args(pytestconfig):
    retval = pytestconfig.getoption("topology")
    return retval
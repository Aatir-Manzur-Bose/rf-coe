#!/usr/bin/python
# -*- coding  utf-8 -*-
#
#  Organization   BOSE CORPORATION
#  Copyright      COPYRIGHT 2021 BOSE CORPORATION ALL RIGHTS RESERVED.
#                 This program may not be reproduced, in whole or in part in any
#                 form or any means whatsoever without the written permission of
#                     BOSE CORPORATION
#                     The Mountain,
#                     Framingham, MA 01701-9168
"""
Listens for peer underflow event from both connected buds and panics them simultaneously 
"""

#We use dynamic loading of protobuf modules so need to import in function scope.
#pylint: disable=locally-disabled, import-outside-toplevel, invalid-name
#pylint: disable=redefined-outer-name, pointless-string-statement, broad-except

# ================================================================================================================================
# Before running the test, need to create python virtual environment using below command
# python3.8 -m venv venv && venv\Scripts\activate && python -m pip install --upgrade pip && pip install -Ur requirements.txt
# ================================================================================================================================
# To run the independent python file, use below command
# pytest test_peerUnderflowTracker.py::test_track_peer_underflow --dut-over-usb --pbdir=.
# ================================================================================================================================

import time
import threading

from pypolycomm.core import DeviceMessageType
from WearableTestUtils.LoggerUtils.wearable_logger import logger
from WearableTestUtils.SpitfireMessagingUtils.pytest_plugins.messaging_plugin import messaging_list
from WearableTestUtils.SpitfireMessagingUtils.PbManager import PbManager
from WearableTestUtils.SpitfireMessagingUtils.SpitfireMessaging import SpitfireMessaging, FunctionSpec
from WearableTestUtils.DutUtils.command.tap_command import TapCommand
from WearableTestUtils.ScriptUtils.pytest_plugins.session_fixture import dut_list

""" Maximum time peer messages can build up. """
UNDERFLOW_PANIC_TIMEOUT = 3000 # milliseconds



class TestData:
    """
    Stored event data.
    """
    def __init__(self):
        """
        Initializer
        """
        """ Used to block until a response is received """
        self.threading_event = threading.Event()
        """ Store any incoming message header for later use """
        self.msg_header = None
        """ Store any incoming message payload for later use """
        self.msg_payload = None

def role_response_callback( header, payload, test_data ):
    """
    Function invoked when response is received.
    :param header: The Spitfire messaging header object
    :param payload: The response message payload object
    :param test_data: Array to hold event payload data
    """
    test_data.msg_header = header
    test_data.msg_payload = payload
    test_data.threading_event.set()

def send_request_and_validate( messaging, request_id, payload ):
    """
    Common function to send request with appropriate request id
    """
    test_data = TestData()
    try:
        function_spec = FunctionSpec( role_response_callback, test_data )
        messaging.send_request( "cor", request_id, payload, function_spec )

        # Validate response event set or not
        test_data.threading_event.wait( 5 )

        # Validate response msg header and payload should not be None 
        if test_data.msg_header is None or test_data.msg_payload is None:
            assert False, f"Error: No response recieved"

        return test_data.msg_payload
    except Exception as error:
        logger.error(error)
        assert False

def peer_underflow_event_callback(header, payload, test_data):
    """
    Function invoked when an incoming event is received.
    :param header: The Spitfire messaging header object
    :param payload: The response message payload object
    :param test_data: Array to hold event payload data
    """
    test_data.msg_payload = header
    test_data.msg_payload = payload
    test_data.threading_event.set()

def handover_changed_event_callback(header, payload, test_data):
    """
    Function invoked when an incoming event is received.
    :param header: The Spitfire messaging header object
    :param payload: The response message payload object
    :param test_data: Array to hold event payload data
    """
    test_data.msg_payload = header
    test_data.msg_payload = payload
    test_data.threading_event.set()

def register_event(messaging: SpitfireMessaging, event_id, event_data):
    """
    Register to peer underflow event.
    :param messaging: SpitfireMessaging object from fixture
    :param event_id: Event type to register to
    :param event_data: Class to hold event payload and header data
    """

    function_spec = FunctionSpec( peer_underflow_event_callback, event_data )
    messaging.register_event( "cor", event_id, function_spec )

def unregister_event(messaging, event_id):
    """
    Unregister to the udnerflow event.
    :param messaging: SpitfireMessaging object from fixture
    :param event_id: Event type to unregister
    """
    messaging.unregister_event( "cor", event_id )

def track_peer_underflow(messaging_list, underflowTimeout):
    """
    loop to check for peer underflow events
    :param messaging_list: list of SpitfireMessaging objects from fixture
    :param underflowTimeout: time in ms the underflow timeout is set to
    """
    # pylint: disable=import-error, unused-import
    import core_api_pb2

    primary_dut = None
    secondary_dut = None

    for msgdev in messaging_list:
        logger.info("Current DUT device is: %s", msgdev.get_device())
        # Send request with payload to identify which dut is primary and which is secondary
        dut_payload = None
        payload = core_api_pb2.core_bt_get_role_request_t()

        dut_payload = send_request_and_validate( msgdev, core_api_pb2.COR_BT_GET_ROLE, payload )
        
        logger.info("Current DUT device [ %s ] role is: [ %d ]\n", msgdev.get_device(), dut_payload.role )

        if dut_payload.role == core_api_pb2.core_bt_role_t.core_bt_role_primary:
            primary_dut = msgdev
            logger.info("PRIMARY device is: %s", primary_dut.get_device())            
        elif dut_payload.role == core_api_pb2.core_bt_role_t.core_bt_role_secondary:
            secondary_dut = msgdev
            logger.info("SECONDARY device is: %s", secondary_dut.get_device())

    logger.info("Starting peer underflow tracker")

    # Underflow event data
    primary_event_data = TestData()
    secondary_event_data = TestData()

    # Get role request data
    role_data = TestData()

    # Keep a time count of the total underflow delay
    primary_time = 0
    secondary_time = 0

    # Register for role changed events
    register_event(primary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_HANDOVER_CHANGED, role_data)

    # Register to the peer underflow event on both buds
    register_event(primary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_P2P_TRANSMIT_UNDERFLOW, primary_event_data)
    register_event(secondary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_P2P_TRANSMIT_UNDERFLOW, secondary_event_data )

    while True:
        # Check Primary dut for a new event
        if primary_event_data.threading_event.is_set():
            primary_time = primary_event_data.msg_payload.underflow_count * underflowTimeout
            primary_event_data.threading_event.clear() 
        # Check Secondary dut for a new event
        if secondary_event_data.threading_event.is_set():
            secondary_time = secondary_event_data.msg_payload.underflow_count * underflowTimeout
            secondary_event_data.threading_event.clear()
        # Send Panics commands to both buds if either hits the timeout
        if (primary_time >= UNDERFLOW_PANIC_TIMEOUT) or (secondary_time >= UNDERFLOW_PANIC_TIMEOUT):
                TAP_COMMAND = "cor.cra panic p1"
                logger.info("Panic")
                logger.info("Maximum underflow reached: panicking both buds!")
                primary_dut.get_device().send(DeviceMessageType.TAP, TAP_COMMAND)
                secondary_dut.get_device().send(DeviceMessageType.TAP, TAP_COMMAND)
                break

        # Sleep for half of timeout panic time converted to seconds (timeout/(2*1000))
        time.sleep(underflowTimeout/2000.0)

    #unregister the underflow events, we have what we need
    unregister_event( primary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_P2P_TRANSMIT_UNDERFLOW )
    unregister_event( secondary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_P2P_TRANSMIT_UNDERFLOW )
    unregister_event( primary_dut, core_api_pb2.core_event_ids_t.CORE_EVENT_HANDOVER_CHANGED)

def test_track_peer_underflow(messaging_list):
    underflowTimeout = 500.0
    track_peer_underflow(messaging_list, underflowTimeout)

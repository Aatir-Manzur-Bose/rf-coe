#    obj/CodeGenerator/Python/Debug/Faults.py
#    Created 27/07/2023 at 10:10:11 from:
#        Messages = messages/Debug/Faults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_Faults_Get :
    ID = 32865
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 6), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (6, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_Faults_Get.MSG_OFFSET + Debug_Faults_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_Faults_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_Faults_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_Faults_Get.MSG_OFFSET + Debug_Faults_Get.SIZE)
        else:
            try:
                messageBuffer.raw
            except AttributeError:
                newbuf = ctypes.create_string_buffer(len(messageBuffer))
                for i in range(0, len(messageBuffer)):
                    newbuf[i] = bytes(messageBuffer)[i]
                messageBuffer = newbuf
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        self.msg_buffer_wrapper = { "msg_buffer": messageBuffer }

        self.hdr = Messaging.hdr(messageBuffer)
        if doInit:
            self.hdr.SetMessageID(Debug_Faults_Get.ID)
            self.hdr.SetDataLength(Debug_Faults_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.Faults.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.Faults.Get", Debug_Faults_Get.ID, Debug_Faults_Get)
#    obj/CodeGenerator/Python/Debug/Faults.py
#    Created 27/07/2023 at 10:10:11 from:
#        Messages = messages/Debug/Faults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_Faults_SetGet :
    ID = 32866
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    FaultID = OrderedDict([("FAULT_NO_FAULT", 0), ("FAULT_USER_REQUEST_INTERRUPT", 1), ("FAULT_AUTOMATIC_INTERRUPT", 2), ("FAULT_BATTERY_VOLTAGE_HIGH", 3), ("FAULT_BATTERY_VOLTAGE_CRITICALLY_HIGH", 4), ("FAULT_BATTERY_EXIT_SHIPMODE_TIMEOUT", 5), ("FAULT_BATTERY_SHIPMODE", 6), ("FAULT_BATTERY_VOLTAGE_LOW", 7), ("FAULT_BATTERY_VOLTAGE_CRITICALLY_LOW", 8), ("FAULT_VOLTAGE_FAULT_REQ_RETURN", 9), ("FAULT_CHARGER_FAULT_REQ_RETURN", 10), ("FAULT_TEMPERATURE_FAULT_REQ_RETURN", 11), ("FAULT_VOLTAGE_REQ_RETURN", 12), ("FAULT_TEMPERATURE_REQ_RETURN", 13), ("FAULT_CHARGER_STATUS_REQ_RETURN", 14), ("FAULT_VOLTAGE_FULL_REQ_RETURN", 15), ("FAULT_CHARGER_CURRENT_REQ_RETURN", 16), ("FAULT_CHARGER_SUSPENDED", 17), ("FAULT_CHARGER_OPERATION_WHILE_CHARGING", 18), ("FAULT_CHARGER_OVER_VOLTAGE", 19), ("FAULT_CHARGER_UNDER_VOLTAGE", 20), ("FAULT_UPDATE_BATTERY_LOW", 21), ("FAULT_UPDATE_FAILED", 22), ("FAULT_TEMPERATURE_BRICK_LOW", 23), ("FAULT_TEMPERATURE_CRITICAL_LOW", 24), ("FAULT_TEMPERATURE_LOW", 25), ("FAULT_TEMPERATURE_HIGH", 26), ("FAULT_TEMPERATURE_CRITICAL_HIGH", 27), ("FAULT_TEMPERATURE_BRICK_HIGH", 28), ("FAULT_BATTERY_NOT_PRESENT", 29), ("FAULT_CHARGER_CONFIGURED_WRONG", 30), ("FAULT_SENSOR_HUB_FW_DOWNLOAD_FAILURE", 31), ("FAULT_CAPTOUCH_FW_DOWNLOAD_FAILURE", 32), ("FAULT_FUEL_GAUGE_STUCK", 33), ("FAULT_FUEL_GAUGE_VOLATILE_DATA_FAILURE", 34), ("FAULT_VOLTAGE_BRICK_LOW", 35), ("FAULT_BATTERY_VOLTAGE_VERY_LOW", 36), ("FAULT_BATTERY_SOC_TIME_BELOW_5MIN", 37), ("FAULT_BATTERY_SOC_TIME_BELOW_15MIN", 38), ("FAULT_FATAL", 39), ("FAULT_BATTERY_OVER_TEMPERATURE", 40), ("FAULT_BATTERY_UNDER_TEMPERATURE", 41), ("FAULT_WAKE_FAILURE", 42), ("FAULT_FUEL_GAUGE_WATCHDOG", 43), ("FAULT_CC_TIMER", 44), ("FAULT_AMPLIFIER", 45), ("FAULT_PRECHARGE_TIMEOUT", 46), ("FAULT_BATTERY_EXTREME_OVER_TEMPERATURE", 47), ("FAULT_TEMPERATURE_MISMATCH", 48)])
    ReverseFaultID = OrderedDict([(0, "FAULT_NO_FAULT"), (1, "FAULT_USER_REQUEST_INTERRUPT"), (2, "FAULT_AUTOMATIC_INTERRUPT"), (3, "FAULT_BATTERY_VOLTAGE_HIGH"), (4, "FAULT_BATTERY_VOLTAGE_CRITICALLY_HIGH"), (5, "FAULT_BATTERY_EXIT_SHIPMODE_TIMEOUT"), (6, "FAULT_BATTERY_SHIPMODE"), (7, "FAULT_BATTERY_VOLTAGE_LOW"), (8, "FAULT_BATTERY_VOLTAGE_CRITICALLY_LOW"), (9, "FAULT_VOLTAGE_FAULT_REQ_RETURN"), (10, "FAULT_CHARGER_FAULT_REQ_RETURN"), (11, "FAULT_TEMPERATURE_FAULT_REQ_RETURN"), (12, "FAULT_VOLTAGE_REQ_RETURN"), (13, "FAULT_TEMPERATURE_REQ_RETURN"), (14, "FAULT_CHARGER_STATUS_REQ_RETURN"), (15, "FAULT_VOLTAGE_FULL_REQ_RETURN"), (16, "FAULT_CHARGER_CURRENT_REQ_RETURN"), (17, "FAULT_CHARGER_SUSPENDED"), (18, "FAULT_CHARGER_OPERATION_WHILE_CHARGING"), (19, "FAULT_CHARGER_OVER_VOLTAGE"), (20, "FAULT_CHARGER_UNDER_VOLTAGE"), (21, "FAULT_UPDATE_BATTERY_LOW"), (22, "FAULT_UPDATE_FAILED"), (23, "FAULT_TEMPERATURE_BRICK_LOW"), (24, "FAULT_TEMPERATURE_CRITICAL_LOW"), (25, "FAULT_TEMPERATURE_LOW"), (26, "FAULT_TEMPERATURE_HIGH"), (27, "FAULT_TEMPERATURE_CRITICAL_HIGH"), (28, "FAULT_TEMPERATURE_BRICK_HIGH"), (29, "FAULT_BATTERY_NOT_PRESENT"), (30, "FAULT_CHARGER_CONFIGURED_WRONG"), (31, "FAULT_SENSOR_HUB_FW_DOWNLOAD_FAILURE"), (32, "FAULT_CAPTOUCH_FW_DOWNLOAD_FAILURE"), (33, "FAULT_FUEL_GAUGE_STUCK"), (34, "FAULT_FUEL_GAUGE_VOLATILE_DATA_FAILURE"), (35, "FAULT_VOLTAGE_BRICK_LOW"), (36, "FAULT_BATTERY_VOLTAGE_VERY_LOW"), (37, "FAULT_BATTERY_SOC_TIME_BELOW_5MIN"), (38, "FAULT_BATTERY_SOC_TIME_BELOW_15MIN"), (39, "FAULT_FATAL"), (40, "FAULT_BATTERY_OVER_TEMPERATURE"), (41, "FAULT_BATTERY_UNDER_TEMPERATURE"), (42, "FAULT_WAKE_FAILURE"), (43, "FAULT_FUEL_GAUGE_WATCHDOG"), (44, "FAULT_CC_TIMER"), (45, "FAULT_AMPLIFIER"), (46, "FAULT_PRECHARGE_TIMEOUT"), (47, "FAULT_BATTERY_EXTREME_OVER_TEMPERATURE"), (48, "FAULT_TEMPERATURE_MISMATCH")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 6), ("Operator", 2)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (6, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_Faults_SetGet.MSG_OFFSET + Debug_Faults_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_Faults_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_Faults_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_Faults_SetGet.MSG_OFFSET + Debug_Faults_SetGet.SIZE)
        else:
            try:
                messageBuffer.raw
            except AttributeError:
                newbuf = ctypes.create_string_buffer(len(messageBuffer))
                for i in range(0, len(messageBuffer)):
                    newbuf[i] = bytes(messageBuffer)[i]
                messageBuffer = newbuf
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        self.msg_buffer_wrapper = { "msg_buffer": messageBuffer }

        self.hdr = Messaging.hdr(messageBuffer)
        if doInit:
            self.hdr.SetMessageID(Debug_Faults_SetGet.ID)
            self.hdr.SetDataLength(Debug_Faults_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.Faults.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFault(self, enumAsInt=0):
        """ID of fault you wish to set/clear"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_Faults_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_Faults_SetGet.ReverseFaultID.get(value, value)
        return value
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def Getvalue(self):
        """1 = set, 0 = clear"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_Faults_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFault(self, value):
        """ID of fault you wish to set/clear"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_Faults_SetGet.FaultID.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_Faults_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def Setvalue(self, value):
        """1 = set, 0 = clear"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_Faults_SetGet.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Fault",type="enumeration",units="",minVal="0",maxVal="255",description="ID of fault you wish to set/clear",get=GetFault,set=SetFault,count=1, bitfieldInfo = [], enum = [FaultID, ReverseFaultID]),\
        FieldInfo(name="value",type="int",units="Boolean",minVal="0",maxVal="255",description="1 = set, 0 = clear",get=Getvalue,set=Setvalue,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.Faults.SetGet", Debug_Faults_SetGet.ID, Debug_Faults_SetGet)
#    obj/CodeGenerator/Python/Debug/Faults.py
#    Created 27/07/2023 at 10:10:11 from:
#        Messages = messages/Debug/Faults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_Faults_Status :
    ID = 32867
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 6), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (6, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_Faults_Status.MSG_OFFSET + Debug_Faults_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_Faults_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_Faults_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_Faults_Status.MSG_OFFSET + Debug_Faults_Status.SIZE)
        else:
            try:
                messageBuffer.raw
            except AttributeError:
                newbuf = ctypes.create_string_buffer(len(messageBuffer))
                for i in range(0, len(messageBuffer)):
                    newbuf[i] = bytes(messageBuffer)[i]
                messageBuffer = newbuf
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        self.msg_buffer_wrapper = { "msg_buffer": messageBuffer }

        self.hdr = Messaging.hdr(messageBuffer)
        if doInit:
            self.hdr.SetMessageID(Debug_Faults_Status.ID)
            self.hdr.SetDataLength(Debug_Faults_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.Faults.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetActiveFaults(self):
        """Array of fault IDs, one for each fault in the system that is set"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_Faults_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetActiveFaults(self, value):
        """Array of fault IDs, one for each fault in the system that is set"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_Faults_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ActiveFaults",type="int",units="",minVal="0",maxVal="255",description="Array of fault IDs, one for each fault in the system that is set",get=GetActiveFaults,set=SetActiveFaults,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.Faults.Status", Debug_Faults_Status.ID, Debug_Faults_Status)

#    obj/CodeGenerator/Python/BatteryDebug/DriverFaults.py
#    Created 27/07/2023 at 10:09:49 from:
#        Messages = messages/BatteryDebug/DriverFaults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_DriverFaults_Get :
    ID = 102737
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 21), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (21, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_Get.MSG_OFFSET + BatteryDebug_DriverFaults_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_DriverFaults_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_DriverFaults_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_Get.MSG_OFFSET + BatteryDebug_DriverFaults_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_DriverFaults_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_DriverFaults_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.DriverFaults.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.DriverFaults.Get", BatteryDebug_DriverFaults_Get.ID, BatteryDebug_DriverFaults_Get)
#    obj/CodeGenerator/Python/BatteryDebug/DriverFaults.py
#    Created 27/07/2023 at 10:09:49 from:
#        Messages = messages/BatteryDebug/DriverFaults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_DriverFaults_SetGet :
    ID = 102738
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    DriverFault = OrderedDict([("None", 0), ("OverVoltage", 1), ("UnderVoltage", 2), ("SuspendedBatteryVoltage", 3), ("InvalidVoltage", 4), ("InvalidCurrent", 5), ("Suspended", 6), ("Unknown", 7), ("NtcHotThreshold", 8), ("NtcColdThreshold", 9), ("BatteryOverVoltage", 10), ("ChargerInputFault", 11), ("ChargerThermalShutdown", 12), ("ChargerTimeExpire", 13), ("OTGFault", 14), ("ChargeWatchdogFault", 15)])
    ReverseDriverFault = OrderedDict([(0, "None"), (1, "OverVoltage"), (2, "UnderVoltage"), (3, "SuspendedBatteryVoltage"), (4, "InvalidVoltage"), (5, "InvalidCurrent"), (6, "Suspended"), (7, "Unknown"), (8, "NtcHotThreshold"), (9, "NtcColdThreshold"), (10, "BatteryOverVoltage"), (11, "ChargerInputFault"), (12, "ChargerThermalShutdown"), (13, "ChargerTimeExpire"), (14, "OTGFault"), (15, "ChargeWatchdogFault")])
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 21), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (21, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_SetGet.MSG_OFFSET + BatteryDebug_DriverFaults_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_DriverFaults_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_DriverFaults_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_SetGet.MSG_OFFSET + BatteryDebug_DriverFaults_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_DriverFaults_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_DriverFaults_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.DriverFaults.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetDriverFault(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_DriverFaults_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = BatteryDebug_DriverFaults_SetGet.ReverseDriverFault.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetDriverFault(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = BatteryDebug_DriverFaults_SetGet.DriverFault.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_DriverFaults_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="DriverFault",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetDriverFault,set=SetDriverFault,count=1, bitfieldInfo = [], enum = [DriverFault, ReverseDriverFault])\
    ]

Messaging.Register("BatteryDebug.DriverFaults.SetGet", BatteryDebug_DriverFaults_SetGet.ID, BatteryDebug_DriverFaults_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/DriverFaults.py
#    Created 27/07/2023 at 10:09:49 from:
#        Messages = messages/BatteryDebug/DriverFaults.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_DriverFaults_Status :
    ID = 102739
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    DriverFault = OrderedDict([("None", 0), ("OverVoltage", 1), ("UnderVoltage", 2), ("SuspendedBatteryVoltage", 3), ("InvalidVoltage", 4), ("InvalidCurrent", 5), ("Suspended", 6), ("Unknown", 7), ("NtcHotThreshold", 8), ("NtcColdThreshold", 9), ("BatteryOverVoltage", 10), ("ChargerInputFault", 11), ("ChargerThermalShutdown", 12), ("ChargerTimeExpire", 13), ("OTGFault", 14), ("ChargeWatchdogFault", 15)])
    ReverseDriverFault = OrderedDict([(0, "None"), (1, "OverVoltage"), (2, "UnderVoltage"), (3, "SuspendedBatteryVoltage"), (4, "InvalidVoltage"), (5, "InvalidCurrent"), (6, "Suspended"), (7, "Unknown"), (8, "NtcHotThreshold"), (9, "NtcColdThreshold"), (10, "BatteryOverVoltage"), (11, "ChargerInputFault"), (12, "ChargerThermalShutdown"), (13, "ChargerTimeExpire"), (14, "OTGFault"), (15, "ChargeWatchdogFault")])
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 21), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (21, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_Status.MSG_OFFSET + BatteryDebug_DriverFaults_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_DriverFaults_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_DriverFaults_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_DriverFaults_Status.MSG_OFFSET + BatteryDebug_DriverFaults_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_DriverFaults_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_DriverFaults_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.DriverFaults.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetDriverFault(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_DriverFaults_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = BatteryDebug_DriverFaults_Status.ReverseDriverFault.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetDriverFault(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = BatteryDebug_DriverFaults_Status.DriverFault.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_DriverFaults_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="DriverFault",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetDriverFault,set=SetDriverFault,count=1, bitfieldInfo = [], enum = [DriverFault, ReverseDriverFault])\
    ]

Messaging.Register("BatteryDebug.DriverFaults.Status", BatteryDebug_DriverFaults_Status.ID, BatteryDebug_DriverFaults_Status)

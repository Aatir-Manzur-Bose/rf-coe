#    obj/CodeGenerator/Python/Debug/RSSI.py
#    Created 27/07/2023 at 10:10:15 from:
#        Messages = messages/Debug/RSSI.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RSSI_Get :
    ID = 32801
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 2), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (2, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RSSI_Get.MSG_OFFSET + Debug_RSSI_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RSSI_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RSSI_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RSSI_Get.MSG_OFFSET + Debug_RSSI_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_RSSI_Get.ID)
            self.hdr.SetDataLength(Debug_RSSI_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RSSI.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.RSSI.Get", Debug_RSSI_Get.ID, Debug_RSSI_Get)
#    obj/CodeGenerator/Python/Debug/RSSI.py
#    Created 27/07/2023 at 10:10:15 from:
#        Messages = messages/Debug/RSSI.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RSSI_SetGet :
    ID = 32802
    SIZE = 8
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 2), ("Operator", 2)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (2, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RSSI_SetGet.MSG_OFFSET + Debug_RSSI_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RSSI_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RSSI_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RSSI_SetGet.MSG_OFFSET + Debug_RSSI_SetGet.SIZE)
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
            self.hdr.SetMessageID(Debug_RSSI_SetGet.ID)
            self.hdr.SetDataLength(Debug_RSSI_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RSSI.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(6)
    def GetMacAddress(self, idx):
        """MAC Address of Source Device (chooses which radio link to query)"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_RSSI_SetGet.MSG_OFFSET + 0+idx*1)[0]
        return value
    
    @msg.units('ms')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def GetNotificationTimerInterval(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_RSSI_SetGet.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(6)
    def SetMacAddress(self, value, idx):
        """MAC Address of Source Device (chooses which radio link to query)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_RSSI_SetGet.MSG_OFFSET + 0+idx*1, tmp)
    
    @msg.units('ms')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def SetNotificationTimerInterval(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_RSSI_SetGet.MSG_OFFSET + 6, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="MacAddress",type="int",units="",minVal="0",maxVal="255",description="MAC Address of Source Device (chooses which radio link to query)",get=GetMacAddress,set=SetMacAddress,count=6, bitfieldInfo = [], enum = []),\
        FieldInfo(name="NotificationTimerInterval",type="int",units="ms",minVal="0",maxVal="65535",description="",get=GetNotificationTimerInterval,set=SetNotificationTimerInterval,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.RSSI.SetGet", Debug_RSSI_SetGet.ID, Debug_RSSI_SetGet)
#    obj/CodeGenerator/Python/Debug/RSSI.py
#    Created 27/07/2023 at 10:10:15 from:
#        Messages = messages/Debug/RSSI.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RSSI_Error :
    ID = 32804
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("FBlockNotSupported", 3), ("FunctionNotSupported", 4), ("OperatorNotSupported", 5), ("InvalidData", 6), ("DataNotAvailable", 7), ("RunTime", 8), ("Timeout", 9), ("InvalidState", 10), ("DeviceNotFound", 11), ("Busy", 12), ("UnableToConnectTimeout", 13), ("UnableToConnectSourceDeviceKeyMissing", 14), ("OTAFirmwareUpdateInProgress", 15), ("LowBatteryVoltage", 16), ("ChargerNotConnected", 17), ("UpdateNotAllowed", 18), ("UnknownPortNumber", 19), ("InsecureTransport", 20), ("InvalidOTPKey", 21), ("OutOfMemory", 22), ("CryptoProcessingError", 23), ("FeatureLocked", 24), ("FunctionBlockSpecificErrorCode", 255)])
    ReverseErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "FBlockNotSupported"), (4, "FunctionNotSupported"), (5, "OperatorNotSupported"), (6, "InvalidData"), (7, "DataNotAvailable"), (8, "RunTime"), (9, "Timeout"), (10, "InvalidState"), (11, "DeviceNotFound"), (12, "Busy"), (13, "UnableToConnectTimeout"), (14, "UnableToConnectSourceDeviceKeyMissing"), (15, "OTAFirmwareUpdateInProgress"), (16, "LowBatteryVoltage"), (17, "ChargerNotConnected"), (18, "UpdateNotAllowed"), (19, "UnknownPortNumber"), (20, "InsecureTransport"), (21, "InvalidOTPKey"), (22, "OutOfMemory"), (23, "CryptoProcessingError"), (24, "FeatureLocked"), (255, "FunctionBlockSpecificErrorCode")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 2), ("Operator", 4)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (2, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RSSI_Error.MSG_OFFSET + Debug_RSSI_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RSSI_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RSSI_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RSSI_Error.MSG_OFFSET + Debug_RSSI_Error.SIZE)
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
            self.hdr.SetMessageID(Debug_RSSI_Error.ID)
            self.hdr.SetDataLength(Debug_RSSI_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RSSI.Error"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetErrorCode(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_RSSI_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_RSSI_Error.ReverseErrorResponseCodes.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetErrorCode(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_RSSI_Error.ErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_RSSI_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [ErrorResponseCodes, ReverseErrorResponseCodes])\
    ]

Messaging.Register("Debug.RSSI.Error", Debug_RSSI_Error.ID, Debug_RSSI_Error)
#    obj/CodeGenerator/Python/Debug/RSSI.py
#    Created 27/07/2023 at 10:10:15 from:
#        Messages = messages/Debug/RSSI.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RSSI_Result :
    ID = 32806
    SIZE = 9
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 2), ("Operator", 6)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (2, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RSSI_Result.MSG_OFFSET + Debug_RSSI_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RSSI_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RSSI_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RSSI_Result.MSG_OFFSET + Debug_RSSI_Result.SIZE)
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
            self.hdr.SetMessageID(Debug_RSSI_Result.ID)
            self.hdr.SetDataLength(Debug_RSSI_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RSSI.Result"
    # Accessors
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetConnectionValidity(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('dB')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetConnectionRssi(self):
        """"""
        value = struct.unpack_from('b', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetSinkRssiValidity(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('dB')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def GetSinkRssi(self):
        """"""
        value = struct.unpack_from('>h', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('ms')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('5')
    @msg.size('4')
    @msg.count(1)
    def GetTimestamp(self):
        """"""
        value = struct.unpack_from('>L', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetConnectionValidity(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 0, tmp)
    
    @msg.units('dB')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetConnectionRssi(self, value):
        """"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 1, tmp)
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetSinkRssiValidity(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 2, tmp)
    
    @msg.units('dB')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def SetSinkRssi(self, value):
        """"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 3, tmp)
    
    @msg.units('ms')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('5')
    @msg.size('4')
    @msg.count(1)
    def SetTimestamp(self, value):
        """"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Debug_RSSI_Result.MSG_OFFSET + 5, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ConnectionValidity",type="int",units="Boolean",minVal="0",maxVal="255",description="",get=GetConnectionValidity,set=SetConnectionValidity,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ConnectionRssi",type="int",units="dB",minVal="-128",maxVal="127",description="",get=GetConnectionRssi,set=SetConnectionRssi,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="SinkRssiValidity",type="int",units="Boolean",minVal="0",maxVal="255",description="",get=GetSinkRssiValidity,set=SetSinkRssiValidity,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="SinkRssi",type="int",units="dB",minVal="-32768",maxVal="32767",description="",get=GetSinkRssi,set=SetSinkRssi,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Timestamp",type="int",units="ms",minVal="0",maxVal="4294967295",description="",get=GetTimestamp,set=SetTimestamp,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.RSSI.Result", Debug_RSSI_Result.ID, Debug_RSSI_Result)

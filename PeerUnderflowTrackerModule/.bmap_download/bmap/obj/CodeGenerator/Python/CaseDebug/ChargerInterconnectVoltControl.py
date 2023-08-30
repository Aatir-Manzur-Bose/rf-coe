#    obj/CodeGenerator/Python/CaseDebug/ChargerInterconnectVoltControl.py
#    Created 27/07/2023 at 10:09:58 from:
#        Messages = messages/CaseDebug/ChargerInterconnectVoltControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class CaseDebug_ChargerInterconnectVoltControl_SetGet :
    ID = 118946
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargerInterconnectVoltControlIdEnum = OrderedDict([("CHG_VOLT_EN", 1), ("PLC_VOLT_EN", 2), ("BOOST_VOLT_EN", 3), ("BOOST_VOLT_LEVEL", 4)])
    ReverseChargerInterconnectVoltControlIdEnum = OrderedDict([(1, "CHG_VOLT_EN"), (2, "PLC_VOLT_EN"), (3, "BOOST_VOLT_EN"), (4, "BOOST_VOLT_LEVEL")])
    IDs = OrderedDict([("FunctionBlock", 29), ("Function", 10), ("Operator", 2)])
    ReverseIDs = OrderedDict([(29, "FunctionBlock"), (10, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, CaseDebug_ChargerInterconnectVoltControl_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, CaseDebug_ChargerInterconnectVoltControl_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_SetGet.SIZE)
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
            self.hdr.SetMessageID(CaseDebug_ChargerInterconnectVoltControl_SetGet.ID)
            self.hdr.SetDataLength(CaseDebug_ChargerInterconnectVoltControl_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "CaseDebug.ChargerInterconnectVoltControl.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetId(self, enumAsInt=0):
        """Select the voltage to control"""
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = CaseDebug_ChargerInterconnectVoltControl_SetGet.ReverseChargerInterconnectVoltControlIdEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetLevel(self):
        """When Id is BOOST_VOLT_LEVEL- new level; all other Ids- 0=off, 1=on"""
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetId(self, value):
        """Select the voltage to control"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = CaseDebug_ChargerInterconnectVoltControl_SetGet.ChargerInterconnectVoltControlIdEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetLevel(self, value):
        """When Id is BOOST_VOLT_LEVEL- new level; all other Ids- 0=off, 1=on"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_SetGet.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Id",type="enumeration",units="",minVal="0",maxVal="255",description="Select the voltage to control",get=GetId,set=SetId,count=1, bitfieldInfo = [], enum = [ChargerInterconnectVoltControlIdEnum, ReverseChargerInterconnectVoltControlIdEnum]),\
        FieldInfo(name="Level",type="int",units="",minVal="0",maxVal="255",description="When Id is BOOST_VOLT_LEVEL- new level; all other Ids- 0=off, 1=on",get=GetLevel,set=SetLevel,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("CaseDebug.ChargerInterconnectVoltControl.SetGet", CaseDebug_ChargerInterconnectVoltControl_SetGet.ID, CaseDebug_ChargerInterconnectVoltControl_SetGet)
#    obj/CodeGenerator/Python/CaseDebug/ChargerInterconnectVoltControl.py
#    Created 27/07/2023 at 10:09:58 from:
#        Messages = messages/CaseDebug/ChargerInterconnectVoltControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class CaseDebug_ChargerInterconnectVoltControl_Get :
    ID = 118945
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargerInterconnectVoltControlIdEnum = OrderedDict([("CHG_VOLT_EN", 1), ("PLC_VOLT_EN", 2), ("BOOST_VOLT_EN", 3), ("BOOST_VOLT_LEVEL", 4)])
    ReverseChargerInterconnectVoltControlIdEnum = OrderedDict([(1, "CHG_VOLT_EN"), (2, "PLC_VOLT_EN"), (3, "BOOST_VOLT_EN"), (4, "BOOST_VOLT_LEVEL")])
    IDs = OrderedDict([("FunctionBlock", 29), ("Function", 10), ("Operator", 1)])
    ReverseIDs = OrderedDict([(29, "FunctionBlock"), (10, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Get.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Get.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Get.SIZE)
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
            self.hdr.SetMessageID(CaseDebug_ChargerInterconnectVoltControl_Get.ID)
            self.hdr.SetDataLength(CaseDebug_ChargerInterconnectVoltControl_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "CaseDebug.ChargerInterconnectVoltControl.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetId(self, enumAsInt=0):
        """Select the voltage to inspect"""
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Get.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = CaseDebug_ChargerInterconnectVoltControl_Get.ReverseChargerInterconnectVoltControlIdEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetId(self, value):
        """Select the voltage to inspect"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = CaseDebug_ChargerInterconnectVoltControl_Get.ChargerInterconnectVoltControlIdEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Id",type="enumeration",units="",minVal="0",maxVal="255",description="Select the voltage to inspect",get=GetId,set=SetId,count=1, bitfieldInfo = [], enum = [ChargerInterconnectVoltControlIdEnum, ReverseChargerInterconnectVoltControlIdEnum])\
    ]

Messaging.Register("CaseDebug.ChargerInterconnectVoltControl.Get", CaseDebug_ChargerInterconnectVoltControl_Get.ID, CaseDebug_ChargerInterconnectVoltControl_Get)
#    obj/CodeGenerator/Python/CaseDebug/ChargerInterconnectVoltControl.py
#    Created 27/07/2023 at 10:09:58 from:
#        Messages = messages/CaseDebug/ChargerInterconnectVoltControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class CaseDebug_ChargerInterconnectVoltControl_Status :
    ID = 118947
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargerInterconnectVoltControlIdEnum = OrderedDict([("CHG_VOLT_EN", 1), ("PLC_VOLT_EN", 2), ("BOOST_VOLT_EN", 3), ("BOOST_VOLT_LEVEL", 4)])
    ReverseChargerInterconnectVoltControlIdEnum = OrderedDict([(1, "CHG_VOLT_EN"), (2, "PLC_VOLT_EN"), (3, "BOOST_VOLT_EN"), (4, "BOOST_VOLT_LEVEL")])
    IDs = OrderedDict([("FunctionBlock", 29), ("Function", 10), ("Operator", 3)])
    ReverseIDs = OrderedDict([(29, "FunctionBlock"), (10, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Status.SIZE)
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
            self.hdr.SetMessageID(CaseDebug_ChargerInterconnectVoltControl_Status.ID)
            self.hdr.SetDataLength(CaseDebug_ChargerInterconnectVoltControl_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "CaseDebug.ChargerInterconnectVoltControl.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetId(self, enumAsInt=0):
        """Selected Charger Interconnect voltage"""
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = CaseDebug_ChargerInterconnectVoltControl_Status.ReverseChargerInterconnectVoltControlIdEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetLevel(self):
        """When Id is BOOST_VOLT_LEVEL- current level; all other Ids- 0=off, 1=on"""
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetId(self, value):
        """Selected Charger Interconnect voltage"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = CaseDebug_ChargerInterconnectVoltControl_Status.ChargerInterconnectVoltControlIdEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetLevel(self, value):
        """When Id is BOOST_VOLT_LEVEL- current level; all other Ids- 0=off, 1=on"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Id",type="enumeration",units="",minVal="0",maxVal="255",description="Selected Charger Interconnect voltage",get=GetId,set=SetId,count=1, bitfieldInfo = [], enum = [ChargerInterconnectVoltControlIdEnum, ReverseChargerInterconnectVoltControlIdEnum]),\
        FieldInfo(name="Level",type="int",units="",minVal="0",maxVal="255",description="When Id is BOOST_VOLT_LEVEL- current level; all other Ids- 0=off, 1=on",get=GetLevel,set=SetLevel,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("CaseDebug.ChargerInterconnectVoltControl.Status", CaseDebug_ChargerInterconnectVoltControl_Status.ID, CaseDebug_ChargerInterconnectVoltControl_Status)
#    obj/CodeGenerator/Python/CaseDebug/ChargerInterconnectVoltControl.py
#    Created 27/07/2023 at 10:09:58 from:
#        Messages = messages/CaseDebug/ChargerInterconnectVoltControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class CaseDebug_ChargerInterconnectVoltControl_Error :
    ID = 118948
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("FBlockNotSupported", 3), ("FunctionNotSupported", 4), ("OperatorNotSupported", 5), ("InvalidData", 6), ("DataNotAvailable", 7), ("RunTime", 8), ("Timeout", 9), ("InvalidState", 10), ("DeviceNotFound", 11), ("Busy", 12), ("UnableToConnectTimeout", 13), ("UnableToConnectSourceDeviceKeyMissing", 14), ("OTAFirmwareUpdateInProgress", 15), ("LowBatteryVoltage", 16), ("ChargerNotConnected", 17), ("UpdateNotAllowed", 18), ("UnknownPortNumber", 19), ("InsecureTransport", 20), ("InvalidOTPKey", 21), ("OutOfMemory", 22), ("CryptoProcessingError", 23), ("FeatureLocked", 24), ("FunctionBlockSpecificErrorCode", 255)])
    ReverseErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "FBlockNotSupported"), (4, "FunctionNotSupported"), (5, "OperatorNotSupported"), (6, "InvalidData"), (7, "DataNotAvailable"), (8, "RunTime"), (9, "Timeout"), (10, "InvalidState"), (11, "DeviceNotFound"), (12, "Busy"), (13, "UnableToConnectTimeout"), (14, "UnableToConnectSourceDeviceKeyMissing"), (15, "OTAFirmwareUpdateInProgress"), (16, "LowBatteryVoltage"), (17, "ChargerNotConnected"), (18, "UpdateNotAllowed"), (19, "UnknownPortNumber"), (20, "InsecureTransport"), (21, "InvalidOTPKey"), (22, "OutOfMemory"), (23, "CryptoProcessingError"), (24, "FeatureLocked"), (255, "FunctionBlockSpecificErrorCode")])
    IDs = OrderedDict([("FunctionBlock", 29), ("Function", 10), ("Operator", 4)])
    ReverseIDs = OrderedDict([(29, "FunctionBlock"), (10, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Error.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, CaseDebug_ChargerInterconnectVoltControl_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(CaseDebug_ChargerInterconnectVoltControl_Error.MSG_OFFSET + CaseDebug_ChargerInterconnectVoltControl_Error.SIZE)
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
            self.hdr.SetMessageID(CaseDebug_ChargerInterconnectVoltControl_Error.ID)
            self.hdr.SetDataLength(CaseDebug_ChargerInterconnectVoltControl_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "CaseDebug.ChargerInterconnectVoltControl.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = CaseDebug_ChargerInterconnectVoltControl_Error.ReverseErrorResponseCodes.get(value, value)
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
        value = CaseDebug_ChargerInterconnectVoltControl_Error.ErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), CaseDebug_ChargerInterconnectVoltControl_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [ErrorResponseCodes, ReverseErrorResponseCodes])\
    ]

Messaging.Register("CaseDebug.ChargerInterconnectVoltControl.Error", CaseDebug_ChargerInterconnectVoltControl_Error.ID, CaseDebug_ChargerInterconnectVoltControl_Error)

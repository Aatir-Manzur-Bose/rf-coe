#    obj/CodeGenerator/Python/SensorInterface/SensorVersion.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/SensorInterface/SensorVersion.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_SensorVersion_Get :
    ID = 98353
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SensorVIdEnum = OrderedDict([("Bootloader", 0), ("Application", 1), ("ROM", 2), ("RAM", 3), ("Config", 4)])
    ReverseSensorVIdEnum = OrderedDict([(0, "Bootloader"), (1, "Application"), (2, "ROM"), (3, "RAM"), (4, "Config")])
    SensorTypeEnum = OrderedDict([("Acc", 0), ("Gyro", 1), ("Mag", 2), ("IR", 3), ("Cap", 4), ("IMU", 5), ("InEar", 6), ("UncalMag", 7), ("Rotation", 8), ("GameRotation", 9), ("Component", 10), ("Touch_Debug", 11), ("Cap_Proximity", 12), ("Sensor_Buttons", 13), ("Second_Acc", 32)])
    ReverseSensorTypeEnum = OrderedDict([(0, "Acc"), (1, "Gyro"), (2, "Mag"), (3, "IR"), (4, "Cap"), (5, "IMU"), (6, "InEar"), (7, "UncalMag"), (8, "Rotation"), (9, "GameRotation"), (10, "Component"), (11, "Touch_Debug"), (12, "Cap_Proximity"), (13, "Sensor_Buttons"), (32, "Second_Acc")])
    SensorLocationEnum = OrderedDict([("Left", 0), ("Right", 1), ("Single", 2)])
    ReverseSensorLocationEnum = OrderedDict([(0, "Left"), (1, "Right"), (2, "Single")])
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 3), ("Operator", 1)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (3, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Get.MSG_OFFSET + SensorInterface_SensorVersion_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_SensorVersion_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_SensorVersion_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Get.MSG_OFFSET + SensorInterface_SensorVersion_Get.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_SensorVersion_Get.ID)
            self.hdr.SetDataLength(SensorInterface_SensorVersion_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.SensorVersion.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSensorType(self, enumAsInt=0):
        """Sensor Type"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Get.ReverseSensorTypeEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetSensorLocation(self, enumAsInt=0):
        """Sensor Location"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 1)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Get.ReverseSensorLocationEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetSensorId(self):
        """Sensor Id"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetId(self, enumAsInt=0):
        """Id that you want version of."""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 3)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Get.ReverseSensorVIdEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSensorType(self, value):
        """Sensor Type"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Get.SensorTypeEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetSensorLocation(self, value):
        """Sensor Location"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Get.SensorLocationEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetSensorId(self, value):
        """Sensor Id"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetId(self, value):
        """Id that you want version of."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Get.SensorVIdEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Get.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SensorType",type="enumeration",units="",minVal="0",maxVal="255",description="Sensor Type",get=GetSensorType,set=SetSensorType,count=1, bitfieldInfo = [], enum = [SensorTypeEnum, ReverseSensorTypeEnum]),\
        FieldInfo(name="SensorLocation",type="enumeration",units="",minVal="0",maxVal="255",description="Sensor Location",get=GetSensorLocation,set=SetSensorLocation,count=1, bitfieldInfo = [], enum = [SensorLocationEnum, ReverseSensorLocationEnum]),\
        FieldInfo(name="SensorId",type="int",units="",minVal="0",maxVal="255",description="Sensor Id",get=GetSensorId,set=SetSensorId,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Id",type="enumeration",units="",minVal="0",maxVal="255",description="Id that you want version of.",get=GetId,set=SetId,count=1, bitfieldInfo = [], enum = [SensorVIdEnum, ReverseSensorVIdEnum])\
    ]

Messaging.Register("SensorInterface.SensorVersion.Get", SensorInterface_SensorVersion_Get.ID, SensorInterface_SensorVersion_Get)
#    obj/CodeGenerator/Python/SensorInterface/SensorVersion.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/SensorInterface/SensorVersion.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_SensorVersion_Status :
    ID = 98355
    SIZE = 34
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SensorVIdEnum = OrderedDict([("Bootloader", 0), ("Application", 1), ("ROM", 2), ("RAM", 3), ("Config", 4)])
    ReverseSensorVIdEnum = OrderedDict([(0, "Bootloader"), (1, "Application"), (2, "ROM"), (3, "RAM"), (4, "Config")])
    SensorTypeEnum = OrderedDict([("Acc", 0), ("Gyro", 1), ("Mag", 2), ("IR", 3), ("Cap", 4), ("IMU", 5), ("InEar", 6), ("UncalMag", 7), ("Rotation", 8), ("GameRotation", 9), ("Component", 10), ("Touch_Debug", 11), ("Cap_Proximity", 12), ("Sensor_Buttons", 13), ("Second_Acc", 32)])
    ReverseSensorTypeEnum = OrderedDict([(0, "Acc"), (1, "Gyro"), (2, "Mag"), (3, "IR"), (4, "Cap"), (5, "IMU"), (6, "InEar"), (7, "UncalMag"), (8, "Rotation"), (9, "GameRotation"), (10, "Component"), (11, "Touch_Debug"), (12, "Cap_Proximity"), (13, "Sensor_Buttons"), (32, "Second_Acc")])
    SensorLocationEnum = OrderedDict([("Left", 0), ("Right", 1), ("Single", 2)])
    ReverseSensorLocationEnum = OrderedDict([(0, "Left"), (1, "Right"), (2, "Single")])
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 3), ("Operator", 3)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (3, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Status.MSG_OFFSET + SensorInterface_SensorVersion_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_SensorVersion_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_SensorVersion_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Status.MSG_OFFSET + SensorInterface_SensorVersion_Status.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_SensorVersion_Status.ID)
            self.hdr.SetDataLength(SensorInterface_SensorVersion_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.SensorVersion.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSensorType(self, enumAsInt=0):
        """Sensor Type"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Status.ReverseSensorTypeEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetSensorLocation(self, enumAsInt=0):
        """Sensor Location"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 1)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Status.ReverseSensorLocationEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetSensorId(self):
        """Sensor Id"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetId(self, enumAsInt=0):
        """Id that you want version of."""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 3)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Status.ReverseSensorVIdEnum.get(value, value)
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(30)
    def GetVersion(self):
        """Sensor components Version (UTF-8 string)"""
        count = 30
        if count > len(self.rawBuffer())-(SensorInterface_SensorVersion_Status.MSG_OFFSET + 4):
            count = len(self.rawBuffer())-(SensorInterface_SensorVersion_Status.MSG_OFFSET + 4)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 4)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSensorType(self, value):
        """Sensor Type"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Status.SensorTypeEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetSensorLocation(self, value):
        """Sensor Location"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Status.SensorLocationEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetSensorId(self, value):
        """Sensor Id"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetId(self, value):
        """Id that you want version of."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_SensorVersion_Status.SensorVIdEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 3, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(30)
    def SetVersion(self, value):
        """Sensor components Version (UTF-8 string)"""
        tmp = value.encode('utf-8')
        struct.pack_into('30s', self.rawBuffer(), SensorInterface_SensorVersion_Status.MSG_OFFSET + 4, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SensorType",type="enumeration",units="",minVal="0",maxVal="255",description="Sensor Type",get=GetSensorType,set=SetSensorType,count=1, bitfieldInfo = [], enum = [SensorTypeEnum, ReverseSensorTypeEnum]),\
        FieldInfo(name="SensorLocation",type="enumeration",units="",minVal="0",maxVal="255",description="Sensor Location",get=GetSensorLocation,set=SetSensorLocation,count=1, bitfieldInfo = [], enum = [SensorLocationEnum, ReverseSensorLocationEnum]),\
        FieldInfo(name="SensorId",type="int",units="",minVal="0",maxVal="255",description="Sensor Id",get=GetSensorId,set=SetSensorId,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Id",type="enumeration",units="",minVal="0",maxVal="255",description="Id that you want version of.",get=GetId,set=SetId,count=1, bitfieldInfo = [], enum = [SensorVIdEnum, ReverseSensorVIdEnum]),\
        FieldInfo(name="Version",type="string",units="ASCII",minVal="0",maxVal="255",description="Sensor components Version (UTF-8 string)",get=GetVersion,set=SetVersion,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SensorInterface.SensorVersion.Status", SensorInterface_SensorVersion_Status.ID, SensorInterface_SensorVersion_Status)
#    obj/CodeGenerator/Python/SensorInterface/SensorVersion.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/SensorInterface/SensorVersion.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_SensorVersion_Error :
    ID = 98356
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("FBlockNotSupported", 3), ("FunctionNotSupported", 4), ("OperatorNotSupported", 5), ("InvalidData", 6), ("DataNotAvailable", 7), ("RunTime", 8), ("Timeout", 9), ("InvalidState", 10), ("DeviceNotFound", 11), ("Busy", 12), ("UnableToConnectTimeout", 13), ("UnableToConnectSourceDeviceKeyMissing", 14), ("OTAFirmwareUpdateInProgress", 15), ("LowBatteryVoltage", 16), ("ChargerNotConnected", 17), ("UpdateNotAllowed", 18), ("UnknownPortNumber", 19), ("InsecureTransport", 20), ("InvalidOTPKey", 21), ("OutOfMemory", 22), ("CryptoProcessingError", 23), ("FeatureLocked", 24), ("FunctionBlockSpecificErrorCode", 255)])
    ReverseErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "FBlockNotSupported"), (4, "FunctionNotSupported"), (5, "OperatorNotSupported"), (6, "InvalidData"), (7, "DataNotAvailable"), (8, "RunTime"), (9, "Timeout"), (10, "InvalidState"), (11, "DeviceNotFound"), (12, "Busy"), (13, "UnableToConnectTimeout"), (14, "UnableToConnectSourceDeviceKeyMissing"), (15, "OTAFirmwareUpdateInProgress"), (16, "LowBatteryVoltage"), (17, "ChargerNotConnected"), (18, "UpdateNotAllowed"), (19, "UnknownPortNumber"), (20, "InsecureTransport"), (21, "InvalidOTPKey"), (22, "OutOfMemory"), (23, "CryptoProcessingError"), (24, "FeatureLocked"), (255, "FunctionBlockSpecificErrorCode")])
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 3), ("Operator", 4)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (3, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Error.MSG_OFFSET + SensorInterface_SensorVersion_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_SensorVersion_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_SensorVersion_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_SensorVersion_Error.MSG_OFFSET + SensorInterface_SensorVersion_Error.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_SensorVersion_Error.ID)
            self.hdr.SetDataLength(SensorInterface_SensorVersion_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.SensorVersion.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_SensorVersion_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SensorInterface_SensorVersion_Error.ReverseErrorResponseCodes.get(value, value)
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
        value = SensorInterface_SensorVersion_Error.ErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_SensorVersion_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [ErrorResponseCodes, ReverseErrorResponseCodes])\
    ]

Messaging.Register("SensorInterface.SensorVersion.Error", SensorInterface_SensorVersion_Error.ID, SensorInterface_SensorVersion_Error)

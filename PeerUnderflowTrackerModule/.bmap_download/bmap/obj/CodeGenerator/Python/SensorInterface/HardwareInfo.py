#    obj/CodeGenerator/Python/SensorInterface/HardwareInfo.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/HardwareInfo.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_HardwareInfo_Get :
    ID = 98337
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SensorHWInfoTypeEnum = OrderedDict([("Cypress/Sensor subsystem HW info type", 0), ("Cypress bootloader diags HW info type", 1)])
    ReverseSensorHWInfoTypeEnum = OrderedDict([(0, "Cypress/Sensor subsystem HW info type"), (1, "Cypress bootloader diags HW info type")])
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 2), ("Operator", 1)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (2, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Get.MSG_OFFSET + SensorInterface_HardwareInfo_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_HardwareInfo_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_HardwareInfo_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Get.MSG_OFFSET + SensorInterface_HardwareInfo_Get.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_HardwareInfo_Get.ID)
            self.hdr.SetDataLength(SensorInterface_HardwareInfo_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.HardwareInfo.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSensorHWInfoType(self, enumAsInt=0):
        """Type of sensor HW info to be fetched"""
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_HardwareInfo_Get.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SensorInterface_HardwareInfo_Get.ReverseSensorHWInfoTypeEnum.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSensorHWInfoType(self, value):
        """Type of sensor HW info to be fetched"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SensorInterface_HardwareInfo_Get.SensorHWInfoTypeEnum.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SensorInterface_HardwareInfo_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SensorHWInfoType",type="enumeration",units="",minVal="0",maxVal="255",description="Type of sensor HW info to be fetched",get=GetSensorHWInfoType,set=SetSensorHWInfoType,count=1, bitfieldInfo = [], enum = [SensorHWInfoTypeEnum, ReverseSensorHWInfoTypeEnum])\
    ]

Messaging.Register("SensorInterface.HardwareInfo.Get", SensorInterface_HardwareInfo_Get.ID, SensorInterface_HardwareInfo_Get)
#    obj/CodeGenerator/Python/SensorInterface/HardwareInfo.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/HardwareInfo.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_HardwareInfo_Status :
    ID = 98339
    SIZE = 16
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 2), ("Operator", 3)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (2, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Status.MSG_OFFSET + SensorInterface_HardwareInfo_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_HardwareInfo_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_HardwareInfo_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Status.MSG_OFFSET + SensorInterface_HardwareInfo_Status.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_HardwareInfo_Status.ID)
            self.hdr.SetDataLength(SensorInterface_HardwareInfo_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.HardwareInfo.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def GetPrimaryMicroprocessorID(self):
        """Primary Microprocessor ID"""
        value = struct.unpack_from('>L', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('4')
    @msg.size('4')
    @msg.count(1)
    def GetSecondaryMicroprocessorID(self):
        """Secondary Microprocessor ID"""
        value = struct.unpack_from('>L', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def GetSensor1ID(self):
        """Sensor 1 ID"""
        value = struct.unpack_from('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 8)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def GetSensor2ID(self):
        """Sensor 2 ID"""
        value = struct.unpack_from('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 10)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('12')
    @msg.size('2')
    @msg.count(1)
    def GetSensor3ID(self):
        """Sensor 3 ID"""
        value = struct.unpack_from('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 12)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('14')
    @msg.size('2')
    @msg.count(1)
    def GetSensor4ID(self):
        """Sensor 4 ID"""
        value = struct.unpack_from('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 14)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def SetPrimaryMicroprocessorID(self, value):
        """Primary Microprocessor ID"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('4')
    @msg.size('4')
    @msg.count(1)
    def SetSecondaryMicroprocessorID(self, value):
        """Secondary Microprocessor ID"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def SetSensor1ID(self, value):
        """Sensor 1 ID"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 8, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def SetSensor2ID(self, value):
        """Sensor 2 ID"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 10, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('12')
    @msg.size('2')
    @msg.count(1)
    def SetSensor3ID(self, value):
        """Sensor 3 ID"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 12, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('14')
    @msg.size('2')
    @msg.count(1)
    def SetSensor4ID(self, value):
        """Sensor 4 ID"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SensorInterface_HardwareInfo_Status.MSG_OFFSET + 14, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="PrimaryMicroprocessorID",type="int",units="",minVal="0",maxVal="4294967295",description="Primary Microprocessor ID",get=GetPrimaryMicroprocessorID,set=SetPrimaryMicroprocessorID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="SecondaryMicroprocessorID",type="int",units="",minVal="0",maxVal="4294967295",description="Secondary Microprocessor ID",get=GetSecondaryMicroprocessorID,set=SetSecondaryMicroprocessorID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Sensor1ID",type="int",units="",minVal="0",maxVal="65535",description="Sensor 1 ID",get=GetSensor1ID,set=SetSensor1ID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Sensor2ID",type="int",units="",minVal="0",maxVal="65535",description="Sensor 2 ID",get=GetSensor2ID,set=SetSensor2ID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Sensor3ID",type="int",units="",minVal="0",maxVal="65535",description="Sensor 3 ID",get=GetSensor3ID,set=SetSensor3ID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Sensor4ID",type="int",units="",minVal="0",maxVal="65535",description="Sensor 4 ID",get=GetSensor4ID,set=SetSensor4ID,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SensorInterface.HardwareInfo.Status", SensorInterface_HardwareInfo_Status.ID, SensorInterface_HardwareInfo_Status)
#    obj/CodeGenerator/Python/SensorInterface/HardwareInfo.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/HardwareInfo.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_HardwareInfo_Result :
    ID = 98342
    SIZE = 128
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 2), ("Operator", 6)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (2, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Result.MSG_OFFSET + SensorInterface_HardwareInfo_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_HardwareInfo_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_HardwareInfo_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_HardwareInfo_Result.MSG_OFFSET + SensorInterface_HardwareInfo_Result.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_HardwareInfo_Result.ID)
            self.hdr.SetDataLength(SensorInterface_HardwareInfo_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.HardwareInfo.Result"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(128)
    def GetState(self):
        """Details"""
        count = 128
        if count > len(self.rawBuffer())-(SensorInterface_HardwareInfo_Result.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(SensorInterface_HardwareInfo_Result.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SensorInterface_HardwareInfo_Result.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(128)
    def SetState(self, value):
        """Details"""
        tmp = value.encode('utf-8')
        struct.pack_into('128s', self.rawBuffer(), SensorInterface_HardwareInfo_Result.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="State",type="string",units="ASCII",minVal="0",maxVal="255",description="Details",get=GetState,set=SetState,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SensorInterface.HardwareInfo.Result", SensorInterface_HardwareInfo_Result.ID, SensorInterface_HardwareInfo_Result)

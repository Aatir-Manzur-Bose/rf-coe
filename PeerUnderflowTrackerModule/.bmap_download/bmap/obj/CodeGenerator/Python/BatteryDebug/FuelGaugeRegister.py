#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeRegister.py
#    Created 27/07/2023 at 10:09:51 from:
#        Messages = messages/BatteryDebug/FuelGaugeRegister.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeRegister_Get :
    ID = 103041
    SIZE = 3
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 40), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (40, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeRegister_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeRegister_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeRegister_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeRegister_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeRegister.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeID(self):
        """Fuel gauge ID"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetRegisterAddress(self):
        """Register address"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeID(self, value):
        """Fuel gauge ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetRegisterAddress(self, value):
        """Register address"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Get.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeID",type="int",units="",minVal="0",maxVal="255",description="Fuel gauge ID",get=GetFuelGaugeID,set=SetFuelGaugeID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterAddress",type="int",units="",minVal="0",maxVal="65535",description="Register address",get=GetRegisterAddress,set=SetRegisterAddress,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeRegister.Get", BatteryDebug_FuelGaugeRegister_Get.ID, BatteryDebug_FuelGaugeRegister_Get)
#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeRegister.py
#    Created 27/07/2023 at 10:09:51 from:
#        Messages = messages/BatteryDebug/FuelGaugeRegister.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeRegister_SetGet :
    ID = 103042
    SIZE = 7
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 40), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (40, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeRegister_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeRegister_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeRegister_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeRegister_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeRegister.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeID(self):
        """Fuel gauge ID"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetRegisterAddress(self):
        """Register address"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('3')
    @msg.size('4')
    @msg.count(1)
    def GetRegisterValue(self):
        """Register value"""
        value = struct.unpack_from('>L', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeID(self, value):
        """Fuel gauge ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetRegisterAddress(self, value):
        """Register address"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('3')
    @msg.size('4')
    @msg.count(1)
    def SetRegisterValue(self, value):
        """Register value"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_SetGet.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeID",type="int",units="",minVal="0",maxVal="255",description="Fuel gauge ID",get=GetFuelGaugeID,set=SetFuelGaugeID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterAddress",type="int",units="",minVal="0",maxVal="65535",description="Register address",get=GetRegisterAddress,set=SetRegisterAddress,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterValue",type="int",units="",minVal="0",maxVal="4294967295",description="Register value",get=GetRegisterValue,set=SetRegisterValue,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeRegister.SetGet", BatteryDebug_FuelGaugeRegister_SetGet.ID, BatteryDebug_FuelGaugeRegister_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeRegister.py
#    Created 27/07/2023 at 10:09:51 from:
#        Messages = messages/BatteryDebug/FuelGaugeRegister.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeRegister_Status :
    ID = 103043
    SIZE = 7
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 40), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (40, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeRegister_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeRegister_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + BatteryDebug_FuelGaugeRegister_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeRegister_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeRegister_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeRegister.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeID(self):
        """Fuel gauge ID"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetRegisterAddress(self):
        """Register address"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('3')
    @msg.size('4')
    @msg.count(1)
    def GetRegisterValue(self):
        """Register value"""
        value = struct.unpack_from('>L', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeID(self, value):
        """Fuel gauge ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetRegisterAddress(self, value):
        """Register address"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('3')
    @msg.size('4')
    @msg.count(1)
    def SetRegisterValue(self, value):
        """Register value"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), BatteryDebug_FuelGaugeRegister_Status.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeID",type="int",units="",minVal="0",maxVal="255",description="Fuel gauge ID",get=GetFuelGaugeID,set=SetFuelGaugeID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterAddress",type="int",units="",minVal="0",maxVal="65535",description="Register address",get=GetRegisterAddress,set=SetRegisterAddress,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterValue",type="int",units="",minVal="0",maxVal="4294967295",description="Register value",get=GetRegisterValue,set=SetRegisterValue,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeRegister.Status", BatteryDebug_FuelGaugeRegister_Status.ID, BatteryDebug_FuelGaugeRegister_Status)

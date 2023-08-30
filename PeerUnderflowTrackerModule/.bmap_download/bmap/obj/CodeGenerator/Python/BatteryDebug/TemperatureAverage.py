#    obj/CodeGenerator/Python/BatteryDebug/TemperatureAverage.py
#    Created 27/07/2023 at 10:09:55 from:
#        Messages = messages/BatteryDebug/TemperatureAverage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_TemperatureAverage_Get :
    ID = 102545
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 9), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (9, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_Get.MSG_OFFSET + BatteryDebug_TemperatureAverage_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_TemperatureAverage_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_TemperatureAverage_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_Get.MSG_OFFSET + BatteryDebug_TemperatureAverage_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_TemperatureAverage_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_TemperatureAverage_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.TemperatureAverage.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.TemperatureAverage.Get", BatteryDebug_TemperatureAverage_Get.ID, BatteryDebug_TemperatureAverage_Get)
#    obj/CodeGenerator/Python/BatteryDebug/TemperatureAverage.py
#    Created 27/07/2023 at 10:09:55 from:
#        Messages = messages/BatteryDebug/TemperatureAverage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_TemperatureAverage_SetGet :
    ID = 102546
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 9), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (9, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_SetGet.MSG_OFFSET + BatteryDebug_TemperatureAverage_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_TemperatureAverage_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_TemperatureAverage_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_SetGet.MSG_OFFSET + BatteryDebug_TemperatureAverage_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_TemperatureAverage_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_TemperatureAverage_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.TemperatureAverage.SetGet"
    # Accessors
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetTemperatureAverage(self):
        """Average temperature"""
        value = struct.unpack_from('>h', self.rawBuffer(), BatteryDebug_TemperatureAverage_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetTemperatureAverage(self, value):
        """Average temperature"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), BatteryDebug_TemperatureAverage_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TemperatureAverage",type="int",units="C",minVal="-32768",maxVal="32767",description="Average temperature",get=GetTemperatureAverage,set=SetTemperatureAverage,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.TemperatureAverage.SetGet", BatteryDebug_TemperatureAverage_SetGet.ID, BatteryDebug_TemperatureAverage_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/TemperatureAverage.py
#    Created 27/07/2023 at 10:09:55 from:
#        Messages = messages/BatteryDebug/TemperatureAverage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_TemperatureAverage_Status :
    ID = 102547
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 9), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (9, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_Status.MSG_OFFSET + BatteryDebug_TemperatureAverage_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_TemperatureAverage_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_TemperatureAverage_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_TemperatureAverage_Status.MSG_OFFSET + BatteryDebug_TemperatureAverage_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_TemperatureAverage_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_TemperatureAverage_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.TemperatureAverage.Status"
    # Accessors
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetTemperatureAverage(self):
        """Average temperature"""
        value = struct.unpack_from('>h', self.rawBuffer(), BatteryDebug_TemperatureAverage_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetTemperatureAverage(self, value):
        """Average temperature"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), BatteryDebug_TemperatureAverage_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TemperatureAverage",type="int",units="C",minVal="-32768",maxVal="32767",description="Average temperature",get=GetTemperatureAverage,set=SetTemperatureAverage,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.TemperatureAverage.Status", BatteryDebug_TemperatureAverage_Status.ID, BatteryDebug_TemperatureAverage_Status)

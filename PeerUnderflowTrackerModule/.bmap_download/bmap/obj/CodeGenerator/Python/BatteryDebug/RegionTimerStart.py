#    obj/CodeGenerator/Python/BatteryDebug/RegionTimerStart.py
#    Created 27/07/2023 at 10:09:52 from:
#        Messages = messages/BatteryDebug/RegionTimerStart.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_RegionTimerStart_Get :
    ID = 102929
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 33), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (33, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_Get.MSG_OFFSET + BatteryDebug_RegionTimerStart_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_RegionTimerStart_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_RegionTimerStart_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_Get.MSG_OFFSET + BatteryDebug_RegionTimerStart_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_RegionTimerStart_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_RegionTimerStart_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.RegionTimerStart.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.RegionTimerStart.Get", BatteryDebug_RegionTimerStart_Get.ID, BatteryDebug_RegionTimerStart_Get)
#    obj/CodeGenerator/Python/BatteryDebug/RegionTimerStart.py
#    Created 27/07/2023 at 10:09:52 from:
#        Messages = messages/BatteryDebug/RegionTimerStart.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_RegionTimerStart_SetGet :
    ID = 102930
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 33), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (33, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_SetGet.MSG_OFFSET + BatteryDebug_RegionTimerStart_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_RegionTimerStart_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_RegionTimerStart_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_SetGet.MSG_OFFSET + BatteryDebug_RegionTimerStart_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_RegionTimerStart_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_RegionTimerStart_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.RegionTimerStart.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetRegionTimerStart(self):
        """Region timer start"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_RegionTimerStart_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetRegionTimerStart(self, value):
        """Region timer start"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_RegionTimerStart_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="RegionTimerStart",type="int",units="",minVal="0",maxVal="65535",description="Region timer start",get=GetRegionTimerStart,set=SetRegionTimerStart,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.RegionTimerStart.SetGet", BatteryDebug_RegionTimerStart_SetGet.ID, BatteryDebug_RegionTimerStart_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/RegionTimerStart.py
#    Created 27/07/2023 at 10:09:52 from:
#        Messages = messages/BatteryDebug/RegionTimerStart.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_RegionTimerStart_Status :
    ID = 102931
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 33), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (33, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_Status.MSG_OFFSET + BatteryDebug_RegionTimerStart_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_RegionTimerStart_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_RegionTimerStart_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_RegionTimerStart_Status.MSG_OFFSET + BatteryDebug_RegionTimerStart_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_RegionTimerStart_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_RegionTimerStart_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.RegionTimerStart.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetRegionTimerStart(self):
        """Region timer start"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_RegionTimerStart_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetRegionTimerStart(self, value):
        """Region timer start"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_RegionTimerStart_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="RegionTimerStart",type="int",units="",minVal="0",maxVal="65535",description="Region timer start",get=GetRegionTimerStart,set=SetRegionTimerStart,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.RegionTimerStart.Status", BatteryDebug_RegionTimerStart_Status.ID, BatteryDebug_RegionTimerStart_Status)

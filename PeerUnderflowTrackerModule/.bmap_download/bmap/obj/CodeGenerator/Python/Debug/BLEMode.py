#    obj/CodeGenerator/Python/Debug/BLEMode.py
#    Created 27/07/2023 at 10:10:06 from:
#        Messages = messages/Debug/BLEMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_BLEMode_Get :
    ID = 33249
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 30), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (30, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_BLEMode_Get.MSG_OFFSET + Debug_BLEMode_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_BLEMode_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_BLEMode_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_BLEMode_Get.MSG_OFFSET + Debug_BLEMode_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_BLEMode_Get.ID)
            self.hdr.SetDataLength(Debug_BLEMode_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.BLEMode.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.BLEMode.Get", Debug_BLEMode_Get.ID, Debug_BLEMode_Get)
#    obj/CodeGenerator/Python/Debug/BLEMode.py
#    Created 27/07/2023 at 10:10:06 from:
#        Messages = messages/Debug/BLEMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_BLEMode_SetGet :
    ID = 33250
    SIZE = 3
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    BLEModeList = OrderedDict([("Normal", 0), ("AdvertisingOn", 1), ("Off", 2)])
    ReverseBLEModeList = OrderedDict([(0, "Normal"), (1, "AdvertisingOn"), (2, "Off")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 30), ("Operator", 2)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (30, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_BLEMode_SetGet.MSG_OFFSET + Debug_BLEMode_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_BLEMode_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_BLEMode_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_BLEMode_SetGet.MSG_OFFSET + Debug_BLEMode_SetGet.SIZE)
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
            self.hdr.SetMessageID(Debug_BLEMode_SetGet.ID)
            self.hdr.SetDataLength(Debug_BLEMode_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.BLEMode.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBLEMode(self, enumAsInt=0):
        """The BLE mode to set."""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_BLEMode_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_BLEMode_SetGet.ReverseBLEModeList.get(value, value)
        return value
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetBLETimer(self):
        """(Optional, only for Off mode) Duration timer in seconds."""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_BLEMode_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBLEMode(self, value):
        """The BLE mode to set."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_BLEMode_SetGet.BLEModeList.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_BLEMode_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetBLETimer(self, value):
        """(Optional, only for Off mode) Duration timer in seconds."""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_BLEMode_SetGet.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BLEMode",type="enumeration",units="",minVal="0",maxVal="255",description="The BLE mode to set.",get=GetBLEMode,set=SetBLEMode,count=1, bitfieldInfo = [], enum = [BLEModeList, ReverseBLEModeList]),\
        FieldInfo(name="BLETimer",type="int",units="seconds",minVal="0",maxVal="65535",description="(Optional, only for Off mode) Duration timer in seconds.",get=GetBLETimer,set=SetBLETimer,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.BLEMode.SetGet", Debug_BLEMode_SetGet.ID, Debug_BLEMode_SetGet)
#    obj/CodeGenerator/Python/Debug/BLEMode.py
#    Created 27/07/2023 at 10:10:06 from:
#        Messages = messages/Debug/BLEMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_BLEMode_Status :
    ID = 33251
    SIZE = 3
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    BLEModeList = OrderedDict([("Normal", 0), ("AdvertisingOn", 1), ("Off", 2)])
    ReverseBLEModeList = OrderedDict([(0, "Normal"), (1, "AdvertisingOn"), (2, "Off")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 30), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (30, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_BLEMode_Status.MSG_OFFSET + Debug_BLEMode_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_BLEMode_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_BLEMode_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_BLEMode_Status.MSG_OFFSET + Debug_BLEMode_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_BLEMode_Status.ID)
            self.hdr.SetDataLength(Debug_BLEMode_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.BLEMode.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBLEMode(self, enumAsInt=0):
        """The current BLE mode."""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_BLEMode_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_BLEMode_Status.ReverseBLEModeList.get(value, value)
        return value
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetBLETimer(self):
        """(Only for Off mode under duration) Remaining duration in seconds."""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_BLEMode_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBLEMode(self, value):
        """The current BLE mode."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_BLEMode_Status.BLEModeList.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_BLEMode_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetBLETimer(self, value):
        """(Only for Off mode under duration) Remaining duration in seconds."""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_BLEMode_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BLEMode",type="enumeration",units="",minVal="0",maxVal="255",description="The current BLE mode.",get=GetBLEMode,set=SetBLEMode,count=1, bitfieldInfo = [], enum = [BLEModeList, ReverseBLEModeList]),\
        FieldInfo(name="BLETimer",type="int",units="seconds",minVal="0",maxVal="65535",description="(Only for Off mode under duration) Remaining duration in seconds.",get=GetBLETimer,set=SetBLETimer,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.BLEMode.Status", Debug_BLEMode_Status.ID, Debug_BLEMode_Status)

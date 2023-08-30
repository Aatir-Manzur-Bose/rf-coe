#    obj/CodeGenerator/Python/BatteryDebug/BatteryCapacity.py
#    Created 27/07/2023 at 10:09:46 from:
#        Messages = messages/BatteryDebug/BatteryCapacity.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_BatteryCapacity_Get :
    ID = 102673
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 17), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (17, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_Get.MSG_OFFSET + BatteryDebug_BatteryCapacity_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_BatteryCapacity_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_BatteryCapacity_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_Get.MSG_OFFSET + BatteryDebug_BatteryCapacity_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_BatteryCapacity_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_BatteryCapacity_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.BatteryCapacity.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.BatteryCapacity.Get", BatteryDebug_BatteryCapacity_Get.ID, BatteryDebug_BatteryCapacity_Get)
#    obj/CodeGenerator/Python/BatteryDebug/BatteryCapacity.py
#    Created 27/07/2023 at 10:09:46 from:
#        Messages = messages/BatteryDebug/BatteryCapacity.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_BatteryCapacity_SetGet :
    ID = 102674
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    BatteryCapacity = OrderedDict([("Full", 0), ("NotFull", 1)])
    ReverseBatteryCapacity = OrderedDict([(0, "Full"), (1, "NotFull")])
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 17), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (17, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_SetGet.MSG_OFFSET + BatteryDebug_BatteryCapacity_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_BatteryCapacity_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_BatteryCapacity_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_SetGet.MSG_OFFSET + BatteryDebug_BatteryCapacity_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_BatteryCapacity_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_BatteryCapacity_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.BatteryCapacity.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBatteryCapacity(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_BatteryCapacity_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = BatteryDebug_BatteryCapacity_SetGet.ReverseBatteryCapacity.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBatteryCapacity(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = BatteryDebug_BatteryCapacity_SetGet.BatteryCapacity.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_BatteryCapacity_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BatteryCapacity",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetBatteryCapacity,set=SetBatteryCapacity,count=1, bitfieldInfo = [], enum = [BatteryCapacity, ReverseBatteryCapacity])\
    ]

Messaging.Register("BatteryDebug.BatteryCapacity.SetGet", BatteryDebug_BatteryCapacity_SetGet.ID, BatteryDebug_BatteryCapacity_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/BatteryCapacity.py
#    Created 27/07/2023 at 10:09:46 from:
#        Messages = messages/BatteryDebug/BatteryCapacity.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_BatteryCapacity_Status :
    ID = 102675
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    BatteryCapacity = OrderedDict([("Full", 0), ("NotFull", 1)])
    ReverseBatteryCapacity = OrderedDict([(0, "Full"), (1, "NotFull")])
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 17), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (17, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_Status.MSG_OFFSET + BatteryDebug_BatteryCapacity_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_BatteryCapacity_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_BatteryCapacity_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_BatteryCapacity_Status.MSG_OFFSET + BatteryDebug_BatteryCapacity_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_BatteryCapacity_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_BatteryCapacity_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.BatteryCapacity.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBatteryCapacity(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_BatteryCapacity_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = BatteryDebug_BatteryCapacity_Status.ReverseBatteryCapacity.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBatteryCapacity(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = BatteryDebug_BatteryCapacity_Status.BatteryCapacity.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_BatteryCapacity_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BatteryCapacity",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetBatteryCapacity,set=SetBatteryCapacity,count=1, bitfieldInfo = [], enum = [BatteryCapacity, ReverseBatteryCapacity])\
    ]

Messaging.Register("BatteryDebug.BatteryCapacity.Status", BatteryDebug_BatteryCapacity_Status.ID, BatteryDebug_BatteryCapacity_Status)

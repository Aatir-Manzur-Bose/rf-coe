#    obj/CodeGenerator/Python/BatteryDebug/BatteryLogRaw.py
#    Created 27/07/2023 at 10:09:47 from:
#        Messages = messages/BatteryDebug/BatteryLogRaw.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_BatteryLogRaw_Get :
    ID = 103329
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 58), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (58, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_BatteryLogRaw_Get.MSG_OFFSET + BatteryDebug_BatteryLogRaw_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_BatteryLogRaw_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_BatteryLogRaw_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_BatteryLogRaw_Get.MSG_OFFSET + BatteryDebug_BatteryLogRaw_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_BatteryLogRaw_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_BatteryLogRaw_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.BatteryLogRaw.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.BatteryLogRaw.Get", BatteryDebug_BatteryLogRaw_Get.ID, BatteryDebug_BatteryLogRaw_Get)
#    obj/CodeGenerator/Python/BatteryDebug/BatteryLogRaw.py
#    Created 27/07/2023 at 10:09:47 from:
#        Messages = messages/BatteryDebug/BatteryLogRaw.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_BatteryLogRaw_Status :
    ID = 103331
    SIZE = 254
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 58), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (58, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + BatteryDebug_BatteryLogRaw_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_BatteryLogRaw_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_BatteryLogRaw_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + BatteryDebug_BatteryLogRaw_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_BatteryLogRaw_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_BatteryLogRaw_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.BatteryLogRaw.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(254)
    def GetPersistData(self):
        """Battery persistence data (bytes in hex)"""
        count = 254
        if count > len(self.rawBuffer())-(BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(254)
    def SetPersistData(self, value):
        """Battery persistence data (bytes in hex)"""
        tmp = value.encode('utf-8')
        struct.pack_into('254s', self.rawBuffer(), BatteryDebug_BatteryLogRaw_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="PersistData",type="string",units="ASCII",minVal="0",maxVal="255",description="Battery persistence data (bytes in hex)",get=GetPersistData,set=SetPersistData,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.BatteryLogRaw.Status", BatteryDebug_BatteryLogRaw_Status.ID, BatteryDebug_BatteryLogRaw_Status)

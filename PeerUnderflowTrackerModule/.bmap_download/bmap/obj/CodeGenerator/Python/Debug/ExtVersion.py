#    obj/CodeGenerator/Python/Debug/ExtVersion.py
#    Created 27/07/2023 at 10:10:11 from:
#        Messages = messages/Debug/ExtVersion.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_ExtVersion_Get :
    ID = 32993
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 14), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (14, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_ExtVersion_Get.MSG_OFFSET + Debug_ExtVersion_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_ExtVersion_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_ExtVersion_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_ExtVersion_Get.MSG_OFFSET + Debug_ExtVersion_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_ExtVersion_Get.ID)
            self.hdr.SetDataLength(Debug_ExtVersion_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.ExtVersion.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.ExtVersion.Get", Debug_ExtVersion_Get.ID, Debug_ExtVersion_Get)
#    obj/CodeGenerator/Python/Debug/ExtVersion.py
#    Created 27/07/2023 at 10:10:11 from:
#        Messages = messages/Debug/ExtVersion.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_ExtVersion_Status :
    ID = 32995
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 14), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (14, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_ExtVersion_Status.MSG_OFFSET + Debug_ExtVersion_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_ExtVersion_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_ExtVersion_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_ExtVersion_Status.MSG_OFFSET + Debug_ExtVersion_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_ExtVersion_Status.ID)
            self.hdr.SetDataLength(Debug_ExtVersion_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.ExtVersion.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetExtVer(self):
        """Extended Version string"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_ExtVersion_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetExtVer(self, value):
        """Extended Version string"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_ExtVersion_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ExtVer",type="string",units="ASCII",minVal="0",maxVal="255",description="Extended Version string",get=GetExtVer,set=SetExtVer,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.ExtVersion.Status", Debug_ExtVersion_Status.ID, Debug_ExtVersion_Status)

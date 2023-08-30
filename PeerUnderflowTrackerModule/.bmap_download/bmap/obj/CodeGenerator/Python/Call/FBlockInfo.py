#    obj/CodeGenerator/Python/Call/FBlockInfo.py
#    Created 27/07/2023 at 10:09:57 from:
#        Messages = messages/Call/FBlockInfo.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Call_FBlockInfo_Get :
    ID = 24577
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 6), ("Function", 0), ("Operator", 1)])
    ReverseIDs = OrderedDict([(6, "FunctionBlock"), (0, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Call_FBlockInfo_Get.MSG_OFFSET + Call_FBlockInfo_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Call_FBlockInfo_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Call_FBlockInfo_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Call_FBlockInfo_Get.MSG_OFFSET + Call_FBlockInfo_Get.SIZE)
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
            self.hdr.SetMessageID(Call_FBlockInfo_Get.ID)
            self.hdr.SetDataLength(Call_FBlockInfo_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Call.FBlockInfo.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Call.FBlockInfo.Get", Call_FBlockInfo_Get.ID, Call_FBlockInfo_Get)
#    obj/CodeGenerator/Python/Call/FBlockInfo.py
#    Created 27/07/2023 at 10:09:57 from:
#        Messages = messages/Call/FBlockInfo.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Call_FBlockInfo_Status :
    ID = 24579
    SIZE = 60
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 6), ("Function", 0), ("Operator", 3)])
    ReverseIDs = OrderedDict([(6, "FunctionBlock"), (0, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Call_FBlockInfo_Status.MSG_OFFSET + Call_FBlockInfo_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Call_FBlockInfo_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Call_FBlockInfo_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Call_FBlockInfo_Status.MSG_OFFSET + Call_FBlockInfo_Status.SIZE)
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
            self.hdr.SetMessageID(Call_FBlockInfo_Status.ID)
            self.hdr.SetDataLength(Call_FBlockInfo_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Call.FBlockInfo.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(60)
    def GetFunctionBlockVersion(self):
        """Function block version(UTF-8 string)"""
        count = 60
        if count > len(self.rawBuffer())-(Call_FBlockInfo_Status.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(Call_FBlockInfo_Status.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Call_FBlockInfo_Status.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(60)
    def SetFunctionBlockVersion(self, value):
        """Function block version(UTF-8 string)"""
        tmp = value.encode('utf-8')
        struct.pack_into('60s', self.rawBuffer(), Call_FBlockInfo_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FunctionBlockVersion",type="string",units="ASCII",minVal="0",maxVal="255",description="Function block version(UTF-8 string)",get=GetFunctionBlockVersion,set=SetFunctionBlockVersion,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Call.FBlockInfo.Status", Call_FBlockInfo_Status.ID, Call_FBlockInfo_Status)

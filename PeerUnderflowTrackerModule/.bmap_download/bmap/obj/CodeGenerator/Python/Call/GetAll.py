#    obj/CodeGenerator/Python/Call/GetAll.py
#    Created 27/07/2023 at 10:09:57 from:
#        Messages = messages/Call/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Call_GetAll_Start :
    ID = 24597
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 6), ("Function", 1), ("Operator", 5)])
    ReverseIDs = OrderedDict([(6, "FunctionBlock"), (1, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Call_GetAll_Start.MSG_OFFSET + Call_GetAll_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Call_GetAll_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Call_GetAll_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Call_GetAll_Start.MSG_OFFSET + Call_GetAll_Start.SIZE)
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
            self.hdr.SetMessageID(Call_GetAll_Start.ID)
            self.hdr.SetDataLength(Call_GetAll_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Call.GetAll.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Call.GetAll.Start", Call_GetAll_Start.ID, Call_GetAll_Start)
#    obj/CodeGenerator/Python/Call/GetAll.py
#    Created 27/07/2023 at 10:09:57 from:
#        Messages = messages/Call/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Call_GetAll_Processing :
    ID = 24599
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 6), ("Function", 1), ("Operator", 7)])
    ReverseIDs = OrderedDict([(6, "FunctionBlock"), (1, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Call_GetAll_Processing.MSG_OFFSET + Call_GetAll_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Call_GetAll_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Call_GetAll_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Call_GetAll_Processing.MSG_OFFSET + Call_GetAll_Processing.SIZE)
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
            self.hdr.SetMessageID(Call_GetAll_Processing.ID)
            self.hdr.SetDataLength(Call_GetAll_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Call.GetAll.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Call.GetAll.Processing", Call_GetAll_Processing.ID, Call_GetAll_Processing)
#    obj/CodeGenerator/Python/Call/GetAll.py
#    Created 27/07/2023 at 10:09:57 from:
#        Messages = messages/Call/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Call_GetAll_Result :
    ID = 24598
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 6), ("Function", 1), ("Operator", 6)])
    ReverseIDs = OrderedDict([(6, "FunctionBlock"), (1, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Call_GetAll_Result.MSG_OFFSET + Call_GetAll_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Call_GetAll_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Call_GetAll_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Call_GetAll_Result.MSG_OFFSET + Call_GetAll_Result.SIZE)
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
            self.hdr.SetMessageID(Call_GetAll_Result.ID)
            self.hdr.SetDataLength(Call_GetAll_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Call.GetAll.Result"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBusy(self):
        """A busy error will be sent if the product is already processing a response to a GetAll command"""
        value = struct.unpack_from('B', self.rawBuffer(), Call_GetAll_Result.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBusy(self, value):
        """A busy error will be sent if the product is already processing a response to a GetAll command"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Call_GetAll_Result.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Busy",type="int",units="",minVal="0",maxVal="255",description="A busy error will be sent if the product is already processing a response to a GetAll command",get=GetBusy,set=SetBusy,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Call.GetAll.Result", Call_GetAll_Result.ID, Call_GetAll_Result)

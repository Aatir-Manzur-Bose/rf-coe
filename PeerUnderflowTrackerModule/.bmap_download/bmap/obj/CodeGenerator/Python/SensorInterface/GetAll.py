#    obj/CodeGenerator/Python/SensorInterface/GetAll.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_GetAll_Start :
    ID = 98325
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 1), ("Operator", 5)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (1, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_GetAll_Start.MSG_OFFSET + SensorInterface_GetAll_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_GetAll_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_GetAll_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_GetAll_Start.MSG_OFFSET + SensorInterface_GetAll_Start.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_GetAll_Start.ID)
            self.hdr.SetDataLength(SensorInterface_GetAll_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.GetAll.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("SensorInterface.GetAll.Start", SensorInterface_GetAll_Start.ID, SensorInterface_GetAll_Start)
#    obj/CodeGenerator/Python/SensorInterface/GetAll.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_GetAll_Processing :
    ID = 98327
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 1), ("Operator", 7)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (1, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_GetAll_Processing.MSG_OFFSET + SensorInterface_GetAll_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_GetAll_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_GetAll_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_GetAll_Processing.MSG_OFFSET + SensorInterface_GetAll_Processing.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_GetAll_Processing.ID)
            self.hdr.SetDataLength(SensorInterface_GetAll_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.GetAll.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("SensorInterface.GetAll.Processing", SensorInterface_GetAll_Processing.ID, SensorInterface_GetAll_Processing)
#    obj/CodeGenerator/Python/SensorInterface/GetAll.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_GetAll_Result :
    ID = 98326
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 1), ("Operator", 6)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (1, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_GetAll_Result.MSG_OFFSET + SensorInterface_GetAll_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_GetAll_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_GetAll_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_GetAll_Result.MSG_OFFSET + SensorInterface_GetAll_Result.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_GetAll_Result.ID)
            self.hdr.SetDataLength(SensorInterface_GetAll_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.GetAll.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("SensorInterface.GetAll.Result", SensorInterface_GetAll_Result.ID, SensorInterface_GetAll_Result)
#    obj/CodeGenerator/Python/SensorInterface/GetAll.py
#    Created 27/07/2023 at 10:11:03 from:
#        Messages = messages/SensorInterface/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SensorInterface_GetAll_Error :
    ID = 98324
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 24), ("Function", 1), ("Operator", 4)])
    ReverseIDs = OrderedDict([(24, "FunctionBlock"), (1, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SensorInterface_GetAll_Error.MSG_OFFSET + SensorInterface_GetAll_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SensorInterface_GetAll_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SensorInterface_GetAll_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SensorInterface_GetAll_Error.MSG_OFFSET + SensorInterface_GetAll_Error.SIZE)
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
            self.hdr.SetMessageID(SensorInterface_GetAll_Error.ID)
            self.hdr.SetDataLength(SensorInterface_GetAll_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SensorInterface.GetAll.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), SensorInterface_GetAll_Error.MSG_OFFSET + 0)[0]
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
        struct.pack_into('B', self.rawBuffer(), SensorInterface_GetAll_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Busy",type="int",units="",minVal="0",maxVal="255",description="A busy error will be sent if the product is already processing a response to a GetAll command",get=GetBusy,set=SetBusy,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SensorInterface.GetAll.Error", SensorInterface_GetAll_Error.ID, SensorInterface_GetAll_Error)

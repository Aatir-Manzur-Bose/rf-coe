#    obj/CodeGenerator/Python/Experimental/TaylorRequest.py
#    Created 27/07/2023 at 10:10:42 from:
#        Messages = messages/Experimental/TaylorRequest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_TaylorRequest_Set :
    ID = 78848
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 64), ("Operator", 0)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (64, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Set.MSG_OFFSET + Experimental_TaylorRequest_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_TaylorRequest_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_TaylorRequest_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Set.MSG_OFFSET + Experimental_TaylorRequest_Set.SIZE)
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
            self.hdr.SetMessageID(Experimental_TaylorRequest_Set.ID)
            self.hdr.SetDataLength(Experimental_TaylorRequest_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.TaylorRequest.Set"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetTaySeqNo(self):
        """Rolling Sequence Number"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_TaylorRequest_Set.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetTaylorPayload(self):
        """Payload data, variable length"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_TaylorRequest_Set.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetTaySeqNo(self, value):
        """Rolling Sequence Number"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_TaylorRequest_Set.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetTaylorPayload(self, value):
        """Payload data, variable length"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_TaylorRequest_Set.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TaySeqNo",type="int",units="",minVal="0",maxVal="255",description="Rolling Sequence Number",get=GetTaySeqNo,set=SetTaySeqNo,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="TaylorPayload",type="int",units="",minVal="0",maxVal="255",description="Payload data, variable length",get=GetTaylorPayload,set=SetTaylorPayload,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Experimental.TaylorRequest.Set", Experimental_TaylorRequest_Set.ID, Experimental_TaylorRequest_Set)
#    obj/CodeGenerator/Python/Experimental/TaylorRequest.py
#    Created 27/07/2023 at 10:10:42 from:
#        Messages = messages/Experimental/TaylorRequest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_TaylorRequest_Start :
    ID = 78853
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 64), ("Operator", 5)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (64, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Start.MSG_OFFSET + Experimental_TaylorRequest_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_TaylorRequest_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_TaylorRequest_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Start.MSG_OFFSET + Experimental_TaylorRequest_Start.SIZE)
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
            self.hdr.SetMessageID(Experimental_TaylorRequest_Start.ID)
            self.hdr.SetDataLength(Experimental_TaylorRequest_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.TaylorRequest.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Experimental.TaylorRequest.Start", Experimental_TaylorRequest_Start.ID, Experimental_TaylorRequest_Start)
#    obj/CodeGenerator/Python/Experimental/TaylorRequest.py
#    Created 27/07/2023 at 10:10:42 from:
#        Messages = messages/Experimental/TaylorRequest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_TaylorRequest_Status :
    ID = 78851
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 64), ("Operator", 3)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (64, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Status.MSG_OFFSET + Experimental_TaylorRequest_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_TaylorRequest_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_TaylorRequest_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Status.MSG_OFFSET + Experimental_TaylorRequest_Status.SIZE)
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
            self.hdr.SetMessageID(Experimental_TaylorRequest_Status.ID)
            self.hdr.SetDataLength(Experimental_TaylorRequest_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.TaylorRequest.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetTaySeqNo(self):
        """Rolling Sequence Number"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_TaylorRequest_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetFrontDoorPayload(self):
        """Payload response data from FrontDoor, variable length"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_TaylorRequest_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetTaySeqNo(self, value):
        """Rolling Sequence Number"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_TaylorRequest_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetFrontDoorPayload(self, value):
        """Payload response data from FrontDoor, variable length"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_TaylorRequest_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TaySeqNo",type="int",units="",minVal="0",maxVal="255",description="Rolling Sequence Number",get=GetTaySeqNo,set=SetTaySeqNo,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FrontDoorPayload",type="int",units="",minVal="0",maxVal="255",description="Payload response data from FrontDoor, variable length",get=GetFrontDoorPayload,set=SetFrontDoorPayload,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Experimental.TaylorRequest.Status", Experimental_TaylorRequest_Status.ID, Experimental_TaylorRequest_Status)
#    obj/CodeGenerator/Python/Experimental/TaylorRequest.py
#    Created 27/07/2023 at 10:10:42 from:
#        Messages = messages/Experimental/TaylorRequest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_TaylorRequest_Result :
    ID = 78854
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 64), ("Operator", 6)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (64, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Result.MSG_OFFSET + Experimental_TaylorRequest_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_TaylorRequest_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_TaylorRequest_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Result.MSG_OFFSET + Experimental_TaylorRequest_Result.SIZE)
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
            self.hdr.SetMessageID(Experimental_TaylorRequest_Result.ID)
            self.hdr.SetDataLength(Experimental_TaylorRequest_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.TaylorRequest.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Experimental.TaylorRequest.Result", Experimental_TaylorRequest_Result.ID, Experimental_TaylorRequest_Result)
#    obj/CodeGenerator/Python/Experimental/TaylorRequest.py
#    Created 27/07/2023 at 10:10:42 from:
#        Messages = messages/Experimental/TaylorRequest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_TaylorRequest_Processing :
    ID = 78855
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 64), ("Operator", 7)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (64, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Processing.MSG_OFFSET + Experimental_TaylorRequest_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_TaylorRequest_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_TaylorRequest_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_TaylorRequest_Processing.MSG_OFFSET + Experimental_TaylorRequest_Processing.SIZE)
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
            self.hdr.SetMessageID(Experimental_TaylorRequest_Processing.ID)
            self.hdr.SetDataLength(Experimental_TaylorRequest_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.TaylorRequest.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Experimental.TaylorRequest.Processing", Experimental_TaylorRequest_Processing.ID, Experimental_TaylorRequest_Processing)

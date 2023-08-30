#    obj/CodeGenerator/Python/Debug/GetAll.py
#    Created 27/07/2023 at 10:10:12 from:
#        Messages = messages/Debug/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_GetAll_Start :
    ID = 32789
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 1), ("Operator", 5)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (1, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_GetAll_Start.MSG_OFFSET + Debug_GetAll_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_GetAll_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_GetAll_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_GetAll_Start.MSG_OFFSET + Debug_GetAll_Start.SIZE)
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
            self.hdr.SetMessageID(Debug_GetAll_Start.ID)
            self.hdr.SetDataLength(Debug_GetAll_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.GetAll.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.GetAll.Start", Debug_GetAll_Start.ID, Debug_GetAll_Start)
#    obj/CodeGenerator/Python/Debug/GetAll.py
#    Created 27/07/2023 at 10:10:12 from:
#        Messages = messages/Debug/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_GetAll_Processing :
    ID = 32791
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 1), ("Operator", 7)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (1, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_GetAll_Processing.MSG_OFFSET + Debug_GetAll_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_GetAll_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_GetAll_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_GetAll_Processing.MSG_OFFSET + Debug_GetAll_Processing.SIZE)
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
            self.hdr.SetMessageID(Debug_GetAll_Processing.ID)
            self.hdr.SetDataLength(Debug_GetAll_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.GetAll.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.GetAll.Processing", Debug_GetAll_Processing.ID, Debug_GetAll_Processing)
#    obj/CodeGenerator/Python/Debug/GetAll.py
#    Created 27/07/2023 at 10:10:12 from:
#        Messages = messages/Debug/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_GetAll_Result :
    ID = 32790
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 1), ("Operator", 6)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (1, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_GetAll_Result.MSG_OFFSET + Debug_GetAll_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_GetAll_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_GetAll_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_GetAll_Result.MSG_OFFSET + Debug_GetAll_Result.SIZE)
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
            self.hdr.SetMessageID(Debug_GetAll_Result.ID)
            self.hdr.SetDataLength(Debug_GetAll_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.GetAll.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.GetAll.Result", Debug_GetAll_Result.ID, Debug_GetAll_Result)
#    obj/CodeGenerator/Python/Debug/GetAll.py
#    Created 27/07/2023 at 10:10:12 from:
#        Messages = messages/Debug/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_GetAll_Get :
    ID = 32785
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 1), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (1, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_GetAll_Get.MSG_OFFSET + Debug_GetAll_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_GetAll_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_GetAll_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_GetAll_Get.MSG_OFFSET + Debug_GetAll_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_GetAll_Get.ID)
            self.hdr.SetDataLength(Debug_GetAll_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.GetAll.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.GetAll.Get", Debug_GetAll_Get.ID, Debug_GetAll_Get)
#    obj/CodeGenerator/Python/Debug/GetAll.py
#    Created 27/07/2023 at 10:10:12 from:
#        Messages = messages/Debug/GetAll.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_GetAll_Status :
    ID = 32787
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 1), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (1, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_GetAll_Status.MSG_OFFSET + Debug_GetAll_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_GetAll_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_GetAll_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_GetAll_Status.MSG_OFFSET + Debug_GetAll_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_GetAll_Status.ID)
            self.hdr.SetDataLength(Debug_GetAll_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.GetAll.Status"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.GetAll.Status", Debug_GetAll_Status.ID, Debug_GetAll_Status)

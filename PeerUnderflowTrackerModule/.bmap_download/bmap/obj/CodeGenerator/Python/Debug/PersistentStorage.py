#    obj/CodeGenerator/Python/Debug/PersistentStorage.py
#    Created 27/07/2023 at 10:10:14 from:
#        Messages = messages/Debug/PersistentStorage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_PersistentStorage_Start :
    ID = 33461
    SIZE = 255
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    StorageOperations = OrderedDict([("StorageRead", 0), ("StorageWrite", 1)])
    ReverseStorageOperations = OrderedDict([(0, "StorageRead"), (1, "StorageWrite")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 43), ("Operator", 5)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (43, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_PersistentStorage_Start.MSG_OFFSET + Debug_PersistentStorage_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_PersistentStorage_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_PersistentStorage_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_PersistentStorage_Start.MSG_OFFSET + Debug_PersistentStorage_Start.SIZE)
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
            self.hdr.SetMessageID(Debug_PersistentStorage_Start.ID)
            self.hdr.SetDataLength(Debug_PersistentStorage_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.PersistentStorage.Start"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetStorageOperation(self, enumAsInt=0):
        """Operation to perform with specified address"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_PersistentStorage_Start.ReverseStorageOperations.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(4)
    def GetAddress(self, idx):
        """Address to access"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 1+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(250)
    def GetOperationPayload(self, idx):
        """Payload for persistent storage operation"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 5+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetStorageOperation(self, value):
        """Operation to perform with specified address"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_PersistentStorage_Start.StorageOperations.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(4)
    def SetAddress(self, value, idx):
        """Address to access"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 1+idx*1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(250)
    def SetOperationPayload(self, value, idx):
        """Payload for persistent storage operation"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_PersistentStorage_Start.MSG_OFFSET + 5+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="StorageOperation",type="enumeration",units="",minVal="0",maxVal="255",description="Operation to perform with specified address",get=GetStorageOperation,set=SetStorageOperation,count=1, bitfieldInfo = [], enum = [StorageOperations, ReverseStorageOperations]),\
        FieldInfo(name="Address",type="int",units="",minVal="0",maxVal="255",description="Address to access",get=GetAddress,set=SetAddress,count=4, bitfieldInfo = [], enum = []),\
        FieldInfo(name="OperationPayload",type="int",units="",minVal="0",maxVal="255",description="Payload for persistent storage operation",get=GetOperationPayload,set=SetOperationPayload,count=250, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.PersistentStorage.Start", Debug_PersistentStorage_Start.ID, Debug_PersistentStorage_Start)
#    obj/CodeGenerator/Python/Debug/PersistentStorage.py
#    Created 27/07/2023 at 10:10:14 from:
#        Messages = messages/Debug/PersistentStorage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_PersistentStorage_Processing :
    ID = 33463
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 43), ("Operator", 7)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (43, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_PersistentStorage_Processing.MSG_OFFSET + Debug_PersistentStorage_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_PersistentStorage_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_PersistentStorage_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_PersistentStorage_Processing.MSG_OFFSET + Debug_PersistentStorage_Processing.SIZE)
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
            self.hdr.SetMessageID(Debug_PersistentStorage_Processing.ID)
            self.hdr.SetDataLength(Debug_PersistentStorage_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.PersistentStorage.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.PersistentStorage.Processing", Debug_PersistentStorage_Processing.ID, Debug_PersistentStorage_Processing)
#    obj/CodeGenerator/Python/Debug/PersistentStorage.py
#    Created 27/07/2023 at 10:10:14 from:
#        Messages = messages/Debug/PersistentStorage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_PersistentStorage_Result :
    ID = 33462
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 43), ("Operator", 6)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (43, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_PersistentStorage_Result.MSG_OFFSET + Debug_PersistentStorage_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_PersistentStorage_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_PersistentStorage_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_PersistentStorage_Result.MSG_OFFSET + Debug_PersistentStorage_Result.SIZE)
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
            self.hdr.SetMessageID(Debug_PersistentStorage_Result.ID)
            self.hdr.SetDataLength(Debug_PersistentStorage_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.PersistentStorage.Result"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetResponse(self):
        """Result of persisent storage operation, dependent on operational"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_PersistentStorage_Result.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetResponse(self, value):
        """Result of persisent storage operation, dependent on operational"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_PersistentStorage_Result.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Response",type="int",units="",minVal="0",maxVal="255",description="Result of persisent storage operation, dependent on operational",get=GetResponse,set=SetResponse,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.PersistentStorage.Result", Debug_PersistentStorage_Result.ID, Debug_PersistentStorage_Result)

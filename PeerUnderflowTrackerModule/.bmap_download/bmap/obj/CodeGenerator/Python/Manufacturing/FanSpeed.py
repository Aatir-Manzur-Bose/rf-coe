#    obj/CodeGenerator/Python/Manufacturing/FanSpeed.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/FanSpeed.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_FanSpeed_SetGet :
    ID = 94530
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 20), ("Operator", 2)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (20, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_SetGet.MSG_OFFSET + Manufacturing_FanSpeed_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_FanSpeed_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_FanSpeed_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_SetGet.MSG_OFFSET + Manufacturing_FanSpeed_SetGet.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_FanSpeed_SetGet.ID)
            self.hdr.SetDataLength(Manufacturing_FanSpeed_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.FanSpeed.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSpeed(self):
        """Fan speed in steps."""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_FanSpeed_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSpeed(self, value):
        """Fan speed in steps."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_FanSpeed_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Speed",type="int",units="",minVal="0",maxVal="255",description="Fan speed in steps.",get=GetSpeed,set=SetSpeed,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.FanSpeed.SetGet", Manufacturing_FanSpeed_SetGet.ID, Manufacturing_FanSpeed_SetGet)
#    obj/CodeGenerator/Python/Manufacturing/FanSpeed.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/FanSpeed.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_FanSpeed_Get :
    ID = 94529
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 20), ("Operator", 1)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (20, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_Get.MSG_OFFSET + Manufacturing_FanSpeed_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_FanSpeed_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_FanSpeed_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_Get.MSG_OFFSET + Manufacturing_FanSpeed_Get.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_FanSpeed_Get.ID)
            self.hdr.SetDataLength(Manufacturing_FanSpeed_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.FanSpeed.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Manufacturing.FanSpeed.Get", Manufacturing_FanSpeed_Get.ID, Manufacturing_FanSpeed_Get)
#    obj/CodeGenerator/Python/Manufacturing/FanSpeed.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/FanSpeed.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_FanSpeed_Status :
    ID = 94531
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 20), ("Operator", 3)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (20, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_Status.MSG_OFFSET + Manufacturing_FanSpeed_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_FanSpeed_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_FanSpeed_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_FanSpeed_Status.MSG_OFFSET + Manufacturing_FanSpeed_Status.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_FanSpeed_Status.ID)
            self.hdr.SetDataLength(Manufacturing_FanSpeed_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.FanSpeed.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSpeed(self):
        """The current fan speed step."""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_FanSpeed_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetSteps(self):
        """The total number of fan speed steps."""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_FanSpeed_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSpeed(self, value):
        """The current fan speed step."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_FanSpeed_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetSteps(self, value):
        """The total number of fan speed steps."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_FanSpeed_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Speed",type="int",units="",minVal="0",maxVal="255",description="The current fan speed step.",get=GetSpeed,set=SetSpeed,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Steps",type="int",units="",minVal="0",maxVal="255",description="The total number of fan speed steps.",get=GetSteps,set=SetSteps,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.FanSpeed.Status", Manufacturing_FanSpeed_Status.ID, Manufacturing_FanSpeed_Status)

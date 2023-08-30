#    obj/CodeGenerator/Python/BatteryDebug/SOCPercentage.py
#    Created 27/07/2023 at 10:09:53 from:
#        Messages = messages/BatteryDebug/SOCPercentage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_SOCPercentage_Get :
    ID = 102593
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 12), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (12, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_Get.MSG_OFFSET + BatteryDebug_SOCPercentage_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_SOCPercentage_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_SOCPercentage_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_Get.MSG_OFFSET + BatteryDebug_SOCPercentage_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_SOCPercentage_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_SOCPercentage_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.SOCPercentage.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.SOCPercentage.Get", BatteryDebug_SOCPercentage_Get.ID, BatteryDebug_SOCPercentage_Get)
#    obj/CodeGenerator/Python/BatteryDebug/SOCPercentage.py
#    Created 27/07/2023 at 10:09:53 from:
#        Messages = messages/BatteryDebug/SOCPercentage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_SOCPercentage_SetGet :
    ID = 102594
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 12), ("Operator", 2)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (12, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_SetGet.MSG_OFFSET + BatteryDebug_SOCPercentage_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_SOCPercentage_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_SOCPercentage_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_SetGet.MSG_OFFSET + BatteryDebug_SOCPercentage_SetGet.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_SOCPercentage_SetGet.ID)
            self.hdr.SetDataLength(BatteryDebug_SOCPercentage_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.SOCPercentage.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSOCPercentage(self):
        """State of charge percentage"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_SOCPercentage_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSOCPercentage(self, value):
        """State of charge percentage"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_SOCPercentage_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SOCPercentage",type="int",units="",minVal="0",maxVal="255",description="State of charge percentage",get=GetSOCPercentage,set=SetSOCPercentage,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.SOCPercentage.SetGet", BatteryDebug_SOCPercentage_SetGet.ID, BatteryDebug_SOCPercentage_SetGet)
#    obj/CodeGenerator/Python/BatteryDebug/SOCPercentage.py
#    Created 27/07/2023 at 10:09:53 from:
#        Messages = messages/BatteryDebug/SOCPercentage.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_SOCPercentage_Status :
    ID = 102595
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 12), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (12, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_Status.MSG_OFFSET + BatteryDebug_SOCPercentage_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_SOCPercentage_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_SOCPercentage_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_SOCPercentage_Status.MSG_OFFSET + BatteryDebug_SOCPercentage_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_SOCPercentage_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_SOCPercentage_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.SOCPercentage.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSOCPercentage(self):
        """State of charge percentage"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_SOCPercentage_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSOCPercentage(self, value):
        """State of charge percentage"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_SOCPercentage_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SOCPercentage",type="int",units="",minVal="0",maxVal="255",description="State of charge percentage",get=GetSOCPercentage,set=SetSOCPercentage,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.SOCPercentage.Status", BatteryDebug_SOCPercentage_Status.ID, BatteryDebug_SOCPercentage_Status)

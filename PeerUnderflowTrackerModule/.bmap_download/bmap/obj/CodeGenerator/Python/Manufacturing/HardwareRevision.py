#    obj/CodeGenerator/Python/Manufacturing/HardwareRevision.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/HardwareRevision.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_HardwareRevision_Get :
    ID = 94625
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 26), ("Operator", 1)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (26, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_Get.MSG_OFFSET + Manufacturing_HardwareRevision_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_HardwareRevision_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_HardwareRevision_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_Get.MSG_OFFSET + Manufacturing_HardwareRevision_Get.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_HardwareRevision_Get.ID)
            self.hdr.SetDataLength(Manufacturing_HardwareRevision_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.HardwareRevision.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Manufacturing.HardwareRevision.Get", Manufacturing_HardwareRevision_Get.ID, Manufacturing_HardwareRevision_Get)
#    obj/CodeGenerator/Python/Manufacturing/HardwareRevision.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/HardwareRevision.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_HardwareRevision_Status :
    ID = 94627
    SIZE = 8
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 26), ("Operator", 3)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (26, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_Status.MSG_OFFSET + Manufacturing_HardwareRevision_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_HardwareRevision_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_HardwareRevision_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_Status.MSG_OFFSET + Manufacturing_HardwareRevision_Status.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_HardwareRevision_Status.ID)
            self.hdr.SetDataLength(Manufacturing_HardwareRevision_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.HardwareRevision.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(8)
    def GetHWRevision(self):
        """Hardware Revision for product (UTF-8 String)"""
        count = 8
        if count > len(self.rawBuffer())-(Manufacturing_HardwareRevision_Status.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(Manufacturing_HardwareRevision_Status.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Manufacturing_HardwareRevision_Status.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(8)
    def SetHWRevision(self, value):
        """Hardware Revision for product (UTF-8 String)"""
        tmp = value.encode('utf-8')
        struct.pack_into('8s', self.rawBuffer(), Manufacturing_HardwareRevision_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="HWRevision",type="string",units="ASCII",minVal="0",maxVal="255",description="Hardware Revision for product (UTF-8 String)",get=GetHWRevision,set=SetHWRevision,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.HardwareRevision.Status", Manufacturing_HardwareRevision_Status.ID, Manufacturing_HardwareRevision_Status)
#    obj/CodeGenerator/Python/Manufacturing/HardwareRevision.py
#    Created 27/07/2023 at 10:10:52 from:
#        Messages = messages/Manufacturing/HardwareRevision.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_HardwareRevision_SetGet :
    ID = 94626
    SIZE = 8
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 26), ("Operator", 2)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (26, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + Manufacturing_HardwareRevision_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_HardwareRevision_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_HardwareRevision_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + Manufacturing_HardwareRevision_SetGet.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_HardwareRevision_SetGet.ID)
            self.hdr.SetDataLength(Manufacturing_HardwareRevision_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.HardwareRevision.SetGet"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(8)
    def GetHWRevision(self):
        """Hardware Revision for product (UTF-8 string)."""
        count = 8
        if count > len(self.rawBuffer())-(Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(8)
    def SetHWRevision(self, value):
        """Hardware Revision for product (UTF-8 string)."""
        tmp = value.encode('utf-8')
        struct.pack_into('8s', self.rawBuffer(), Manufacturing_HardwareRevision_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="HWRevision",type="string",units="ASCII",minVal="0",maxVal="255",description="Hardware Revision for product (UTF-8 string).",get=GetHWRevision,set=SetHWRevision,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.HardwareRevision.SetGet", Manufacturing_HardwareRevision_SetGet.ID, Manufacturing_HardwareRevision_SetGet)

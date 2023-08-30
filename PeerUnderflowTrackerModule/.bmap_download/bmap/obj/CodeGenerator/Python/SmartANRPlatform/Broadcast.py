#    obj/CodeGenerator/Python/SmartANRPlatform/Broadcast.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/Broadcast.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_Broadcast_Get :
    ID = 106945
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 28), ("Operator", 1)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (28, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Get.MSG_OFFSET + SmartANRPlatform_Broadcast_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_Broadcast_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_Broadcast_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Get.MSG_OFFSET + SmartANRPlatform_Broadcast_Get.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_Broadcast_Get.ID)
            self.hdr.SetDataLength(SmartANRPlatform_Broadcast_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.Broadcast.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def Getignored(self):
        """Pypolycomm bug workaround, need at least one field"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def Setignored(self, value):
        """Pypolycomm bug workaround, need at least one field"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ignored",type="int",units="",minVal="0",maxVal="255",description="Pypolycomm bug workaround, need at least one field",get=Getignored,set=Setignored,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.Broadcast.Get", SmartANRPlatform_Broadcast_Get.ID, SmartANRPlatform_Broadcast_Get)
#    obj/CodeGenerator/Python/SmartANRPlatform/Broadcast.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/Broadcast.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_Broadcast_Status :
    ID = 106947
    SIZE = 17
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 28), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (28, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Status.MSG_OFFSET + SmartANRPlatform_Broadcast_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_Broadcast_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_Broadcast_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Status.MSG_OFFSET + SmartANRPlatform_Broadcast_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_Broadcast_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_Broadcast_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.Broadcast.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def Getbytecnt(self):
        """how many bytes of payload"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(16)
    def Getdata(self, idx):
        """payload of broadcast message"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Status.MSG_OFFSET + 1+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def Setbytecnt(self, value):
        """how many bytes of payload"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(16)
    def Setdata(self, value, idx):
        """payload of broadcast message"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Status.MSG_OFFSET + 1+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="bytecnt",type="int",units="",minVal="0",maxVal="255",description="how many bytes of payload",get=Getbytecnt,set=Setbytecnt,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="data",type="int",units="",minVal="0",maxVal="255",description="payload of broadcast message",get=Getdata,set=Setdata,count=16, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.Broadcast.Status", SmartANRPlatform_Broadcast_Status.ID, SmartANRPlatform_Broadcast_Status)
#    obj/CodeGenerator/Python/SmartANRPlatform/Broadcast.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/Broadcast.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_Broadcast_Error :
    ID = 106948
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SmartANRPlatformErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("InvalidData", 3), ("RunTime", 4), ("Timeout", 5), ("InvalidState", 6), ("Verify", 7)])
    ReverseSmartANRPlatformErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "InvalidData"), (4, "RunTime"), (5, "Timeout"), (6, "InvalidState"), (7, "Verify")])
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 28), ("Operator", 4)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (28, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Error.MSG_OFFSET + SmartANRPlatform_Broadcast_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_Broadcast_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_Broadcast_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_Broadcast_Error.MSG_OFFSET + SmartANRPlatform_Broadcast_Error.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_Broadcast_Error.ID)
            self.hdr.SetDataLength(SmartANRPlatform_Broadcast_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.Broadcast.Error"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetErrorCode(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SmartANRPlatform_Broadcast_Error.ReverseSmartANRPlatformErrorResponseCodes.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetErrorCode(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SmartANRPlatform_Broadcast_Error.SmartANRPlatformErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_Broadcast_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [SmartANRPlatformErrorResponseCodes, ReverseSmartANRPlatformErrorResponseCodes])\
    ]

Messaging.Register("SmartANRPlatform.Broadcast.Error", SmartANRPlatform_Broadcast_Error.ID, SmartANRPlatform_Broadcast_Error)

#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggleSafe.py
#    Created 27/07/2023 at 10:11:15 from:
#        Messages = messages/SmartANRPlatform/MixerToggleSafe.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggleSafe_SetGet :
    ID = 107154
    SIZE = 125
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 41), ("Operator", 2)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (41, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggleSafe_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggleSafe_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_SetGet.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggleSafe_SetGet.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggleSafe_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggleSafe.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBSCID(self):
        """ID of BSC to access"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(120)
    def GetMixerName(self):
        """The name of the mixer"""
        count = 120
        if count > len(self.rawBuffer())-(SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 1):
            count = len(self.rawBuffer())-(SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 1)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 1)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('121')
    @msg.size('1')
    @msg.count(4)
    def GetToggleArray(self, idx):
        """4 mixer paths state (1 = enabled, 0 = disabled)."""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 121+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBSCID(self, value):
        """ID of BSC to access"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(120)
    def SetMixerName(self, value):
        """The name of the mixer"""
        tmp = value.encode('utf-8')
        struct.pack_into('120s', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('121')
    @msg.size('1')
    @msg.count(4)
    def SetToggleArray(self, value, idx):
        """4 mixer paths state (1 = enabled, 0 = disabled)."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_SetGet.MSG_OFFSET + 121+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MixerName",type="string",units="ASCII",minVal="0",maxVal="255",description="The name of the mixer",get=GetMixerName,set=SetMixerName,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ToggleArray",type="int",units="",minVal="0",maxVal="255",description="4 mixer paths state (1 = enabled, 0 = disabled).",get=GetToggleArray,set=SetToggleArray,count=4, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggleSafe.SetGet", SmartANRPlatform_MixerToggleSafe_SetGet.ID, SmartANRPlatform_MixerToggleSafe_SetGet)
#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggleSafe.py
#    Created 27/07/2023 at 10:11:15 from:
#        Messages = messages/SmartANRPlatform/MixerToggleSafe.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggleSafe_Status :
    ID = 107155
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 41), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (41, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_Status.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggleSafe_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggleSafe_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_Status.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggleSafe_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggleSafe_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggleSafe.Status"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("SmartANRPlatform.MixerToggleSafe.Status", SmartANRPlatform_MixerToggleSafe_Status.ID, SmartANRPlatform_MixerToggleSafe_Status)
#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggleSafe.py
#    Created 27/07/2023 at 10:11:15 from:
#        Messages = messages/SmartANRPlatform/MixerToggleSafe.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggleSafe_Error :
    ID = 107156
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SmartANRPlatformErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("InvalidData", 3), ("RunTime", 4), ("Timeout", 5), ("InvalidState", 6), ("Verify", 7)])
    ReverseSmartANRPlatformErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "InvalidData"), (4, "RunTime"), (5, "Timeout"), (6, "InvalidState"), (7, "Verify")])
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 41), ("Operator", 4)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (41, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_Error.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggleSafe_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggleSafe_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggleSafe_Error.MSG_OFFSET + SmartANRPlatform_MixerToggleSafe_Error.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggleSafe_Error.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggleSafe_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggleSafe.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SmartANRPlatform_MixerToggleSafe_Error.ReverseSmartANRPlatformErrorResponseCodes.get(value, value)
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
        value = SmartANRPlatform_MixerToggleSafe_Error.SmartANRPlatformErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggleSafe_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [SmartANRPlatformErrorResponseCodes, ReverseSmartANRPlatformErrorResponseCodes])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggleSafe.Error", SmartANRPlatform_MixerToggleSafe_Error.ID, SmartANRPlatform_MixerToggleSafe_Error)

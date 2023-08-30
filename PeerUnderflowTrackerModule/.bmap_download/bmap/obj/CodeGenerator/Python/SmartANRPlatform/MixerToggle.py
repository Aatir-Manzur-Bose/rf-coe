#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggle.py
#    Created 27/07/2023 at 10:11:14 from:
#        Messages = messages/SmartANRPlatform/MixerToggle.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggle_Get :
    ID = 107137
    SIZE = 122
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 40), ("Operator", 1)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (40, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + SmartANRPlatform_MixerToggle_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggle_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggle_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + SmartANRPlatform_MixerToggle_Get.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggle_Get.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggle_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggle.Get"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetBankNum(self):
        """Bank Number (0, 1, 2)"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(120)
    def GetMixerName(self):
        """The name of the mixer"""
        count = 120
        if count > len(self.rawBuffer())-(SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 2):
            count = len(self.rawBuffer())-(SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 2)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 2)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
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
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetBankNum(self, value):
        """Bank Number (0, 1, 2)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 1, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(120)
    def SetMixerName(self, value):
        """The name of the mixer"""
        tmp = value.encode('utf-8')
        struct.pack_into('120s', self.rawBuffer(), SmartANRPlatform_MixerToggle_Get.MSG_OFFSET + 2, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Bank Number (0, 1, 2)",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MixerName",type="string",units="ASCII",minVal="0",maxVal="255",description="The name of the mixer",get=GetMixerName,set=SetMixerName,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggle.Get", SmartANRPlatform_MixerToggle_Get.ID, SmartANRPlatform_MixerToggle_Get)
#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggle.py
#    Created 27/07/2023 at 10:11:14 from:
#        Messages = messages/SmartANRPlatform/MixerToggle.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggle_SetGet :
    ID = 107138
    SIZE = 126
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 40), ("Operator", 2)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (40, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + SmartANRPlatform_MixerToggle_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggle_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggle_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + SmartANRPlatform_MixerToggle_SetGet.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggle_SetGet.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggle_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggle.SetGet"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetBankNum(self):
        """Bank Number (0, 1, 2)"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(120)
    def GetMixerName(self):
        """The name of the mixer"""
        count = 120
        if count > len(self.rawBuffer())-(SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 2):
            count = len(self.rawBuffer())-(SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 2)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 2)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('122')
    @msg.size('1')
    @msg.count(4)
    def GetToggleArray(self, idx):
        """4 mixer paths state (1 = enabled, 0 = disabled)."""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 122+idx*1)[0]
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
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetBankNum(self, value):
        """Bank Number (0, 1, 2)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(120)
    def SetMixerName(self, value):
        """The name of the mixer"""
        tmp = value.encode('utf-8')
        struct.pack_into('120s', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('122')
    @msg.size('1')
    @msg.count(4)
    def SetToggleArray(self, value, idx):
        """4 mixer paths state (1 = enabled, 0 = disabled)."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_SetGet.MSG_OFFSET + 122+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Bank Number (0, 1, 2)",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MixerName",type="string",units="ASCII",minVal="0",maxVal="255",description="The name of the mixer",get=GetMixerName,set=SetMixerName,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ToggleArray",type="int",units="",minVal="0",maxVal="255",description="4 mixer paths state (1 = enabled, 0 = disabled).",get=GetToggleArray,set=SetToggleArray,count=4, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggle.SetGet", SmartANRPlatform_MixerToggle_SetGet.ID, SmartANRPlatform_MixerToggle_SetGet)
#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggle.py
#    Created 27/07/2023 at 10:11:14 from:
#        Messages = messages/SmartANRPlatform/MixerToggle.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggle_Status :
    ID = 107139
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 40), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (40, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Status.MSG_OFFSET + SmartANRPlatform_MixerToggle_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggle_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggle_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Status.MSG_OFFSET + SmartANRPlatform_MixerToggle_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggle_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggle_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggle.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(4)
    def GetToggleArray(self, idx):
        """Mixer paths status."""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Status.MSG_OFFSET + 0+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(4)
    def SetToggleArray(self, value, idx):
        """Mixer paths status."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Status.MSG_OFFSET + 0+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ToggleArray",type="int",units="",minVal="0",maxVal="255",description="Mixer paths status.",get=GetToggleArray,set=SetToggleArray,count=4, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggle.Status", SmartANRPlatform_MixerToggle_Status.ID, SmartANRPlatform_MixerToggle_Status)
#    obj/CodeGenerator/Python/SmartANRPlatform/MixerToggle.py
#    Created 27/07/2023 at 10:11:14 from:
#        Messages = messages/SmartANRPlatform/MixerToggle.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_MixerToggle_Error :
    ID = 107140
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SmartANRPlatformErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("InvalidData", 3), ("RunTime", 4), ("Timeout", 5), ("InvalidState", 6), ("Verify", 7)])
    ReverseSmartANRPlatformErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "InvalidData"), (4, "RunTime"), (5, "Timeout"), (6, "InvalidState"), (7, "Verify")])
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 40), ("Operator", 4)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (40, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Error.MSG_OFFSET + SmartANRPlatform_MixerToggle_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_MixerToggle_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_MixerToggle_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_MixerToggle_Error.MSG_OFFSET + SmartANRPlatform_MixerToggle_Error.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_MixerToggle_Error.ID)
            self.hdr.SetDataLength(SmartANRPlatform_MixerToggle_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.MixerToggle.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SmartANRPlatform_MixerToggle_Error.ReverseSmartANRPlatformErrorResponseCodes.get(value, value)
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
        value = SmartANRPlatform_MixerToggle_Error.SmartANRPlatformErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_MixerToggle_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [SmartANRPlatformErrorResponseCodes, ReverseSmartANRPlatformErrorResponseCodes])\
    ]

Messaging.Register("SmartANRPlatform.MixerToggle.Error", SmartANRPlatform_MixerToggle_Error.ID, SmartANRPlatform_MixerToggle_Error)

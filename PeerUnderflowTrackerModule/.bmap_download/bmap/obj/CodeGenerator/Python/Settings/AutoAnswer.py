#    obj/CodeGenerator/Python/Settings/AutoAnswer.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/Settings/AutoAnswer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Settings_AutoAnswer_Get :
    ID = 4529
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 1), ("Function", 27), ("Operator", 1)])
    ReverseIDs = OrderedDict([(1, "FunctionBlock"), (27, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Settings_AutoAnswer_Get.MSG_OFFSET + Settings_AutoAnswer_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Settings_AutoAnswer_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Settings_AutoAnswer_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Settings_AutoAnswer_Get.MSG_OFFSET + Settings_AutoAnswer_Get.SIZE)
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
            self.hdr.SetMessageID(Settings_AutoAnswer_Get.ID)
            self.hdr.SetDataLength(Settings_AutoAnswer_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Settings.AutoAnswer.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Settings.AutoAnswer.Get", Settings_AutoAnswer_Get.ID, Settings_AutoAnswer_Get)
#    obj/CodeGenerator/Python/Settings/AutoAnswer.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/Settings/AutoAnswer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Settings_AutoAnswer_SetGet :
    ID = 4530
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 1), ("Function", 27), ("Operator", 2)])
    ReverseIDs = OrderedDict([(1, "FunctionBlock"), (27, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Settings_AutoAnswer_SetGet.MSG_OFFSET + Settings_AutoAnswer_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Settings_AutoAnswer_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Settings_AutoAnswer_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Settings_AutoAnswer_SetGet.MSG_OFFSET + Settings_AutoAnswer_SetGet.SIZE)
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
            self.hdr.SetMessageID(Settings_AutoAnswer_SetGet.ID)
            self.hdr.SetDataLength(Settings_AutoAnswer_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Settings.AutoAnswer.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetContainer(self):
        """AutoAnswer setting"""
        value = struct.unpack_from('B', self.rawBuffer(), Settings_AutoAnswer_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAutoAnswer(self):
        """Enable AutoAnswer (0 == disable, 1 == enable)"""
        value = (self.GetContainer() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetUnusedAutoAnswerSetGet(self):
        """Unused, ignored"""
        value = (self.GetContainer() >> 1) & 0x7f
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetContainer(self, value):
        """AutoAnswer setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Settings_AutoAnswer_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAutoAnswer(self, value):
        """Enable AutoAnswer (0 == disable, 1 == enable)"""
        tmp = min(max(value, 0), 1)
        self.SetContainer((self.GetContainer() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetUnusedAutoAnswerSetGet(self, value):
        """Unused, ignored"""
        tmp = min(max(value, 0), 127)
        self.SetContainer((self.GetContainer() & ~(0x7f << 1)) | ((tmp & 0x7f) << 1))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Container",type="int",units="",minVal="0",maxVal="255",description="AutoAnswer setting",get=GetContainer,set=SetContainer,count=1, bitfieldInfo = [\
            BitFieldInfo(name="AutoAnswer",type="int",units="",minVal="0",maxVal="1",description="Enable AutoAnswer (0 == disable, 1 == enable)",get=GetAutoAnswer,set=SetAutoAnswer, enum = []),\
            BitFieldInfo(name="UnusedAutoAnswerSetGet",type="int",units="",minVal="0",maxVal="127",description="Unused, ignored",get=GetUnusedAutoAnswerSetGet,set=SetUnusedAutoAnswerSetGet, enum = [])], enum = [])\
    ]

Messaging.Register("Settings.AutoAnswer.SetGet", Settings_AutoAnswer_SetGet.ID, Settings_AutoAnswer_SetGet)
#    obj/CodeGenerator/Python/Settings/AutoAnswer.py
#    Created 27/07/2023 at 10:11:05 from:
#        Messages = messages/Settings/AutoAnswer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Settings_AutoAnswer_Status :
    ID = 4531
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 1), ("Function", 27), ("Operator", 3)])
    ReverseIDs = OrderedDict([(1, "FunctionBlock"), (27, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Settings_AutoAnswer_Status.MSG_OFFSET + Settings_AutoAnswer_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Settings_AutoAnswer_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Settings_AutoAnswer_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Settings_AutoAnswer_Status.MSG_OFFSET + Settings_AutoAnswer_Status.SIZE)
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
            self.hdr.SetMessageID(Settings_AutoAnswer_Status.ID)
            self.hdr.SetDataLength(Settings_AutoAnswer_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Settings.AutoAnswer.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetAutoPlayPauseStatus(self):
        """AutoAnswer Status"""
        value = struct.unpack_from('B', self.rawBuffer(), Settings_AutoAnswer_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAutoAnswerEnabled(self):
        """0 == AutoAnswer disabled, 1 == AutoAnswer enabled"""
        value = (self.GetAutoPlayPauseStatus() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetUnusedAutoAnswerStatus(self):
        """Unused"""
        value = (self.GetAutoPlayPauseStatus() >> 1) & 0x7f
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetAutoPlayPauseStatus(self, value):
        """AutoAnswer Status"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Settings_AutoAnswer_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAutoAnswerEnabled(self, value):
        """0 == AutoAnswer disabled, 1 == AutoAnswer enabled"""
        tmp = min(max(value, 0), 1)
        self.SetAutoPlayPauseStatus((self.GetAutoPlayPauseStatus() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetUnusedAutoAnswerStatus(self, value):
        """Unused"""
        tmp = min(max(value, 0), 127)
        self.SetAutoPlayPauseStatus((self.GetAutoPlayPauseStatus() & ~(0x7f << 1)) | ((tmp & 0x7f) << 1))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="AutoPlayPauseStatus",type="int",units="",minVal="0",maxVal="255",description="AutoAnswer Status",get=GetAutoPlayPauseStatus,set=SetAutoPlayPauseStatus,count=1, bitfieldInfo = [\
            BitFieldInfo(name="AutoAnswerEnabled",type="int",units="",minVal="0",maxVal="1",description="0 == AutoAnswer disabled, 1 == AutoAnswer enabled",get=GetAutoAnswerEnabled,set=SetAutoAnswerEnabled, enum = []),\
            BitFieldInfo(name="UnusedAutoAnswerStatus",type="int",units="",minVal="0",maxVal="127",description="Unused",get=GetUnusedAutoAnswerStatus,set=SetUnusedAutoAnswerStatus, enum = [])], enum = [])\
    ]

Messaging.Register("Settings.AutoAnswer.Status", Settings_AutoAnswer_Status.ID, Settings_AutoAnswer_Status)

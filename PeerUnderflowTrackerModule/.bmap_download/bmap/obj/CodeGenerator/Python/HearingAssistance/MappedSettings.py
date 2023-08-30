#    obj/CodeGenerator/Python/HearingAssistance/MappedSettings.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/MappedSettings.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_MappedSettings_Get :
    ID = 49265
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 7), ("Operator", 1)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (7, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Get.MSG_OFFSET + HearingAssistance_MappedSettings_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_MappedSettings_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_MappedSettings_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Get.MSG_OFFSET + HearingAssistance_MappedSettings_Get.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_MappedSettings_Get.ID)
            self.hdr.SetDataLength(HearingAssistance_MappedSettings_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.MappedSettings.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("HearingAssistance.MappedSettings.Get", HearingAssistance_MappedSettings_Get.ID, HearingAssistance_MappedSettings_Get)
#    obj/CodeGenerator/Python/HearingAssistance/MappedSettings.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/MappedSettings.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_MappedSettings_Set :
    ID = 49264
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 7), ("Operator", 0)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (7, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Set.MSG_OFFSET + HearingAssistance_MappedSettings_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_MappedSettings_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_MappedSettings_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Set.MSG_OFFSET + HearingAssistance_MappedSettings_Set.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_MappedSettings_Set.ID)
            self.hdr.SetDataLength(HearingAssistance_MappedSettings_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.MappedSettings.Set"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessLeft(self):
        """Loudness setting left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneLeft(self):
        """Fine-tune setting, left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessRight(self):
        """Loudness setting right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneRight(self):
        """Fine-tune setting, right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessLeft(self, value):
        """Loudness setting left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneLeft(self, value):
        """Fine-tune setting, left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessRight(self, value):
        """Loudness setting right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneRight(self, value):
        """Fine-tune setting, right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Set.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="LoudnessLeft",type="int",units="",minVal="-128",maxVal="127",description="Loudness setting left channel",get=GetLoudnessLeft,set=SetLoudnessLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneLeft",type="int",units="",minVal="-128",maxVal="127",description="Fine-tune setting, left channel",get=GetFineTuneLeft,set=SetFineTuneLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="LoudnessRight",type="int",units="",minVal="-128",maxVal="127",description="Loudness setting right channel",get=GetLoudnessRight,set=SetLoudnessRight,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneRight",type="int",units="",minVal="-128",maxVal="127",description="Fine-tune setting, right channel",get=GetFineTuneRight,set=SetFineTuneRight,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.MappedSettings.Set", HearingAssistance_MappedSettings_Set.ID, HearingAssistance_MappedSettings_Set)
#    obj/CodeGenerator/Python/HearingAssistance/MappedSettings.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/MappedSettings.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_MappedSettings_SetGet :
    ID = 49266
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 7), ("Operator", 2)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (7, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + HearingAssistance_MappedSettings_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_MappedSettings_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_MappedSettings_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + HearingAssistance_MappedSettings_SetGet.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_MappedSettings_SetGet.ID)
            self.hdr.SetDataLength(HearingAssistance_MappedSettings_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.MappedSettings.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessLeft(self):
        """Loudness setting left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneLeft(self):
        """Fine-tune setting, left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessRight(self):
        """Loudness setting right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneRight(self):
        """Fine-tune setting, right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessLeft(self, value):
        """Loudness setting left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneLeft(self, value):
        """Fine-tune setting, left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessRight(self, value):
        """Loudness setting right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneRight(self, value):
        """Fine-tune setting, right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_SetGet.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="LoudnessLeft",type="int",units="",minVal="-128",maxVal="127",description="Loudness setting left channel",get=GetLoudnessLeft,set=SetLoudnessLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneLeft",type="int",units="",minVal="-128",maxVal="127",description="Fine-tune setting, left channel",get=GetFineTuneLeft,set=SetFineTuneLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="LoudnessRight",type="int",units="",minVal="-128",maxVal="127",description="Loudness setting right channel",get=GetLoudnessRight,set=SetLoudnessRight,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneRight",type="int",units="",minVal="-128",maxVal="127",description="Fine-tune setting, right channel",get=GetFineTuneRight,set=SetFineTuneRight,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.MappedSettings.SetGet", HearingAssistance_MappedSettings_SetGet.ID, HearingAssistance_MappedSettings_SetGet)
#    obj/CodeGenerator/Python/HearingAssistance/MappedSettings.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/MappedSettings.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_MappedSettings_Status :
    ID = 49267
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 7), ("Operator", 3)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (7, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Status.MSG_OFFSET + HearingAssistance_MappedSettings_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_MappedSettings_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_MappedSettings_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_MappedSettings_Status.MSG_OFFSET + HearingAssistance_MappedSettings_Status.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_MappedSettings_Status.ID)
            self.hdr.SetDataLength(HearingAssistance_MappedSettings_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.MappedSettings.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessLeft(self):
        """Current loudness setting left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneLeft(self):
        """Current fine-tune setting, left channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetLoudnessRight(self):
        """Current loudness setting right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetFineTuneRight(self):
        """Current fine-tune setting, right channel"""
        value = struct.unpack_from('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessLeft(self, value):
        """Current loudness setting left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneLeft(self, value):
        """Current fine-tune setting, left channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetLoudnessRight(self, value):
        """Current loudness setting right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetFineTuneRight(self, value):
        """Current fine-tune setting, right channel"""
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), HearingAssistance_MappedSettings_Status.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="LoudnessLeft",type="int",units="",minVal="-128",maxVal="127",description="Current loudness setting left channel",get=GetLoudnessLeft,set=SetLoudnessLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneLeft",type="int",units="",minVal="-128",maxVal="127",description="Current fine-tune setting, left channel",get=GetFineTuneLeft,set=SetFineTuneLeft,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="LoudnessRight",type="int",units="",minVal="-128",maxVal="127",description="Current loudness setting right channel",get=GetLoudnessRight,set=SetLoudnessRight,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FineTuneRight",type="int",units="",minVal="-128",maxVal="127",description="Current fine-tune setting, right channel",get=GetFineTuneRight,set=SetFineTuneRight,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.MappedSettings.Status", HearingAssistance_MappedSettings_Status.ID, HearingAssistance_MappedSettings_Status)

#    obj/CodeGenerator/Python/HearingAssistance/NoiseReductionControl.py
#    Created 27/07/2023 at 10:10:47 from:
#        Messages = messages/HearingAssistance/NoiseReductionControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_NoiseReductionControl_Get :
    ID = 49233
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 5), ("Operator", 1)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (5, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Get.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_NoiseReductionControl_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_NoiseReductionControl_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Get.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Get.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_NoiseReductionControl_Get.ID)
            self.hdr.SetDataLength(HearingAssistance_NoiseReductionControl_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.NoiseReductionControl.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("HearingAssistance.NoiseReductionControl.Get", HearingAssistance_NoiseReductionControl_Get.ID, HearingAssistance_NoiseReductionControl_Get)
#    obj/CodeGenerator/Python/HearingAssistance/NoiseReductionControl.py
#    Created 27/07/2023 at 10:10:47 from:
#        Messages = messages/HearingAssistance/NoiseReductionControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_NoiseReductionControl_Set :
    ID = 49232
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 5), ("Operator", 0)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (5, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Set.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_NoiseReductionControl_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_NoiseReductionControl_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Set.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Set.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_NoiseReductionControl_Set.ID)
            self.hdr.SetDataLength(HearingAssistance_NoiseReductionControl_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.NoiseReductionControl.Set"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSetting(self):
        """Select noise reduction setting"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Set.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSetting(self, value):
        """Select noise reduction setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Set.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Setting",type="int",units="",minVal="0",maxVal="255",description="Select noise reduction setting",get=GetSetting,set=SetSetting,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.NoiseReductionControl.Set", HearingAssistance_NoiseReductionControl_Set.ID, HearingAssistance_NoiseReductionControl_Set)
#    obj/CodeGenerator/Python/HearingAssistance/NoiseReductionControl.py
#    Created 27/07/2023 at 10:10:47 from:
#        Messages = messages/HearingAssistance/NoiseReductionControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_NoiseReductionControl_SetGet :
    ID = 49234
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 5), ("Operator", 2)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (5, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_SetGet.MSG_OFFSET + HearingAssistance_NoiseReductionControl_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_NoiseReductionControl_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_NoiseReductionControl_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_SetGet.MSG_OFFSET + HearingAssistance_NoiseReductionControl_SetGet.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_NoiseReductionControl_SetGet.ID)
            self.hdr.SetDataLength(HearingAssistance_NoiseReductionControl_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.NoiseReductionControl.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSetting(self):
        """Select noise reduction setting"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSetting(self, value):
        """Select noise reduction setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Setting",type="int",units="",minVal="0",maxVal="255",description="Select noise reduction setting",get=GetSetting,set=SetSetting,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.NoiseReductionControl.SetGet", HearingAssistance_NoiseReductionControl_SetGet.ID, HearingAssistance_NoiseReductionControl_SetGet)
#    obj/CodeGenerator/Python/HearingAssistance/NoiseReductionControl.py
#    Created 27/07/2023 at 10:10:47 from:
#        Messages = messages/HearingAssistance/NoiseReductionControl.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_NoiseReductionControl_Status :
    ID = 49235
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 5), ("Operator", 3)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (5, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_NoiseReductionControl_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_NoiseReductionControl_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + HearingAssistance_NoiseReductionControl_Status.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_NoiseReductionControl_Status.ID)
            self.hdr.SetDataLength(HearingAssistance_NoiseReductionControl_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.NoiseReductionControl.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetNumSettings(self):
        """Number of settings"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetSetting(self):
        """Currently selected noise reduction setting"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetNumSettings(self, value):
        """Number of settings"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetSetting(self, value):
        """Currently selected noise reduction setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_NoiseReductionControl_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="NumSettings",type="int",units="",minVal="0",maxVal="255",description="Number of settings",get=GetNumSettings,set=SetNumSettings,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Setting",type="int",units="",minVal="0",maxVal="255",description="Currently selected noise reduction setting",get=GetSetting,set=SetSetting,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.NoiseReductionControl.Status", HearingAssistance_NoiseReductionControl_Status.ID, HearingAssistance_NoiseReductionControl_Status)

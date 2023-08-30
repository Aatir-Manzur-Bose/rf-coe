#    obj/CodeGenerator/Python/AudioManagement/LatencyAndLimits.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/LatencyAndLimits.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_LatencyAndLimits_Get :
    ID = 20689
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 13), ("Operator", 1)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (13, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_Get.MSG_OFFSET + AudioManagement_LatencyAndLimits_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_LatencyAndLimits_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_LatencyAndLimits_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_Get.MSG_OFFSET + AudioManagement_LatencyAndLimits_Get.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_LatencyAndLimits_Get.ID)
            self.hdr.SetDataLength(AudioManagement_LatencyAndLimits_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.LatencyAndLimits.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("AudioManagement.LatencyAndLimits.Get", AudioManagement_LatencyAndLimits_Get.ID, AudioManagement_LatencyAndLimits_Get)
#    obj/CodeGenerator/Python/AudioManagement/LatencyAndLimits.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/LatencyAndLimits.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_LatencyAndLimits_SetGet :
    ID = 20690
    SIZE = 6
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 13), ("Operator", 2)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (13, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + AudioManagement_LatencyAndLimits_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_LatencyAndLimits_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_LatencyAndLimits_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + AudioManagement_LatencyAndLimits_SetGet.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_LatencyAndLimits_SetGet.ID)
            self.hdr.SetDataLength(AudioManagement_LatencyAndLimits_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.LatencyAndLimits.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetTargetLatency(self):
        """Target Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def GetMinimumLatency(self):
        """Minimum Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def GetMaximumLatency(self):
        """Maximum Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetTargetLatency(self, value):
        """Target Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def SetMinimumLatency(self, value):
        """Minimum Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def SetMaximumLatency(self, value):
        """Maximum Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_SetGet.MSG_OFFSET + 4, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TargetLatency",type="int",units="",minVal="0",maxVal="65535",description="Target Latency",get=GetTargetLatency,set=SetTargetLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MinimumLatency",type="int",units="",minVal="0",maxVal="65535",description="Minimum Latency",get=GetMinimumLatency,set=SetMinimumLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MaximumLatency",type="int",units="",minVal="0",maxVal="65535",description="Maximum Latency",get=GetMaximumLatency,set=SetMaximumLatency,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("AudioManagement.LatencyAndLimits.SetGet", AudioManagement_LatencyAndLimits_SetGet.ID, AudioManagement_LatencyAndLimits_SetGet)
#    obj/CodeGenerator/Python/AudioManagement/LatencyAndLimits.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/LatencyAndLimits.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_LatencyAndLimits_Status :
    ID = 20691
    SIZE = 10
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 13), ("Operator", 3)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (13, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + AudioManagement_LatencyAndLimits_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_LatencyAndLimits_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_LatencyAndLimits_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + AudioManagement_LatencyAndLimits_Status.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_LatencyAndLimits_Status.ID)
            self.hdr.SetDataLength(AudioManagement_LatencyAndLimits_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.LatencyAndLimits.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetCurrentTargetLatency(self):
        """Current Target Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def GetCurrentMinimumLatency(self):
        """Current Minimum Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def GetCurrentMaximumLatency(self):
        """Current Maximum Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def GetMinimumTargetLatency(self):
        """Minimum Target Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def GetMaximumTargetLatency(self):
        """Maximum Target Latency"""
        value = struct.unpack_from('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 8)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetCurrentTargetLatency(self, value):
        """Current Target Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def SetCurrentMinimumLatency(self, value):
        """Current Minimum Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def SetCurrentMaximumLatency(self, value):
        """Current Maximum Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def SetMinimumTargetLatency(self, value):
        """Minimum Target Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 6, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def SetMaximumTargetLatency(self, value):
        """Maximum Target Latency"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AudioManagement_LatencyAndLimits_Status.MSG_OFFSET + 8, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="CurrentTargetLatency",type="int",units="",minVal="0",maxVal="65535",description="Current Target Latency",get=GetCurrentTargetLatency,set=SetCurrentTargetLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CurrentMinimumLatency",type="int",units="",minVal="0",maxVal="65535",description="Current Minimum Latency",get=GetCurrentMinimumLatency,set=SetCurrentMinimumLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CurrentMaximumLatency",type="int",units="",minVal="0",maxVal="65535",description="Current Maximum Latency",get=GetCurrentMaximumLatency,set=SetCurrentMaximumLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MinimumTargetLatency",type="int",units="",minVal="0",maxVal="65535",description="Minimum Target Latency",get=GetMinimumTargetLatency,set=SetMinimumTargetLatency,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MaximumTargetLatency",type="int",units="",minVal="0",maxVal="65535",description="Maximum Target Latency",get=GetMaximumTargetLatency,set=SetMaximumTargetLatency,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("AudioManagement.LatencyAndLimits.Status", AudioManagement_LatencyAndLimits_Status.ID, AudioManagement_LatencyAndLimits_Status)

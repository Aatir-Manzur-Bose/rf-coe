#    obj/CodeGenerator/Python/HearingAssistance/LiveMetrics.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/LiveMetrics.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_LiveMetrics_Get :
    ID = 49457
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 19), ("Operator", 1)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (19, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_LiveMetrics_Get.MSG_OFFSET + HearingAssistance_LiveMetrics_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_LiveMetrics_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_LiveMetrics_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_LiveMetrics_Get.MSG_OFFSET + HearingAssistance_LiveMetrics_Get.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_LiveMetrics_Get.ID)
            self.hdr.SetDataLength(HearingAssistance_LiveMetrics_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.LiveMetrics.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("HearingAssistance.LiveMetrics.Get", HearingAssistance_LiveMetrics_Get.ID, HearingAssistance_LiveMetrics_Get)
#    obj/CodeGenerator/Python/HearingAssistance/LiveMetrics.py
#    Created 27/07/2023 at 10:10:46 from:
#        Messages = messages/HearingAssistance/LiveMetrics.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class HearingAssistance_LiveMetrics_Status :
    ID = 49459
    SIZE = 9
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 12), ("Function", 19), ("Operator", 3)])
    ReverseIDs = OrderedDict([(12, "FunctionBlock"), (19, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(HearingAssistance_LiveMetrics_Status.MSG_OFFSET + HearingAssistance_LiveMetrics_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, HearingAssistance_LiveMetrics_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, HearingAssistance_LiveMetrics_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(HearingAssistance_LiveMetrics_Status.MSG_OFFSET + HearingAssistance_LiveMetrics_Status.SIZE)
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
            self.hdr.SetMessageID(HearingAssistance_LiveMetrics_Status.ID)
            self.hdr.SetDataLength(HearingAssistance_LiveMetrics_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "HearingAssistance.LiveMetrics.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(3)
    def GetLeftFitDoff(self, idx):
        """Left fit and doff metrics"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 0+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(3)
    def GetRightFitDoff(self, idx):
        """Right fit and doff metrics"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 3+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(3)
    def GetVocalEffort(self, idx):
        """Vocal effort metric"""
        value = struct.unpack_from('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 6+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(3)
    def SetLeftFitDoff(self, value, idx):
        """Left fit and doff metrics"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 0+idx*1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(3)
    def SetRightFitDoff(self, value, idx):
        """Right fit and doff metrics"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 3+idx*1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(3)
    def SetVocalEffort(self, value, idx):
        """Vocal effort metric"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), HearingAssistance_LiveMetrics_Status.MSG_OFFSET + 6+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="LeftFitDoff",type="int",units="",minVal="0",maxVal="255",description="Left fit and doff metrics",get=GetLeftFitDoff,set=SetLeftFitDoff,count=3, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RightFitDoff",type="int",units="",minVal="0",maxVal="255",description="Right fit and doff metrics",get=GetRightFitDoff,set=SetRightFitDoff,count=3, bitfieldInfo = [], enum = []),\
        FieldInfo(name="VocalEffort",type="int",units="",minVal="0",maxVal="255",description="Vocal effort metric",get=GetVocalEffort,set=SetVocalEffort,count=3, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("HearingAssistance.LiveMetrics.Status", HearingAssistance_LiveMetrics_Status.ID, HearingAssistance_LiveMetrics_Status)

#    obj/CodeGenerator/Python/EarbudDebug/B2bConnectionState.py
#    Created 27/07/2023 at 10:10:24 from:
#        Messages = messages/EarbudDebug/B2bConnectionState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class EarbudDebug_B2bConnectionState_Get :
    ID = 110657
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 27), ("Function", 4), ("Operator", 1)])
    ReverseIDs = OrderedDict([(27, "FunctionBlock"), (4, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(EarbudDebug_B2bConnectionState_Get.MSG_OFFSET + EarbudDebug_B2bConnectionState_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, EarbudDebug_B2bConnectionState_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, EarbudDebug_B2bConnectionState_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(EarbudDebug_B2bConnectionState_Get.MSG_OFFSET + EarbudDebug_B2bConnectionState_Get.SIZE)
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
            self.hdr.SetMessageID(EarbudDebug_B2bConnectionState_Get.ID)
            self.hdr.SetDataLength(EarbudDebug_B2bConnectionState_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "EarbudDebug.B2bConnectionState.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("EarbudDebug.B2bConnectionState.Get", EarbudDebug_B2bConnectionState_Get.ID, EarbudDebug_B2bConnectionState_Get)
#    obj/CodeGenerator/Python/EarbudDebug/B2bConnectionState.py
#    Created 27/07/2023 at 10:10:24 from:
#        Messages = messages/EarbudDebug/B2bConnectionState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class EarbudDebug_B2bConnectionState_Status :
    ID = 110659
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    B2bConnectionStates = OrderedDict([("B2B_CONNECTION_STATE_DISCONNECTED", 0), ("B2B_CONNECTION_STATE_CONNECTING", 1), ("B2B_CONNECTION_STATE_CONNECTED", 2), ("B2B_CONNECTION_STATE_DISCONNECTING", 3), ("B2B_CONNECTION_STATE_LINK_LOSS", 4)])
    ReverseB2bConnectionStates = OrderedDict([(0, "B2B_CONNECTION_STATE_DISCONNECTED"), (1, "B2B_CONNECTION_STATE_CONNECTING"), (2, "B2B_CONNECTION_STATE_CONNECTED"), (3, "B2B_CONNECTION_STATE_DISCONNECTING"), (4, "B2B_CONNECTION_STATE_LINK_LOSS")])
    IDs = OrderedDict([("FunctionBlock", 27), ("Function", 4), ("Operator", 3)])
    ReverseIDs = OrderedDict([(27, "FunctionBlock"), (4, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(EarbudDebug_B2bConnectionState_Status.MSG_OFFSET + EarbudDebug_B2bConnectionState_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, EarbudDebug_B2bConnectionState_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, EarbudDebug_B2bConnectionState_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(EarbudDebug_B2bConnectionState_Status.MSG_OFFSET + EarbudDebug_B2bConnectionState_Status.SIZE)
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
            self.hdr.SetMessageID(EarbudDebug_B2bConnectionState_Status.ID)
            self.hdr.SetDataLength(EarbudDebug_B2bConnectionState_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "EarbudDebug.B2bConnectionState.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetValue(self):
        """The current state of the B2B connection"""
        value = struct.unpack_from('B', self.rawBuffer(), EarbudDebug_B2bConnectionState_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetState(self, enumAsInt=0):
        """"""
        value = (self.GetValue() >> 0) & 0xff
        if not enumAsInt:
            value = EarbudDebug_B2bConnectionState_Status.ReverseB2bConnectionStates.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetValue(self, value):
        """The current state of the B2B connection"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), EarbudDebug_B2bConnectionState_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetState(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = EarbudDebug_B2bConnectionState_Status.B2bConnectionStates.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        self.SetValue((self.GetValue() & ~(0xff << 0)) | ((tmp & 0xff) << 0))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Value",type="int",units="",minVal="0",maxVal="255",description="The current state of the B2B connection",get=GetValue,set=SetValue,count=1, bitfieldInfo = [\
            BitFieldInfo(name="State",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetState,set=SetState, enum = [B2bConnectionStates, ReverseB2bConnectionStates])], enum = [])\
    ]

Messaging.Register("EarbudDebug.B2bConnectionState.Status", EarbudDebug_B2bConnectionState_Status.ID, EarbudDebug_B2bConnectionState_Status)

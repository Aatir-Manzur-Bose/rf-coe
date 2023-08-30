#    obj/CodeGenerator/Python/Peer/OobState.py
#    Created 27/07/2023 at 10:10:57 from:
#        Messages = messages/Peer/OobState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Peer_OobState_Get :
    ID = 61665
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 15), ("Function", 14), ("Operator", 1)])
    ReverseIDs = OrderedDict([(15, "FunctionBlock"), (14, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Peer_OobState_Get.MSG_OFFSET + Peer_OobState_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Peer_OobState_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Peer_OobState_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Peer_OobState_Get.MSG_OFFSET + Peer_OobState_Get.SIZE)
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
            self.hdr.SetMessageID(Peer_OobState_Get.ID)
            self.hdr.SetDataLength(Peer_OobState_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Peer.OobState.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Peer.OobState.Get", Peer_OobState_Get.ID, Peer_OobState_Get)
#    obj/CodeGenerator/Python/Peer/OobState.py
#    Created 27/07/2023 at 10:10:57 from:
#        Messages = messages/Peer/OobState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Peer_OobState_Status :
    ID = 61667
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    OobStates = OrderedDict([("OOB_IDLE", 0), ("OOB_PAIRED_BY_CUSTOMER", 1), ("OOB_SETUP_COMPLETE", 2), ("OOB_PAIRED_BY_CUSTOMER_AND_SETUP_COMPLETE", 3)])
    ReverseOobStates = OrderedDict([(0, "OOB_IDLE"), (1, "OOB_PAIRED_BY_CUSTOMER"), (2, "OOB_SETUP_COMPLETE"), (3, "OOB_PAIRED_BY_CUSTOMER_AND_SETUP_COMPLETE")])
    IDs = OrderedDict([("FunctionBlock", 15), ("Function", 14), ("Operator", 3)])
    ReverseIDs = OrderedDict([(15, "FunctionBlock"), (14, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Peer_OobState_Status.MSG_OFFSET + Peer_OobState_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Peer_OobState_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Peer_OobState_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Peer_OobState_Status.MSG_OFFSET + Peer_OobState_Status.SIZE)
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
            self.hdr.SetMessageID(Peer_OobState_Status.ID)
            self.hdr.SetDataLength(Peer_OobState_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Peer.OobState.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetOobStatus(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Peer_OobState_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('15')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetOobState(self, enumAsInt=0):
        """Out Of Box state"""
        value = (self.GetOobStatus() >> 0) & 0xf
        if not enumAsInt:
            value = Peer_OobState_Status.ReverseOobStates.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetWelcomeTonePlayed(self):
        """Whether welcome tone played, 1 - played, 0 - not played"""
        value = (self.GetOobStatus() >> 4) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('7')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def Getunused(self):
        """unused, should be set to 0"""
        value = (self.GetOobStatus() >> 5) & 0x7
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetOobStatus(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Peer_OobState_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('15')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetOobState(self, value):
        """Out Of Box state"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Peer_OobState_Status.OobStates.get(value, defaultValue)
        tmp = min(max(value, 0), 15)
        self.SetOobStatus((self.GetOobStatus() & ~(0xf << 0)) | ((tmp & 0xf) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetWelcomeTonePlayed(self, value):
        """Whether welcome tone played, 1 - played, 0 - not played"""
        tmp = min(max(value, 0), 1)
        self.SetOobStatus((self.GetOobStatus() & ~(0x1 << 4)) | ((tmp & 0x1) << 4))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('7')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def Setunused(self, value):
        """unused, should be set to 0"""
        tmp = min(max(value, 0), 7)
        self.SetOobStatus((self.GetOobStatus() & ~(0x7 << 5)) | ((tmp & 0x7) << 5))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="OobStatus",type="int",units="",minVal="0",maxVal="255",description="",get=GetOobStatus,set=SetOobStatus,count=1, bitfieldInfo = [\
            BitFieldInfo(name="OobState",type="enumeration",units="",minVal="0",maxVal="15",description="Out Of Box state",get=GetOobState,set=SetOobState, enum = [OobStates, ReverseOobStates]),\
            BitFieldInfo(name="WelcomeTonePlayed",type="int",units="",minVal="0",maxVal="1",description="Whether welcome tone played, 1 - played, 0 - not played",get=GetWelcomeTonePlayed,set=SetWelcomeTonePlayed, enum = []),\
            BitFieldInfo(name="unused",type="int",units="",minVal="0",maxVal="7",description="unused, should be set to 0",get=Getunused,set=Setunused, enum = [])], enum = [])\
    ]

Messaging.Register("Peer.OobState.Status", Peer_OobState_Status.ID, Peer_OobState_Status)

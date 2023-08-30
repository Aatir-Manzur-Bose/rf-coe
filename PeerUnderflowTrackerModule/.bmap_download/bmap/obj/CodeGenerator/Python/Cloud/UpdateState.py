#    obj/CodeGenerator/Python/Cloud/UpdateState.py
#    Created 27/07/2023 at 10:09:59 from:
#        Messages = messages/Cloud/UpdateState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Cloud_UpdateState_Get :
    ID = 81985
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 20), ("Function", 4), ("Operator", 1)])
    ReverseIDs = OrderedDict([(20, "FunctionBlock"), (4, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Cloud_UpdateState_Get.MSG_OFFSET + Cloud_UpdateState_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Cloud_UpdateState_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Cloud_UpdateState_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Cloud_UpdateState_Get.MSG_OFFSET + Cloud_UpdateState_Get.SIZE)
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
            self.hdr.SetMessageID(Cloud_UpdateState_Get.ID)
            self.hdr.SetDataLength(Cloud_UpdateState_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Cloud.UpdateState.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Cloud.UpdateState.Get", Cloud_UpdateState_Get.ID, Cloud_UpdateState_Get)
#    obj/CodeGenerator/Python/Cloud/UpdateState.py
#    Created 27/07/2023 at 10:09:59 from:
#        Messages = messages/Cloud/UpdateState.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Cloud_UpdateState_Status :
    ID = 81987
    SIZE = 7
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    CloudUpdateStates = OrderedDict([("Error", 0), ("CheckingForCloudUpdate", 1), ("NoUpdate", 2), ("Downloading", 3), ("InstallationPending", 4), ("Installing", 5), ("CheckingForLocalUpdate", 6), ("CancelInstallationPending", 7)])
    ReverseCloudUpdateStates = OrderedDict([(0, "Error"), (1, "CheckingForCloudUpdate"), (2, "NoUpdate"), (3, "Downloading"), (4, "InstallationPending"), (5, "Installing"), (6, "CheckingForLocalUpdate"), (7, "CancelInstallationPending")])
    IDs = OrderedDict([("FunctionBlock", 20), ("Function", 4), ("Operator", 3)])
    ReverseIDs = OrderedDict([(20, "FunctionBlock"), (4, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Cloud_UpdateState_Status.MSG_OFFSET + Cloud_UpdateState_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Cloud_UpdateState_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Cloud_UpdateState_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Cloud_UpdateState_Status.MSG_OFFSET + Cloud_UpdateState_Status.SIZE)
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
            self.hdr.SetMessageID(Cloud_UpdateState_Status.ID)
            self.hdr.SetDataLength(Cloud_UpdateState_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Cloud.UpdateState.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetcurrentFwuState(self, enumAsInt=0):
        """Current FWU state of device"""
        value = struct.unpack_from('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Cloud_UpdateState_Status.ReverseCloudUpdateStates.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(4)
    def Getdeadline(self, idx):
        """Unix timestamp of deadline (32-bit unix epoch)"""
        value = struct.unpack_from('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 1+idx*1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def GetContainer(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('5')
    @msg.size('0')
    @msg.count(1)
    def Getpercent(self):
        """Percent complete (0 to 100)"""
        value = (self.GetContainer() >> 0) & 0x7f
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('5')
    @msg.size('0')
    @msg.count(1)
    def Getdeferrable(self):
        """Is update deferable (0 == not deferrable, 1 == deferrable)"""
        value = (self.GetContainer() >> 7) & 0x1
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def GetavailableVersion(self):
        """Version that is available to update to (semantic versioning)"""
        value = struct.unpack_from('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetcurrentFwuState(self, value):
        """Current FWU state of device"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Cloud_UpdateState_Status.CloudUpdateStates.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(4)
    def Setdeadline(self, value, idx):
        """Unix timestamp of deadline (32-bit unix epoch)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 1+idx*1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def SetContainer(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 5, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('127')
    @msg.offset('5')
    @msg.size('0')
    @msg.count(1)
    def Setpercent(self, value):
        """Percent complete (0 to 100)"""
        tmp = min(max(value, 0), 127)
        self.SetContainer((self.GetContainer() & ~(0x7f << 0)) | ((tmp & 0x7f) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('5')
    @msg.size('0')
    @msg.count(1)
    def Setdeferrable(self, value):
        """Is update deferable (0 == not deferrable, 1 == deferrable)"""
        tmp = min(max(value, 0), 1)
        self.SetContainer((self.GetContainer() & ~(0x1 << 7)) | ((tmp & 0x1) << 7))
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def SetavailableVersion(self, value):
        """Version that is available to update to (semantic versioning)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Cloud_UpdateState_Status.MSG_OFFSET + 6, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="currentFwuState",type="enumeration",units="",minVal="0",maxVal="255",description="Current FWU state of device",get=GetcurrentFwuState,set=SetcurrentFwuState,count=1, bitfieldInfo = [], enum = [CloudUpdateStates, ReverseCloudUpdateStates]),\
        FieldInfo(name="deadline",type="int",units="",minVal="0",maxVal="255",description="Unix timestamp of deadline (32-bit unix epoch)",get=Getdeadline,set=Setdeadline,count=4, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Container",type="int",units="",minVal="0",maxVal="255",description="",get=GetContainer,set=SetContainer,count=1, bitfieldInfo = [\
            BitFieldInfo(name="percent",type="int",units="",minVal="0",maxVal="127",description="Percent complete (0 to 100)",get=Getpercent,set=Setpercent, enum = []),\
            BitFieldInfo(name="deferrable",type="int",units="",minVal="0",maxVal="1",description="Is update deferable (0 == not deferrable, 1 == deferrable)",get=Getdeferrable,set=Setdeferrable, enum = [])], enum = []),\
        FieldInfo(name="availableVersion",type="string",units="ASCII",minVal="0",maxVal="255",description="Version that is available to update to (semantic versioning)",get=GetavailableVersion,set=SetavailableVersion,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Cloud.UpdateState.Status", Cloud_UpdateState_Status.ID, Cloud_UpdateState_Status)

#    obj/CodeGenerator/Python/Status/InEar.py
#    Created 27/07/2023 at 10:11:17 from:
#        Messages = messages/Status/InEar.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Status_InEar_Get :
    ID = 8337
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 2), ("Function", 9), ("Operator", 1)])
    ReverseIDs = OrderedDict([(2, "FunctionBlock"), (9, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Status_InEar_Get.MSG_OFFSET + Status_InEar_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Status_InEar_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Status_InEar_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Status_InEar_Get.MSG_OFFSET + Status_InEar_Get.SIZE)
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
            self.hdr.SetMessageID(Status_InEar_Get.ID)
            self.hdr.SetDataLength(Status_InEar_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Status.InEar.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Status.InEar.Get", Status_InEar_Get.ID, Status_InEar_Get)
#    obj/CodeGenerator/Python/Status/InEar.py
#    Created 27/07/2023 at 10:11:17 from:
#        Messages = messages/Status/InEar.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Status_InEar_Status :
    ID = 8339
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 2), ("Function", 9), ("Operator", 3)])
    ReverseIDs = OrderedDict([(2, "FunctionBlock"), (9, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Status_InEar_Status.MSG_OFFSET + Status_InEar_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Status_InEar_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Status_InEar_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Status_InEar_Status.MSG_OFFSET + Status_InEar_Status.SIZE)
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
            self.hdr.SetMessageID(Status_InEar_Status.ID)
            self.hdr.SetDataLength(Status_InEar_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Status.InEar.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetInEarStatus(self):
        """In Ear status of left and right buds"""
        value = struct.unpack_from('B', self.rawBuffer(), Status_InEar_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetInEarLeftStatus(self):
        """In Ear status of left bud (0 == not in ear, 1 == currently in ear)"""
        value = (self.GetInEarStatus() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetInEarRightStatus(self):
        """In Ear status of right bud (0 == not in ear, 1== currently in ear)"""
        value = (self.GetInEarStatus() >> 1) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('63')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetInEarUnused(self):
        """Unused"""
        value = (self.GetInEarStatus() >> 2) & 0x3f
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetInEarStatus(self, value):
        """In Ear status of left and right buds"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Status_InEar_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetInEarLeftStatus(self, value):
        """In Ear status of left bud (0 == not in ear, 1 == currently in ear)"""
        tmp = min(max(value, 0), 1)
        self.SetInEarStatus((self.GetInEarStatus() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetInEarRightStatus(self, value):
        """In Ear status of right bud (0 == not in ear, 1== currently in ear)"""
        tmp = min(max(value, 0), 1)
        self.SetInEarStatus((self.GetInEarStatus() & ~(0x1 << 1)) | ((tmp & 0x1) << 1))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('63')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetInEarUnused(self, value):
        """Unused"""
        tmp = min(max(value, 0), 63)
        self.SetInEarStatus((self.GetInEarStatus() & ~(0x3f << 2)) | ((tmp & 0x3f) << 2))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="InEarStatus",type="int",units="",minVal="0",maxVal="255",description="In Ear status of left and right buds",get=GetInEarStatus,set=SetInEarStatus,count=1, bitfieldInfo = [\
            BitFieldInfo(name="InEarLeftStatus",type="int",units="",minVal="0",maxVal="1",description="In Ear status of left bud (0 == not in ear, 1 == currently in ear)",get=GetInEarLeftStatus,set=SetInEarLeftStatus, enum = []),\
            BitFieldInfo(name="InEarRightStatus",type="int",units="",minVal="0",maxVal="1",description="In Ear status of right bud (0 == not in ear, 1== currently in ear)",get=GetInEarRightStatus,set=SetInEarRightStatus, enum = []),\
            BitFieldInfo(name="InEarUnused",type="int",units="",minVal="0",maxVal="63",description="Unused",get=GetInEarUnused,set=SetInEarUnused, enum = [])], enum = [])\
    ]

Messaging.Register("Status.InEar.Status", Status_InEar_Status.ID, Status_InEar_Status)

#    obj/CodeGenerator/Python/Auth/PlatformName.py
#    Created 27/07/2023 at 10:09:44 from:
#        Messages = messages/Auth/PlatformName.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Auth_PlatformName_Get :
    ID = 73937
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 18), ("Function", 13), ("Operator", 1)])
    ReverseIDs = OrderedDict([(18, "FunctionBlock"), (13, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Auth_PlatformName_Get.MSG_OFFSET + Auth_PlatformName_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Auth_PlatformName_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Auth_PlatformName_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Auth_PlatformName_Get.MSG_OFFSET + Auth_PlatformName_Get.SIZE)
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
            self.hdr.SetMessageID(Auth_PlatformName_Get.ID)
            self.hdr.SetDataLength(Auth_PlatformName_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Auth.PlatformName.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Auth.PlatformName.Get", Auth_PlatformName_Get.ID, Auth_PlatformName_Get)
#    obj/CodeGenerator/Python/Auth/PlatformName.py
#    Created 27/07/2023 at 10:09:44 from:
#        Messages = messages/Auth/PlatformName.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Auth_PlatformName_Status :
    ID = 73939
    SIZE = 60
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 18), ("Function", 13), ("Operator", 3)])
    ReverseIDs = OrderedDict([(18, "FunctionBlock"), (13, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Auth_PlatformName_Status.MSG_OFFSET + Auth_PlatformName_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Auth_PlatformName_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Auth_PlatformName_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Auth_PlatformName_Status.MSG_OFFSET + Auth_PlatformName_Status.SIZE)
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
            self.hdr.SetMessageID(Auth_PlatformName_Status.ID)
            self.hdr.SetDataLength(Auth_PlatformName_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Auth.PlatformName.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(60)
    def GetPlatformName(self):
        """Platform Name (ASCII String)"""
        count = 60
        if count > len(self.rawBuffer())-(Auth_PlatformName_Status.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(Auth_PlatformName_Status.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Auth_PlatformName_Status.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(60)
    def SetPlatformName(self, value):
        """Platform Name (ASCII String)"""
        tmp = value.encode('utf-8')
        struct.pack_into('60s', self.rawBuffer(), Auth_PlatformName_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="PlatformName",type="string",units="ASCII",minVal="0",maxVal="255",description="Platform Name (ASCII String)",get=GetPlatformName,set=SetPlatformName,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Auth.PlatformName.Status", Auth_PlatformName_Status.ID, Auth_PlatformName_Status)

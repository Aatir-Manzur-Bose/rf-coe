#    obj/CodeGenerator/Python/Auth/AppIRK.py
#    Created 27/07/2023 at 10:09:42 from:
#        Messages = messages/Auth/AppIRK.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Auth_AppIRK_SetGet :
    ID = 73954
    SIZE = 48
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 18), ("Function", 14), ("Operator", 2)])
    ReverseIDs = OrderedDict([(18, "FunctionBlock"), (14, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Auth_AppIRK_SetGet.MSG_OFFSET + Auth_AppIRK_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Auth_AppIRK_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Auth_AppIRK_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Auth_AppIRK_SetGet.MSG_OFFSET + Auth_AppIRK_SetGet.SIZE)
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
            self.hdr.SetMessageID(Auth_AppIRK_SetGet.ID)
            self.hdr.SetDataLength(Auth_AppIRK_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Auth.AppIRK.SetGet"
    # Accessors
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(16)
    def GetEncryptedAppIRK(self, idx):
        """16 bytes of App IRK encrypted using AES-128-CBC algorithm w/ first 128-bits of ECDHE shared secret as the Initialization Vector (IV) and last 128-bits as the encryption key."""
        value = struct.unpack_from('B', self.rawBuffer(), Auth_AppIRK_SetGet.MSG_OFFSET + 0+idx*1)[0]
        return value
    
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('16')
    @msg.size('1')
    @msg.count(32)
    def GetAppIRKSignature(self, idx):
        """32 bytes of App IRK signature using SHA256-HMAC algorithm w/ entire ECDHE shared secret as the HMAC signing key."""
        value = struct.unpack_from('B', self.rawBuffer(), Auth_AppIRK_SetGet.MSG_OFFSET + 16+idx*1)[0]
        return value
    
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(16)
    def SetEncryptedAppIRK(self, value, idx):
        """16 bytes of App IRK encrypted using AES-128-CBC algorithm w/ first 128-bits of ECDHE shared secret as the Initialization Vector (IV) and last 128-bits as the encryption key."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Auth_AppIRK_SetGet.MSG_OFFSET + 0+idx*1, tmp)
    
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('16')
    @msg.size('1')
    @msg.count(32)
    def SetAppIRKSignature(self, value, idx):
        """32 bytes of App IRK signature using SHA256-HMAC algorithm w/ entire ECDHE shared secret as the HMAC signing key."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Auth_AppIRK_SetGet.MSG_OFFSET + 16+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="EncryptedAppIRK",type="int",units="hex",minVal="0",maxVal="255",description="16 bytes of App IRK encrypted using AES-128-CBC algorithm w/ first 128-bits of ECDHE shared secret as the Initialization Vector (IV) and last 128-bits as the encryption key.",get=GetEncryptedAppIRK,set=SetEncryptedAppIRK,count=16, bitfieldInfo = [], enum = []),\
        FieldInfo(name="AppIRKSignature",type="int",units="hex",minVal="0",maxVal="255",description="32 bytes of App IRK signature using SHA256-HMAC algorithm w/ entire ECDHE shared secret as the HMAC signing key.",get=GetAppIRKSignature,set=SetAppIRKSignature,count=32, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Auth.AppIRK.SetGet", Auth_AppIRK_SetGet.ID, Auth_AppIRK_SetGet)
#    obj/CodeGenerator/Python/Auth/AppIRK.py
#    Created 27/07/2023 at 10:09:42 from:
#        Messages = messages/Auth/AppIRK.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Auth_AppIRK_Status :
    ID = 73955
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 18), ("Function", 14), ("Operator", 3)])
    ReverseIDs = OrderedDict([(18, "FunctionBlock"), (14, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Auth_AppIRK_Status.MSG_OFFSET + Auth_AppIRK_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Auth_AppIRK_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Auth_AppIRK_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Auth_AppIRK_Status.MSG_OFFSET + Auth_AppIRK_Status.SIZE)
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
            self.hdr.SetMessageID(Auth_AppIRK_Status.ID)
            self.hdr.SetDataLength(Auth_AppIRK_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Auth.AppIRK.Status"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Auth.AppIRK.Status", Auth_AppIRK_Status.ID, Auth_AppIRK_Status)

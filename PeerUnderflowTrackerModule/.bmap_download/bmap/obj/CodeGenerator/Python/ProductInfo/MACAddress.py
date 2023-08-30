#    obj/CodeGenerator/Python/ProductInfo/MACAddress.py
#    Created 27/07/2023 at 10:11:01 from:
#        Messages = messages/ProductInfo/MACAddress.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_MACAddress_Get :
    ID = 97
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 6), ("Operator", 1)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (6, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_MACAddress_Get.MSG_OFFSET + ProductInfo_MACAddress_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_MACAddress_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_MACAddress_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_MACAddress_Get.MSG_OFFSET + ProductInfo_MACAddress_Get.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_MACAddress_Get.ID)
            self.hdr.SetDataLength(ProductInfo_MACAddress_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.MACAddress.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("ProductInfo.MACAddress.Get", ProductInfo_MACAddress_Get.ID, ProductInfo_MACAddress_Get)
#    obj/CodeGenerator/Python/ProductInfo/MACAddress.py
#    Created 27/07/2023 at 10:11:01 from:
#        Messages = messages/ProductInfo/MACAddress.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_MACAddress_Status :
    ID = 99
    SIZE = 6
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 6), ("Operator", 3)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (6, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_MACAddress_Status.MSG_OFFSET + ProductInfo_MACAddress_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_MACAddress_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_MACAddress_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_MACAddress_Status.MSG_OFFSET + ProductInfo_MACAddress_Status.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_MACAddress_Status.ID)
            self.hdr.SetDataLength(ProductInfo_MACAddress_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.MACAddress.Status"
    # Accessors
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(6)
    def GetMACAddress(self, idx):
        """MAC Address of BOSE Product"""
        value = struct.unpack_from('B', self.rawBuffer(), ProductInfo_MACAddress_Status.MSG_OFFSET + 0+idx*1)[0]
        return value
    
    @msg.units('hex')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(6)
    def SetMACAddress(self, value, idx):
        """MAC Address of BOSE Product"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), ProductInfo_MACAddress_Status.MSG_OFFSET + 0+idx*1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="MACAddress",type="int",units="hex",minVal="0",maxVal="255",description="MAC Address of BOSE Product",get=GetMACAddress,set=SetMACAddress,count=6, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("ProductInfo.MACAddress.Status", ProductInfo_MACAddress_Status.ID, ProductInfo_MACAddress_Status)

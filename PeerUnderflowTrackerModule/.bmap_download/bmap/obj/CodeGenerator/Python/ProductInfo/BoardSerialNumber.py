#    obj/CodeGenerator/Python/ProductInfo/BoardSerialNumber.py
#    Created 27/07/2023 at 10:10:59 from:
#        Messages = messages/ProductInfo/BoardSerialNumber.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_BoardSerialNumber_Get :
    ID = 145
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 9), ("Operator", 1)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (9, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_BoardSerialNumber_Get.MSG_OFFSET + ProductInfo_BoardSerialNumber_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_BoardSerialNumber_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_BoardSerialNumber_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_BoardSerialNumber_Get.MSG_OFFSET + ProductInfo_BoardSerialNumber_Get.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_BoardSerialNumber_Get.ID)
            self.hdr.SetDataLength(ProductInfo_BoardSerialNumber_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.BoardSerialNumber.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBoardAssemblyID(self):
        """If the payload length is 0, Returns Board serial number for main PCB (ID 0)  if no Board/Assembly ID specified. If the payload length is 1, Board/Assembly ID (use 0 unless the product contains  multiple PCBAs, in which case the specific PCBAs are assigned IDs on a product-by-product basis.) """
        value = struct.unpack_from('B', self.rawBuffer(), ProductInfo_BoardSerialNumber_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBoardAssemblyID(self, value):
        """If the payload length is 0, Returns Board serial number for main PCB (ID 0)  if no Board/Assembly ID specified. If the payload length is 1, Board/Assembly ID (use 0 unless the product contains  multiple PCBAs, in which case the specific PCBAs are assigned IDs on a product-by-product basis.) """
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), ProductInfo_BoardSerialNumber_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BoardAssemblyID",type="int",units="",minVal="0",maxVal="255",description="If the payload length is 0, Returns Board serial number for main PCB (ID 0)  if no Board/Assembly ID specified. If the payload length is 1, Board/Assembly ID (use 0 unless the product contains  multiple PCBAs, in which case the specific PCBAs are assigned IDs on a product-by-product basis.) ",get=GetBoardAssemblyID,set=SetBoardAssemblyID,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("ProductInfo.BoardSerialNumber.Get", ProductInfo_BoardSerialNumber_Get.ID, ProductInfo_BoardSerialNumber_Get)
#    obj/CodeGenerator/Python/ProductInfo/BoardSerialNumber.py
#    Created 27/07/2023 at 10:10:59 from:
#        Messages = messages/ProductInfo/BoardSerialNumber.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_BoardSerialNumber_Status :
    ID = 147
    SIZE = 60
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 9), ("Operator", 3)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (9, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + ProductInfo_BoardSerialNumber_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_BoardSerialNumber_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_BoardSerialNumber_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + ProductInfo_BoardSerialNumber_Status.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_BoardSerialNumber_Status.ID)
            self.hdr.SetDataLength(ProductInfo_BoardSerialNumber_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.BoardSerialNumber.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBoardAssemblyID(self):
        """Board/Assembly ID"""
        value = struct.unpack_from('B', self.rawBuffer(), ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(59)
    def GetBoardSerialNumber(self):
        """Serial Number (UTF-8 String)"""
        count = 59
        if count > len(self.rawBuffer())-(ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 1):
            count = len(self.rawBuffer())-(ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 1)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 1)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBoardAssemblyID(self, value):
        """Board/Assembly ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(59)
    def SetBoardSerialNumber(self, value):
        """Serial Number (UTF-8 String)"""
        tmp = value.encode('utf-8')
        struct.pack_into('59s', self.rawBuffer(), ProductInfo_BoardSerialNumber_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BoardAssemblyID",type="int",units="",minVal="0",maxVal="255",description="Board/Assembly ID",get=GetBoardAssemblyID,set=SetBoardAssemblyID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BoardSerialNumber",type="string",units="ASCII",minVal="0",maxVal="255",description="Serial Number (UTF-8 String)",get=GetBoardSerialNumber,set=SetBoardSerialNumber,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("ProductInfo.BoardSerialNumber.Status", ProductInfo_BoardSerialNumber_Status.ID, ProductInfo_BoardSerialNumber_Status)

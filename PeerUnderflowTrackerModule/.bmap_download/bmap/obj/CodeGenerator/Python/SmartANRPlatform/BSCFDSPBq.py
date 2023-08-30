#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBq.py
#    Created 27/07/2023 at 10:11:12 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBq.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBq_Get :
    ID = 106593
    SIZE = 123
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 6), ("Operator", 1)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (6, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBq_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBq_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Get.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBq_Get.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBq_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBq.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBSCID(self):
        """ID of BSC to access"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetBankNum(self):
        """Bank Number (0, 1, 2)"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetBiquadNum(self):
        """Which biquad within the filter"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(120)
    def GetFilterName(self):
        """The name of the filter"""
        count = 120
        if count > len(self.rawBuffer())-(SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 3):
            count = len(self.rawBuffer())-(SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 3)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 3)[0]
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
    def SetBSCID(self, value):
        """ID of BSC to access"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetBankNum(self, value):
        """Bank Number (0, 1, 2)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetBiquadNum(self, value):
        """Which biquad within the filter"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 2, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(120)
    def SetFilterName(self, value):
        """The name of the filter"""
        tmp = value.encode('utf-8')
        struct.pack_into('120s', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Get.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Bank Number (0, 1, 2)",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BiquadNum",type="int",units="",minVal="0",maxVal="255",description="Which biquad within the filter",get=GetBiquadNum,set=SetBiquadNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FilterName",type="string",units="ASCII",minVal="0",maxVal="255",description="The name of the filter",get=GetFilterName,set=SetFilterName,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBq.Get", SmartANRPlatform_BSCFDSPBq_Get.ID, SmartANRPlatform_BSCFDSPBq_Get)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBq.py
#    Created 27/07/2023 at 10:11:12 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBq.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBq_SetGet :
    ID = 106594
    SIZE = 143
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 6), ("Operator", 2)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (6, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBq_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBq_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_SetGet.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBq_SetGet.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBq_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBq.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBSCID(self):
        """ID of BSC to access"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetBankNum(self):
        """Bank Number (0, 1, 2)"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetBiquadNum(self):
        """Which biquad within the filter"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(120)
    def GetFilterName(self):
        """The name of the filter"""
        count = 120
        if count > len(self.rawBuffer())-(SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 3):
            count = len(self.rawBuffer())-(SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 3)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 3)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('123')
    @msg.size('4')
    @msg.count(5)
    def GetCoefficientArray(self, idx):
        """5 FDSP Filter signal flow coefficients."""
        value = struct.unpack_from('>L', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 123+idx*4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBSCID(self, value):
        """ID of BSC to access"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetBankNum(self, value):
        """Bank Number (0, 1, 2)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetBiquadNum(self, value):
        """Which biquad within the filter"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 2, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(120)
    def SetFilterName(self, value):
        """The name of the filter"""
        tmp = value.encode('utf-8')
        struct.pack_into('120s', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('123')
    @msg.size('4')
    @msg.count(5)
    def SetCoefficientArray(self, value, idx):
        """5 FDSP Filter signal flow coefficients."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_SetGet.MSG_OFFSET + 123+idx*4, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Bank Number (0, 1, 2)",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BiquadNum",type="int",units="",minVal="0",maxVal="255",description="Which biquad within the filter",get=GetBiquadNum,set=SetBiquadNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FilterName",type="string",units="ASCII",minVal="0",maxVal="255",description="The name of the filter",get=GetFilterName,set=SetFilterName,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CoefficientArray",type="int",units="",minVal="0",maxVal="4294967295",description="5 FDSP Filter signal flow coefficients.",get=GetCoefficientArray,set=SetCoefficientArray,count=5, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBq.SetGet", SmartANRPlatform_BSCFDSPBq_SetGet.ID, SmartANRPlatform_BSCFDSPBq_SetGet)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBq.py
#    Created 27/07/2023 at 10:11:12 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBq.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBq_Status :
    ID = 106595
    SIZE = 20
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 6), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (6, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Status.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBq_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBq_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Status.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBq_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBq_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBq.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(5)
    def GetCoefficientArray(self, idx):
        """SetGet- 0 byte payload indicating success. Get- 5 FDSP Filter signal flow coefficients."""
        value = struct.unpack_from('>L', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Status.MSG_OFFSET + 0+idx*4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(5)
    def SetCoefficientArray(self, value, idx):
        """SetGet- 0 byte payload indicating success. Get- 5 FDSP Filter signal flow coefficients."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Status.MSG_OFFSET + 0+idx*4, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="CoefficientArray",type="int",units="",minVal="0",maxVal="4294967295",description="SetGet- 0 byte payload indicating success. Get- 5 FDSP Filter signal flow coefficients.",get=GetCoefficientArray,set=SetCoefficientArray,count=5, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBq.Status", SmartANRPlatform_BSCFDSPBq_Status.ID, SmartANRPlatform_BSCFDSPBq_Status)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBq.py
#    Created 27/07/2023 at 10:11:12 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBq.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBq_Error :
    ID = 106596
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SmartANRPlatformErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("InvalidData", 3), ("RunTime", 4), ("Timeout", 5), ("InvalidState", 6), ("Verify", 7)])
    ReverseSmartANRPlatformErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "InvalidData"), (4, "RunTime"), (5, "Timeout"), (6, "InvalidState"), (7, "Verify")])
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 6), ("Operator", 4)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (6, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Error.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBq_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBq_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBq_Error.MSG_OFFSET + SmartANRPlatform_BSCFDSPBq_Error.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBq_Error.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBq_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBq.Error"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetErrorCode(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SmartANRPlatform_BSCFDSPBq_Error.ReverseSmartANRPlatformErrorResponseCodes.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetErrorCode(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SmartANRPlatform_BSCFDSPBq_Error.SmartANRPlatformErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBq_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [SmartANRPlatformErrorResponseCodes, ReverseSmartANRPlatformErrorResponseCodes])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBq.Error", SmartANRPlatform_BSCFDSPBq_Error.ID, SmartANRPlatform_BSCFDSPBq_Error)

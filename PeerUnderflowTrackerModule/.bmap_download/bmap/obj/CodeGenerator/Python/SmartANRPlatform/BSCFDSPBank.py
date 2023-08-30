#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBank.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBank.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBank_Get :
    ID = 106673
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 11), ("Operator", 1)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (11, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Get.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBank_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBank_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Get.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Get.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBank_Get.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBank_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBank.Get"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Get.MSG_OFFSET + 0)[0]
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
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBank.Get", SmartANRPlatform_BSCFDSPBank_Get.ID, SmartANRPlatform_BSCFDSPBank_Get)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBank.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBank.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBank_SetGet :
    ID = 106674
    SIZE = 5
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 11), ("Operator", 2)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (11, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBank_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBank_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_SetGet.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBank_SetGet.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBank_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBank.SetGet"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 0)[0]
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetRampMode(self):
        """0 = ramp, 1 = instant"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetZeroState(self):
        """0 = do not zero stored state on bank switch, 1 = zero stored states on bank switch"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def GetRampRate(self):
        """FDSP Bank Ramp Rate of Change (0-15)"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 4)[0]
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
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 0, tmp)
    
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
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetRampMode(self, value):
        """0 = ramp, 1 = instant"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetZeroState(self, value):
        """0 = do not zero stored state on bank switch, 1 = zero stored states on bank switch"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def SetRampRate(self, value):
        """FDSP Bank Ramp Rate of Change (0-15)"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_SetGet.MSG_OFFSET + 4, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BSCID",type="int",units="",minVal="0",maxVal="255",description="ID of BSC to access",get=GetBSCID,set=SetBSCID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Bank Number (0, 1, 2)",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RampMode",type="int",units="",minVal="0",maxVal="255",description="0 = ramp, 1 = instant",get=GetRampMode,set=SetRampMode,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ZeroState",type="int",units="",minVal="0",maxVal="255",description="0 = do not zero stored state on bank switch, 1 = zero stored states on bank switch",get=GetZeroState,set=SetZeroState,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RampRate",type="int",units="",minVal="0",maxVal="255",description="FDSP Bank Ramp Rate of Change (0-15)",get=GetRampRate,set=SetRampRate,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBank.SetGet", SmartANRPlatform_BSCFDSPBank_SetGet.ID, SmartANRPlatform_BSCFDSPBank_SetGet)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBank.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBank.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBank_Status :
    ID = 106675
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 11), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (11, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBank_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBank_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBank_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBank_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBank.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetBankNum(self):
        """Current Bank"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetRampMode(self):
        """Current ramp mode setting"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def GetZeroState(self):
        """Current zero state setting"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetRampRate(self):
        """Current ramp rate setting"""
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetBankNum(self, value):
        """Current Bank"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetRampMode(self, value):
        """Current ramp mode setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('2')
    @msg.size('1')
    @msg.count(1)
    def SetZeroState(self, value):
        """Current zero state setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetRampRate(self, value):
        """Current ramp rate setting"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Status.MSG_OFFSET + 3, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="BankNum",type="int",units="",minVal="0",maxVal="255",description="Current Bank",get=GetBankNum,set=SetBankNum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RampMode",type="int",units="",minVal="0",maxVal="255",description="Current ramp mode setting",get=GetRampMode,set=SetRampMode,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ZeroState",type="int",units="",minVal="0",maxVal="255",description="Current zero state setting",get=GetZeroState,set=SetZeroState,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RampRate",type="int",units="",minVal="0",maxVal="255",description="Current ramp rate setting",get=GetRampRate,set=SetRampRate,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBank.Status", SmartANRPlatform_BSCFDSPBank_Status.ID, SmartANRPlatform_BSCFDSPBank_Status)
#    obj/CodeGenerator/Python/SmartANRPlatform/BSCFDSPBank.py
#    Created 27/07/2023 at 10:11:11 from:
#        Messages = messages/SmartANRPlatform/BSCFDSPBank.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_BSCFDSPBank_Error :
    ID = 106676
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SmartANRPlatformErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("InvalidData", 3), ("RunTime", 4), ("Timeout", 5), ("InvalidState", 6), ("Verify", 7)])
    ReverseSmartANRPlatformErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "InvalidData"), (4, "RunTime"), (5, "Timeout"), (6, "InvalidState"), (7, "Verify")])
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 11), ("Operator", 4)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (11, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Error.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_BSCFDSPBank_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_BSCFDSPBank_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_BSCFDSPBank_Error.MSG_OFFSET + SmartANRPlatform_BSCFDSPBank_Error.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_BSCFDSPBank_Error.ID)
            self.hdr.SetDataLength(SmartANRPlatform_BSCFDSPBank_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.BSCFDSPBank.Error"
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
        value = struct.unpack_from('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = SmartANRPlatform_BSCFDSPBank_Error.ReverseSmartANRPlatformErrorResponseCodes.get(value, value)
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
        value = SmartANRPlatform_BSCFDSPBank_Error.SmartANRPlatformErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SmartANRPlatform_BSCFDSPBank_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [SmartANRPlatformErrorResponseCodes, ReverseSmartANRPlatformErrorResponseCodes])\
    ]

Messaging.Register("SmartANRPlatform.BSCFDSPBank.Error", SmartANRPlatform_BSCFDSPBank_Error.ID, SmartANRPlatform_BSCFDSPBank_Error)

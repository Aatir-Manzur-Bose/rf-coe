#    obj/CodeGenerator/Python/Manufacturing/APTxLicense.py
#    Created 27/07/2023 at 10:10:49 from:
#        Messages = messages/Manufacturing/APTxLicense.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_APTxLicense_Start :
    ID = 94805
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 37), ("Operator", 5)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (37, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_APTxLicense_Start.MSG_OFFSET + Manufacturing_APTxLicense_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_APTxLicense_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_APTxLicense_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_APTxLicense_Start.MSG_OFFSET + Manufacturing_APTxLicense_Start.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_APTxLicense_Start.ID)
            self.hdr.SetDataLength(Manufacturing_APTxLicense_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.APTxLicense.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Manufacturing.APTxLicense.Start", Manufacturing_APTxLicense_Start.ID, Manufacturing_APTxLicense_Start)
#    obj/CodeGenerator/Python/Manufacturing/APTxLicense.py
#    Created 27/07/2023 at 10:10:49 from:
#        Messages = messages/Manufacturing/APTxLicense.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_APTxLicense_Result :
    ID = 94806
    SIZE = 5
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    APTxLicenseStatus = OrderedDict([("APTX_LICENSE_INVALID", 0), ("APTX_LICENSE_VALID", 1)])
    ReverseAPTxLicenseStatus = OrderedDict([(0, "APTX_LICENSE_INVALID"), (1, "APTX_LICENSE_VALID")])
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 37), ("Operator", 6)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (37, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_APTxLicense_Result.MSG_OFFSET + Manufacturing_APTxLicense_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_APTxLicense_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_APTxLicense_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_APTxLicense_Result.MSG_OFFSET + Manufacturing_APTxLicense_Result.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_APTxLicense_Result.ID)
            self.hdr.SetDataLength(Manufacturing_APTxLicense_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.APTxLicense.Result"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetVerifyResult(self, enumAsInt=0):
        """Aptx license validation result is either 1 for valid license or 0 for invalid license"""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_APTxLicense_Result.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Manufacturing_APTxLicense_Result.ReverseAPTxLicenseStatus.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('1')
    @msg.size('4')
    @msg.count(1)
    def GetFeatureFlags(self):
        """Bitfield denoting features supported by license"""
        value = struct.unpack_from('>L', self.rawBuffer(), Manufacturing_APTxLicense_Result.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def GetAPTxLicenseFeatureAdaptiveDecode(self):
        """Aptx license feature adaptive decode."""
        value = (self.GetFeatureFlags() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def GetAPTxLicenseFeatureMonoDecode(self):
        """Aptx license feature mono decode."""
        value = (self.GetFeatureFlags() >> 1) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def GetAPTxLicenseFeatureLossLessDecode(self):
        """Aptx license feature Loss less decode."""
        value = (self.GetFeatureFlags() >> 2) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('536870911')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def GetUnassigned(self):
        """Unassigned"""
        value = (self.GetFeatureFlags() >> 3) & 0x1fffffff
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetVerifyResult(self, value):
        """Aptx license validation result is either 1 for valid license or 0 for invalid license"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Manufacturing_APTxLicense_Result.APTxLicenseStatus.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_APTxLicense_Result.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('1')
    @msg.size('4')
    @msg.count(1)
    def SetFeatureFlags(self, value):
        """Bitfield denoting features supported by license"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Manufacturing_APTxLicense_Result.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def SetAPTxLicenseFeatureAdaptiveDecode(self, value):
        """Aptx license feature adaptive decode."""
        tmp = min(max(value, 0), 1)
        self.SetFeatureFlags((self.GetFeatureFlags() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def SetAPTxLicenseFeatureMonoDecode(self, value):
        """Aptx license feature mono decode."""
        tmp = min(max(value, 0), 1)
        self.SetFeatureFlags((self.GetFeatureFlags() & ~(0x1 << 1)) | ((tmp & 0x1) << 1))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def SetAPTxLicenseFeatureLossLessDecode(self, value):
        """Aptx license feature Loss less decode."""
        tmp = min(max(value, 0), 1)
        self.SetFeatureFlags((self.GetFeatureFlags() & ~(0x1 << 2)) | ((tmp & 0x1) << 2))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('536870911')
    @msg.offset('1')
    @msg.size('0')
    @msg.count(1)
    def SetUnassigned(self, value):
        """Unassigned"""
        tmp = min(max(value, 0), 536870911)
        self.SetFeatureFlags((self.GetFeatureFlags() & ~(0x1fffffff << 3)) | ((tmp & 0x1fffffff) << 3))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="VerifyResult",type="enumeration",units="",minVal="0",maxVal="255",description="Aptx license validation result is either 1 for valid license or 0 for invalid license",get=GetVerifyResult,set=SetVerifyResult,count=1, bitfieldInfo = [], enum = [APTxLicenseStatus, ReverseAPTxLicenseStatus]),\
        FieldInfo(name="FeatureFlags",type="int",units="",minVal="0",maxVal="4294967295",description="Bitfield denoting features supported by license",get=GetFeatureFlags,set=SetFeatureFlags,count=1, bitfieldInfo = [\
            BitFieldInfo(name="APTxLicenseFeatureAdaptiveDecode",type="int",units="",minVal="0",maxVal="1",description="Aptx license feature adaptive decode.",get=GetAPTxLicenseFeatureAdaptiveDecode,set=SetAPTxLicenseFeatureAdaptiveDecode, enum = []),\
            BitFieldInfo(name="APTxLicenseFeatureMonoDecode",type="int",units="",minVal="0",maxVal="1",description="Aptx license feature mono decode.",get=GetAPTxLicenseFeatureMonoDecode,set=SetAPTxLicenseFeatureMonoDecode, enum = []),\
            BitFieldInfo(name="APTxLicenseFeatureLossLessDecode",type="int",units="",minVal="0",maxVal="1",description="Aptx license feature Loss less decode.",get=GetAPTxLicenseFeatureLossLessDecode,set=SetAPTxLicenseFeatureLossLessDecode, enum = []),\
            BitFieldInfo(name="Unassigned",type="int",units="",minVal="0",maxVal="536870911",description="Unassigned",get=GetUnassigned,set=SetUnassigned, enum = [])], enum = [])\
    ]

Messaging.Register("Manufacturing.APTxLicense.Result", Manufacturing_APTxLicense_Result.ID, Manufacturing_APTxLicense_Result)

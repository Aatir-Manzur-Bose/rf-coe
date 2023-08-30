#    obj/CodeGenerator/Python/Debug/ConnDetails.py
#    Created 27/07/2023 at 10:10:10 from:
#        Messages = messages/Debug/ConnDetails.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_ConnDetails_Start :
    ID = 33173
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 25), ("Operator", 5)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (25, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_ConnDetails_Start.MSG_OFFSET + Debug_ConnDetails_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_ConnDetails_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_ConnDetails_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_ConnDetails_Start.MSG_OFFSET + Debug_ConnDetails_Start.SIZE)
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
            self.hdr.SetMessageID(Debug_ConnDetails_Start.ID)
            self.hdr.SetDataLength(Debug_ConnDetails_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.ConnDetails.Start"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetValue(self):
        """Connection index"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_ConnDetails_Start.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetValue(self, value):
        """Connection index"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_ConnDetails_Start.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Value",type="int",units="",minVal="0",maxVal="255",description="Connection index",get=GetValue,set=SetValue,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.ConnDetails.Start", Debug_ConnDetails_Start.ID, Debug_ConnDetails_Start)
#    obj/CodeGenerator/Python/Debug/ConnDetails.py
#    Created 27/07/2023 at 10:10:10 from:
#        Messages = messages/Debug/ConnDetails.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_ConnDetails_Status :
    ID = 33171
    SIZE = 90
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    BTAddressType = OrderedDict([("Public", 0), ("Random", 1), ("Invalid", 2)])
    ReverseBTAddressType = OrderedDict([(0, "Public"), (1, "Random"), (2, "Invalid")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 25), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (25, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_ConnDetails_Status.MSG_OFFSET + Debug_ConnDetails_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_ConnDetails_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_ConnDetails_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_ConnDetails_Status.MSG_OFFSET + Debug_ConnDetails_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_ConnDetails_Status.ID)
            self.hdr.SetDataLength(Debug_ConnDetails_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.ConnDetails.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetDeviceConnected(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetConnected(self):
        """1 == Connected, 0 == Not Connected."""
        value = (self.GetDeviceConnected() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAddressType(self, enumAsInt=0):
        """BT Address Type."""
        value = (self.GetDeviceConnected() >> 1) & 0x3
        if not enumAsInt:
            value = Debug_ConnDetails_Status.ReverseBTAddressType.get(value, value)
        return value
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(6)
    def GetMacAddress(self, idx):
        """Mac address of PDL device"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 1+idx*1)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('7')
    @msg.size('1')
    @msg.count(7)
    def GetProfiles(self):
        """Profiles of the connection. h=hfp 2=a2dp v=avrcp p=pbapc s=spp i=iap"""
        count = 7
        if count > len(self.rawBuffer())-(Debug_ConnDetails_Status.MSG_OFFSET + 7):
            count = len(self.rawBuffer())-(Debug_ConnDetails_Status.MSG_OFFSET + 7)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 7)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('14')
    @msg.size('1')
    @msg.count(16)
    def GetLinkKey(self, idx):
        """Link key of the connection"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 14+idx*1)[0]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('30')
    @msg.size('1')
    @msg.count(60)
    def GetFriendlyName(self):
        """Friendly name of PDL device."""
        count = 60
        if count > len(self.rawBuffer())-(Debug_ConnDetails_Status.MSG_OFFSET + 30):
            count = len(self.rawBuffer())-(Debug_ConnDetails_Status.MSG_OFFSET + 30)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 30)[0]
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
    def SetDeviceConnected(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('Boolean')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetConnected(self, value):
        """1 == Connected, 0 == Not Connected."""
        tmp = min(max(value, 0), 1)
        self.SetDeviceConnected((self.GetDeviceConnected() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAddressType(self, value):
        """BT Address Type."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_ConnDetails_Status.BTAddressType.get(value, defaultValue)
        tmp = min(max(value, 0), 3)
        self.SetDeviceConnected((self.GetDeviceConnected() & ~(0x3 << 1)) | ((tmp & 0x3) << 1))
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(6)
    def SetMacAddress(self, value, idx):
        """Mac address of PDL device"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 1+idx*1, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('7')
    @msg.size('1')
    @msg.count(7)
    def SetProfiles(self, value):
        """Profiles of the connection. h=hfp 2=a2dp v=avrcp p=pbapc s=spp i=iap"""
        tmp = value.encode('utf-8')
        struct.pack_into('7s', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 7, tmp)
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('14')
    @msg.size('1')
    @msg.count(16)
    def SetLinkKey(self, value, idx):
        """Link key of the connection"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 14+idx*1, tmp)
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('30')
    @msg.size('1')
    @msg.count(60)
    def SetFriendlyName(self, value):
        """Friendly name of PDL device."""
        tmp = value.encode('utf-8')
        struct.pack_into('60s', self.rawBuffer(), Debug_ConnDetails_Status.MSG_OFFSET + 30, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="DeviceConnected",type="int",units="",minVal="0",maxVal="255",description="",get=GetDeviceConnected,set=SetDeviceConnected,count=1, bitfieldInfo = [\
            BitFieldInfo(name="Connected",type="int",units="Boolean",minVal="0",maxVal="1",description="1 == Connected, 0 == Not Connected.",get=GetConnected,set=SetConnected, enum = []),\
            BitFieldInfo(name="AddressType",type="enumeration",units="",minVal="0",maxVal="3",description="BT Address Type.",get=GetAddressType,set=SetAddressType, enum = [BTAddressType, ReverseBTAddressType])], enum = []),\
        FieldInfo(name="MacAddress",type="int",units="HEX",minVal="0",maxVal="255",description="Mac address of PDL device",get=GetMacAddress,set=SetMacAddress,count=6, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Profiles",type="string",units="ASCII",minVal="0",maxVal="255",description="Profiles of the connection. h=hfp 2=a2dp v=avrcp p=pbapc s=spp i=iap",get=GetProfiles,set=SetProfiles,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="LinkKey",type="int",units="HEX",minVal="0",maxVal="255",description="Link key of the connection",get=GetLinkKey,set=SetLinkKey,count=16, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FriendlyName",type="string",units="ASCII",minVal="0",maxVal="255",description="Friendly name of PDL device.",get=GetFriendlyName,set=SetFriendlyName,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.ConnDetails.Status", Debug_ConnDetails_Status.ID, Debug_ConnDetails_Status)
#    obj/CodeGenerator/Python/Debug/ConnDetails.py
#    Created 27/07/2023 at 10:10:10 from:
#        Messages = messages/Debug/ConnDetails.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_ConnDetails_Result :
    ID = 33174
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 25), ("Operator", 6)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (25, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_ConnDetails_Result.MSG_OFFSET + Debug_ConnDetails_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_ConnDetails_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_ConnDetails_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_ConnDetails_Result.MSG_OFFSET + Debug_ConnDetails_Result.SIZE)
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
            self.hdr.SetMessageID(Debug_ConnDetails_Result.ID)
            self.hdr.SetDataLength(Debug_ConnDetails_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.ConnDetails.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.ConnDetails.Result", Debug_ConnDetails_Result.ID, Debug_ConnDetails_Result)

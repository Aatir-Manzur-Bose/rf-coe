#    obj/CodeGenerator/Python/headers/SerialHeader.py
#    Created 27/07/2023 at 10:10:45 from:
#        Messages = messages/headers/SerialHeader.yaml
#        Template = HeaderTemplate.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SerialHeader :
    SIZE = 12
    MSG_OFFSET = 0
    # Enumerations
    FunctionBlocks = OrderedDict([("ProductInfo", 0), ("Settings", 1), ("Status", 2), ("FirmwareUpdate", 3), ("DeviceManagement", 4), ("AudioManagement", 5), ("Call", 6), ("Control", 7), ("Debug", 8), ("Notification", 9), ("Reserved1", 10), ("Reserved2", 11), ("HearingAssistance", 12), ("DataCollection", 13), ("HeartRateMonitor", 14), ("Peer", 15), ("VPA", 16), ("WiFi", 17), ("Auth", 18), ("Experimental", 19), ("Cloud", 20), ("AugmentedReality", 21), ("Print", 22), ("Manufacturing", 23), ("SensorInterface", 24), ("BatteryDebug", 25), ("SmartANRPlatform", 26), ("EarbudDebug", 27), ("AudioStream", 28), ("CaseDebug", 29), ("MTIDVI", 30), ("AudioModes", 31)])
    ReverseFunctionBlocks = OrderedDict([(0, "ProductInfo"), (1, "Settings"), (2, "Status"), (3, "FirmwareUpdate"), (4, "DeviceManagement"), (5, "AudioManagement"), (6, "Call"), (7, "Control"), (8, "Debug"), (9, "Notification"), (10, "Reserved1"), (11, "Reserved2"), (12, "HearingAssistance"), (13, "DataCollection"), (14, "HeartRateMonitor"), (15, "Peer"), (16, "VPA"), (17, "WiFi"), (18, "Auth"), (19, "Experimental"), (20, "Cloud"), (21, "AugmentedReality"), (22, "Print"), (23, "Manufacturing"), (24, "SensorInterface"), (25, "BatteryDebug"), (26, "SmartANRPlatform"), (27, "EarbudDebug"), (28, "AudioStream"), (29, "CaseDebug"), (30, "MTIDVI"), (31, "AudioModes")])
    Operators = OrderedDict([("Set", 0), ("Get", 1), ("SetGet", 2), ("Status", 3), ("Error", 4), ("Start", 5), ("Result", 6), ("Processing", 7)])
    ReverseOperators = OrderedDict([(0, "Set"), (1, "Get"), (2, "SetGet"), (3, "Status"), (4, "Error"), (5, "Start"), (6, "Result"), (7, "Processing")])
    

    #@staticmethod
    #def Create() :
    #    message_buffer = ctypes.create_string_buffer(SerialHeader.SIZE)
    #    self.SetStartSequence(3735928559)
    #    self.SetHeaderChecksum(0)
    #    self.SetBodyChecksum(0)
    #    return message_buffer
    
    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SerialHeader.SIZE)
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
        if doInit:
            self.initialize()

    def initialize(self):
            self.SetStartSequence(3735928559)
            self.SetHeaderChecksum(0)
            self.SetBodyChecksum(0)
            pass
    
    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SerialHeader"

    def SetMessageID(self, id):
        self.SetOperator(id & 0xf)
        id = id >> 4
        self.SetFunction(id & 0xff)
        id = id >> 8
        self.SetFunctionBlock(id & 0xff)

    def GetMessageID(self):
        id = ((((self.GetFunctionBlock(1))<<8)+self.GetFunction())<<4)+self.GetOperator(1)
        return id

    # Accessors
    @msg.units('')
    @msg.default('3735928559')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def GetStartSequence(self):
        """"""
        value = struct.unpack_from('>L', self.rawBuffer(), SerialHeader.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def GetFunctionBlock(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 4)[0]
        if not enumAsInt:
            value = SerialHeader.ReverseFunctionBlocks.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def GetFunction(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def GetPackedField(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('15')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def GetOperator(self, enumAsInt=0):
        """"""
        value = (self.GetPackedField() >> 0) & 0xf
        if not enumAsInt:
            value = SerialHeader.ReverseOperators.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def GetSessionID(self):
        """"""
        value = (self.GetPackedField() >> 4) & 0x3
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def GetDeviceID(self):
        """"""
        value = (self.GetPackedField() >> 6) & 0x3
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('7')
    @msg.size('1')
    @msg.count(1)
    def GetDataLength(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 7)[0]
        return value
    
    @msg.units('')
    @msg.default('0')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def GetHeaderChecksum(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), SerialHeader.MSG_OFFSET + 8)[0]
        return value
    
    @msg.units('')
    @msg.default('0')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def GetBodyChecksum(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), SerialHeader.MSG_OFFSET + 10)[0]
        return value
    
    @msg.units('')
    @msg.default('3735928559')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def SetStartSequence(self, value):
        """"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), SerialHeader.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def SetFunctionBlock(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SerialHeader.FunctionBlocks.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def SetFunction(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 5, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def SetPackedField(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 6, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('15')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def SetOperator(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = SerialHeader.Operators.get(value, defaultValue)
        tmp = min(max(value, 0), 15)
        self.SetPackedField((self.GetPackedField() & ~(0xf << 0)) | ((tmp & 0xf) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def SetSessionID(self, value):
        """"""
        tmp = min(max(value, 0), 3)
        self.SetPackedField((self.GetPackedField() & ~(0x3 << 4)) | ((tmp & 0x3) << 4))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('3')
    @msg.offset('6')
    @msg.size('0')
    @msg.count(1)
    def SetDeviceID(self, value):
        """"""
        tmp = min(max(value, 0), 3)
        self.SetPackedField((self.GetPackedField() & ~(0x3 << 6)) | ((tmp & 0x3) << 6))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('7')
    @msg.size('1')
    @msg.count(1)
    def SetDataLength(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), SerialHeader.MSG_OFFSET + 7, tmp)
    
    @msg.units('')
    @msg.default('0')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def SetHeaderChecksum(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SerialHeader.MSG_OFFSET + 8, tmp)
    
    @msg.units('')
    @msg.default('0')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def SetBodyChecksum(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), SerialHeader.MSG_OFFSET + 10, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="StartSequence",type="int",units="",minVal="0",maxVal="4294967295",description="",get=GetStartSequence,set=SetStartSequence,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FunctionBlock",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetFunctionBlock,set=SetFunctionBlock,count=1, idbits=8,bitfieldInfo = [], enum = [FunctionBlocks, ReverseFunctionBlocks]),\
        FieldInfo(name="Function",type="int",units="",minVal="0",maxVal="255",description="",get=GetFunction,set=SetFunction,count=1, idbits=8,bitfieldInfo = [], enum = []),\
        FieldInfo(name="PackedField",type="int",units="",minVal="0",maxVal="255",description="",get=GetPackedField,set=SetPackedField,count=1, bitfieldInfo = [\
            BitFieldInfo(name="Operator",type="enumeration",units="",minVal="0",maxVal="15",description="",get=GetOperator,set=SetOperator, idbits=4,enum = [Operators, ReverseOperators]),\
            BitFieldInfo(name="SessionID",type="int",units="",minVal="0",maxVal="3",description="",get=GetSessionID,set=SetSessionID, enum = []),\
            BitFieldInfo(name="DeviceID",type="int",units="",minVal="0",maxVal="3",description="",get=GetDeviceID,set=SetDeviceID, enum = [])], enum = []),\
        FieldInfo(name="DataLength",type="int",units="",minVal="0",maxVal="255",description="",get=GetDataLength,set=SetDataLength,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="HeaderChecksum",type="int",units="",minVal="0",maxVal="65535",description="",get=GetHeaderChecksum,set=SetHeaderChecksum,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BodyChecksum",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBodyChecksum,set=SetBodyChecksum,count=1, bitfieldInfo = [], enum = [])\
    ]

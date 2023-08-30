#    obj/CodeGenerator/Python/Debug/RadioTest.py
#    Created 27/07/2023 at 10:10:14 from:
#        Messages = messages/Debug/RadioTest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RadioTest_Start :
    ID = 33029
    SIZE = 9
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    RadioTestType = OrderedDict([("TestStopMode", 0), ("TxContinuousTestMode", 1), ("DutMode", 2), ("TxData1Mode", 3), ("TxData2Mode", 4), ("TxPacketTypeMode", 5), ("RxDataMode", 6), ("SetTxPower", 7)])
    ReverseRadioTestType = OrderedDict([(0, "TestStopMode"), (1, "TxContinuousTestMode"), (2, "DutMode"), (3, "TxData1Mode"), (4, "TxData2Mode"), (5, "TxPacketTypeMode"), (6, "RxDataMode"), (7, "SetTxPower")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 16), ("Operator", 5)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (16, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RadioTest_Start.MSG_OFFSET + Debug_RadioTest_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RadioTest_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RadioTest_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RadioTest_Start.MSG_OFFSET + Debug_RadioTest_Start.SIZE)
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
            self.hdr.SetMessageID(Debug_RadioTest_Start.ID)
            self.hdr.SetDataLength(Debug_RadioTest_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RadioTest.Start"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetRadioTestMode(self, enumAsInt=0):
        """Radio Test Mode"""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_RadioTest_Start.ReverseRadioTestType.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetParam1(self):
        """LO Frequency from 2402 to 2480 (Continuous Transmit Mode, Tx Data 1 Test, Rx Data Test); or Country Code (Tx Data 2 Test); or Packet Type (TX Packet Types Test)"""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def GetParam2(self):
        """Power Level from 0 to 4095 (Continuous Transmit Mode, Tx Data 1 Test, Tx Data 2 Test, Set Tx Power); or Highside modulation 0 or 1 (Rx Data Test); or Packet Size (TX Packet Types Test)"""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('5')
    @msg.size('2')
    @msg.count(1)
    def GetParam3(self):
        """Frequency Modulation from -32678 to 32767 in 1/4096 MHz steps, 4096 means 1MHz (Continuous Transmit Mode); or Attenuation (Rx Data Test)"""
        value = struct.unpack_from('>h', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('7')
    @msg.size('2')
    @msg.count(1)
    def GetTimeToReset(self):
        """Time To Reset System. 0 means 'run test forever'"""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 7)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetRadioTestMode(self, value):
        """Radio Test Mode"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_RadioTest_Start.RadioTestType.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetParam1(self, value):
        """LO Frequency from 2402 to 2480 (Continuous Transmit Mode, Tx Data 1 Test, Rx Data Test); or Country Code (Tx Data 2 Test); or Packet Type (TX Packet Types Test)"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def SetParam2(self, value):
        """Power Level from 0 to 4095 (Continuous Transmit Mode, Tx Data 1 Test, Tx Data 2 Test, Set Tx Power); or Highside modulation 0 or 1 (Rx Data Test); or Packet Size (TX Packet Types Test)"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('5')
    @msg.size('2')
    @msg.count(1)
    def SetParam3(self, value):
        """Frequency Modulation from -32678 to 32767 in 1/4096 MHz steps, 4096 means 1MHz (Continuous Transmit Mode); or Attenuation (Rx Data Test)"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 5, tmp)
    
    @msg.units('seconds')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('7')
    @msg.size('2')
    @msg.count(1)
    def SetTimeToReset(self, value):
        """Time To Reset System. 0 means 'run test forever'"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_RadioTest_Start.MSG_OFFSET + 7, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="RadioTestMode",type="enumeration",units="",minVal="0",maxVal="255",description="Radio Test Mode",get=GetRadioTestMode,set=SetRadioTestMode,count=1, bitfieldInfo = [], enum = [RadioTestType, ReverseRadioTestType]),\
        FieldInfo(name="Param1",type="int",units="",minVal="0",maxVal="65535",description="LO Frequency from 2402 to 2480 (Continuous Transmit Mode, Tx Data 1 Test, Rx Data Test); or Country Code (Tx Data 2 Test); or Packet Type (TX Packet Types Test)",get=GetParam1,set=SetParam1,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Param2",type="int",units="",minVal="0",maxVal="65535",description="Power Level from 0 to 4095 (Continuous Transmit Mode, Tx Data 1 Test, Tx Data 2 Test, Set Tx Power); or Highside modulation 0 or 1 (Rx Data Test); or Packet Size (TX Packet Types Test)",get=GetParam2,set=SetParam2,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Param3",type="int",units="",minVal="-32768",maxVal="32767",description="Frequency Modulation from -32678 to 32767 in 1/4096 MHz steps, 4096 means 1MHz (Continuous Transmit Mode); or Attenuation (Rx Data Test)",get=GetParam3,set=SetParam3,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="TimeToReset",type="int",units="seconds",minVal="0",maxVal="65535",description="Time To Reset System. 0 means 'run test forever'",get=GetTimeToReset,set=SetTimeToReset,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.RadioTest.Start", Debug_RadioTest_Start.ID, Debug_RadioTest_Start)
#    obj/CodeGenerator/Python/Debug/RadioTest.py
#    Created 27/07/2023 at 10:10:14 from:
#        Messages = messages/Debug/RadioTest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_RadioTest_Result :
    ID = 33030
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 16), ("Operator", 6)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (16, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_RadioTest_Result.MSG_OFFSET + Debug_RadioTest_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_RadioTest_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_RadioTest_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_RadioTest_Result.MSG_OFFSET + Debug_RadioTest_Result.SIZE)
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
            self.hdr.SetMessageID(Debug_RadioTest_Result.ID)
            self.hdr.SetDataLength(Debug_RadioTest_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.RadioTest.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.RadioTest.Result", Debug_RadioTest_Result.ID, Debug_RadioTest_Result)

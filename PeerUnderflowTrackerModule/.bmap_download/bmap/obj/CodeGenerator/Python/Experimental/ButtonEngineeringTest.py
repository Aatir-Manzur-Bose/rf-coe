#    obj/CodeGenerator/Python/Experimental/ButtonEngineeringTest.py
#    Created 27/07/2023 at 10:10:31 from:
#        Messages = messages/Experimental/ButtonEngineeringTest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_ButtonEngineeringTest_Get :
    ID = 79105
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 80), ("Operator", 1)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (80, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_Get.MSG_OFFSET + Experimental_ButtonEngineeringTest_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_ButtonEngineeringTest_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_ButtonEngineeringTest_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_Get.MSG_OFFSET + Experimental_ButtonEngineeringTest_Get.SIZE)
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
            self.hdr.SetMessageID(Experimental_ButtonEngineeringTest_Get.ID)
            self.hdr.SetDataLength(Experimental_ButtonEngineeringTest_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.ButtonEngineeringTest.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Experimental.ButtonEngineeringTest.Get", Experimental_ButtonEngineeringTest_Get.ID, Experimental_ButtonEngineeringTest_Get)
#    obj/CodeGenerator/Python/Experimental/ButtonEngineeringTest.py
#    Created 27/07/2023 at 10:10:31 from:
#        Messages = messages/Experimental/ButtonEngineeringTest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_ButtonEngineeringTest_SetGet :
    ID = 79106
    SIZE = 7
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    UeBudPhysicalStatus = OrderedDict([("BPS_NOT_AVAILABLE", -2), ("BPS_IN_CASE", 0), ("BPS_ON_BODY", 1), ("BPS_ON_TABLE", 2), ("BPS_IN_HAND", 3), ("BPS_PRESUMED_TRANSITION", 4), ("BPS_PRESUMED_ON_BODY", 5)])
    ReverseUeBudPhysicalStatus = OrderedDict([(-2, "BPS_NOT_AVAILABLE"), (0, "BPS_IN_CASE"), (1, "BPS_ON_BODY"), (2, "BPS_ON_TABLE"), (3, "BPS_IN_HAND"), (4, "BPS_PRESUMED_TRANSITION"), (5, "BPS_PRESUMED_ON_BODY")])
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 80), ("Operator", 2)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (80, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + Experimental_ButtonEngineeringTest_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_ButtonEngineeringTest_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_ButtonEngineeringTest_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + Experimental_ButtonEngineeringTest_SetGet.SIZE)
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
            self.hdr.SetMessageID(Experimental_ButtonEngineeringTest_SetGet.ID)
            self.hdr.SetDataLength(Experimental_ButtonEngineeringTest_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.ButtonEngineeringTest.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetType(self):
        """Button press type"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetButtons(self):
        """Bitfield of buttons pressed."""
        value = struct.unpack_from('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetButtonGroup(self):
        """0 == earbud Master or non-earbud product; 1 == earbud Puppet"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def GetInternalState(self):
        """Simulated System State of Device. If not set, the simulated button will be processed according to the device actual state."""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def GetBudPhyStatus(self, enumAsInt=0):
        """Location of earbud. Do not set or set to UE_PS_NOT_AVAILABLE for Non-Earbud products."""
        value = struct.unpack_from('b', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 5)[0]
        if not enumAsInt:
            value = Experimental_ButtonEngineeringTest_SetGet.ReverseUeBudPhysicalStatus.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def GetSendControlEvent(self):
        """0 == Only lookup the generated control event; 1 == Send out the generated control event"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetType(self, value):
        """Button press type"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetButtons(self, value):
        """Bitfield of buttons pressed."""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetButtonGroup(self, value):
        """0 == earbud Master or non-earbud product; 1 == earbud Puppet"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def SetInternalState(self, value):
        """Simulated System State of Device. If not set, the simulated button will be processed according to the device actual state."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-128')
    @msg.maxVal('127')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def SetBudPhyStatus(self, value):
        """Location of earbud. Do not set or set to UE_PS_NOT_AVAILABLE for Non-Earbud products."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Experimental_ButtonEngineeringTest_SetGet.UeBudPhysicalStatus.get(value, defaultValue)
        tmp = min(max(value, -128), 127)
        struct.pack_into('b', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 5, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('6')
    @msg.size('1')
    @msg.count(1)
    def SetSendControlEvent(self, value):
        """0 == Only lookup the generated control event; 1 == Send out the generated control event"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_SetGet.MSG_OFFSET + 6, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Type",type="int",units="",minVal="0",maxVal="255",description="Button press type",get=GetType,set=SetType,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Buttons",type="int",units="",minVal="0",maxVal="65535",description="Bitfield of buttons pressed.",get=GetButtons,set=SetButtons,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ButtonGroup",type="int",units="",minVal="0",maxVal="255",description="0 == earbud Master or non-earbud product; 1 == earbud Puppet",get=GetButtonGroup,set=SetButtonGroup,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="InternalState",type="int",units="",minVal="0",maxVal="255",description="Simulated System State of Device. If not set, the simulated button will be processed according to the device actual state.",get=GetInternalState,set=SetInternalState,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BudPhyStatus",type="enumeration",units="",minVal="-128",maxVal="127",description="Location of earbud. Do not set or set to UE_PS_NOT_AVAILABLE for Non-Earbud products.",get=GetBudPhyStatus,set=SetBudPhyStatus,count=1, bitfieldInfo = [], enum = [UeBudPhysicalStatus, ReverseUeBudPhysicalStatus]),\
        FieldInfo(name="SendControlEvent",type="int",units="",minVal="0",maxVal="255",description="0 == Only lookup the generated control event; 1 == Send out the generated control event",get=GetSendControlEvent,set=SetSendControlEvent,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Experimental.ButtonEngineeringTest.SetGet", Experimental_ButtonEngineeringTest_SetGet.ID, Experimental_ButtonEngineeringTest_SetGet)
#    obj/CodeGenerator/Python/Experimental/ButtonEngineeringTest.py
#    Created 27/07/2023 at 10:10:31 from:
#        Messages = messages/Experimental/ButtonEngineeringTest.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_ButtonEngineeringTest_Status :
    ID = 79107
    SIZE = 84
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 80), ("Operator", 3)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (80, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + Experimental_ButtonEngineeringTest_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_ButtonEngineeringTest_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_ButtonEngineeringTest_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + Experimental_ButtonEngineeringTest_Status.SIZE)
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
            self.hdr.SetMessageID(Experimental_ButtonEngineeringTest_Status.ID)
            self.hdr.SetDataLength(Experimental_ButtonEngineeringTest_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.ButtonEngineeringTest.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetType(self):
        """Button press type."""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetButtons(self):
        """Bitfield of buttons pressed."""
        value = struct.unpack_from('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def GetButtonGroup(self):
        """0 == earbud Master or non-earbud product; 1 == earbud Puppet"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(40)
    def GetButtonControlEvent(self, idx):
        """Control Events generated by Button, there maybe more than 1 control events mapping to Button"""
        value = struct.unpack_from('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 4+idx*2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetType(self, value):
        """Button press type."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetButtons(self, value):
        """Bitfield of buttons pressed."""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('3')
    @msg.size('1')
    @msg.count(1)
    def SetButtonGroup(self, value):
        """0 == earbud Master or non-earbud product; 1 == earbud Puppet"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(40)
    def SetButtonControlEvent(self, value, idx):
        """Control Events generated by Button, there maybe more than 1 control events mapping to Button"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Experimental_ButtonEngineeringTest_Status.MSG_OFFSET + 4+idx*2, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Type",type="int",units="",minVal="0",maxVal="255",description="Button press type.",get=GetType,set=SetType,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Buttons",type="int",units="",minVal="0",maxVal="65535",description="Bitfield of buttons pressed.",get=GetButtons,set=SetButtons,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ButtonGroup",type="int",units="",minVal="0",maxVal="255",description="0 == earbud Master or non-earbud product; 1 == earbud Puppet",get=GetButtonGroup,set=SetButtonGroup,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ButtonControlEvent",type="int",units="",minVal="0",maxVal="65535",description="Control Events generated by Button, there maybe more than 1 control events mapping to Button",get=GetButtonControlEvent,set=SetButtonControlEvent,count=40, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Experimental.ButtonEngineeringTest.Status", Experimental_ButtonEngineeringTest_Status.ID, Experimental_ButtonEngineeringTest_Status)

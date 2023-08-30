#    obj/CodeGenerator/Python/Control/MaxSourceCurrent.py
#    Created 27/07/2023 at 10:10:01 from:
#        Messages = messages/Control/MaxSourceCurrent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Control_MaxSourceCurrent_SetGet :
    ID = 28802
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargeCurrentValue = OrderedDict([("STANDARD_CHARGE", 0), ("FAST_CHARGE", 1), ("QUICK_CHARGE", 2)])
    ReverseChargeCurrentValue = OrderedDict([(0, "STANDARD_CHARGE"), (1, "FAST_CHARGE"), (2, "QUICK_CHARGE")])
    IDs = OrderedDict([("FunctionBlock", 7), ("Function", 8), ("Operator", 2)])
    ReverseIDs = OrderedDict([(7, "FunctionBlock"), (8, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_SetGet.MSG_OFFSET + Control_MaxSourceCurrent_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Control_MaxSourceCurrent_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Control_MaxSourceCurrent_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_SetGet.MSG_OFFSET + Control_MaxSourceCurrent_SetGet.SIZE)
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
            self.hdr.SetMessageID(Control_MaxSourceCurrent_SetGet.ID)
            self.hdr.SetDataLength(Control_MaxSourceCurrent_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Control.MaxSourceCurrent.SetGet"
    # Accessors
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetChargeCurrentCapacity(self, enumAsInt=0):
        """Charger current in battery capacity (C)"""
        value = struct.unpack_from('B', self.rawBuffer(), Control_MaxSourceCurrent_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Control_MaxSourceCurrent_SetGet.ReverseChargeCurrentValue.get(value, value)
        return value
    
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetChargeCurrentCapacity(self, value):
        """Charger current in battery capacity (C)"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Control_MaxSourceCurrent_SetGet.ChargeCurrentValue.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Control_MaxSourceCurrent_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ChargeCurrentCapacity",type="enumeration",units="ChargeCurrentValue",minVal="0",maxVal="255",description="Charger current in battery capacity (C)",get=GetChargeCurrentCapacity,set=SetChargeCurrentCapacity,count=1, bitfieldInfo = [], enum = [ChargeCurrentValue, ReverseChargeCurrentValue])\
    ]

Messaging.Register("Control.MaxSourceCurrent.SetGet", Control_MaxSourceCurrent_SetGet.ID, Control_MaxSourceCurrent_SetGet)
#    obj/CodeGenerator/Python/Control/MaxSourceCurrent.py
#    Created 27/07/2023 at 10:10:01 from:
#        Messages = messages/Control/MaxSourceCurrent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Control_MaxSourceCurrent_Get :
    ID = 28801
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargeCurrentValue = OrderedDict([("STANDARD_CHARGE", 0), ("FAST_CHARGE", 1), ("QUICK_CHARGE", 2)])
    ReverseChargeCurrentValue = OrderedDict([(0, "STANDARD_CHARGE"), (1, "FAST_CHARGE"), (2, "QUICK_CHARGE")])
    IDs = OrderedDict([("FunctionBlock", 7), ("Function", 8), ("Operator", 1)])
    ReverseIDs = OrderedDict([(7, "FunctionBlock"), (8, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_Get.MSG_OFFSET + Control_MaxSourceCurrent_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Control_MaxSourceCurrent_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Control_MaxSourceCurrent_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_Get.MSG_OFFSET + Control_MaxSourceCurrent_Get.SIZE)
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
            self.hdr.SetMessageID(Control_MaxSourceCurrent_Get.ID)
            self.hdr.SetDataLength(Control_MaxSourceCurrent_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Control.MaxSourceCurrent.Get"
    # Accessors
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetChargeCurrentCapacity(self, enumAsInt=0):
        """Charger current in battery capacity (C)"""
        value = struct.unpack_from('B', self.rawBuffer(), Control_MaxSourceCurrent_Get.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Control_MaxSourceCurrent_Get.ReverseChargeCurrentValue.get(value, value)
        return value
    
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetChargeCurrentCapacity(self, value):
        """Charger current in battery capacity (C)"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Control_MaxSourceCurrent_Get.ChargeCurrentValue.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Control_MaxSourceCurrent_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ChargeCurrentCapacity",type="enumeration",units="ChargeCurrentValue",minVal="0",maxVal="255",description="Charger current in battery capacity (C)",get=GetChargeCurrentCapacity,set=SetChargeCurrentCapacity,count=1, bitfieldInfo = [], enum = [ChargeCurrentValue, ReverseChargeCurrentValue])\
    ]

Messaging.Register("Control.MaxSourceCurrent.Get", Control_MaxSourceCurrent_Get.ID, Control_MaxSourceCurrent_Get)
#    obj/CodeGenerator/Python/Control/MaxSourceCurrent.py
#    Created 27/07/2023 at 10:10:01 from:
#        Messages = messages/Control/MaxSourceCurrent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Control_MaxSourceCurrent_Status :
    ID = 28803
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ChargeCurrentValue = OrderedDict([("STANDARD_CHARGE", 0), ("FAST_CHARGE", 1), ("QUICK_CHARGE", 2)])
    ReverseChargeCurrentValue = OrderedDict([(0, "STANDARD_CHARGE"), (1, "FAST_CHARGE"), (2, "QUICK_CHARGE")])
    IDs = OrderedDict([("FunctionBlock", 7), ("Function", 8), ("Operator", 3)])
    ReverseIDs = OrderedDict([(7, "FunctionBlock"), (8, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_Status.MSG_OFFSET + Control_MaxSourceCurrent_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Control_MaxSourceCurrent_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Control_MaxSourceCurrent_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Control_MaxSourceCurrent_Status.MSG_OFFSET + Control_MaxSourceCurrent_Status.SIZE)
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
            self.hdr.SetMessageID(Control_MaxSourceCurrent_Status.ID)
            self.hdr.SetDataLength(Control_MaxSourceCurrent_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Control.MaxSourceCurrent.Status"
    # Accessors
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetChargeCurrentCapacity(self, enumAsInt=0):
        """Charger current in battery capacity (C)"""
        value = struct.unpack_from('B', self.rawBuffer(), Control_MaxSourceCurrent_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Control_MaxSourceCurrent_Status.ReverseChargeCurrentValue.get(value, value)
        return value
    
    @msg.units('ChargeCurrentValue')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetChargeCurrentCapacity(self, value):
        """Charger current in battery capacity (C)"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Control_MaxSourceCurrent_Status.ChargeCurrentValue.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Control_MaxSourceCurrent_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ChargeCurrentCapacity",type="enumeration",units="ChargeCurrentValue",minVal="0",maxVal="255",description="Charger current in battery capacity (C)",get=GetChargeCurrentCapacity,set=SetChargeCurrentCapacity,count=1, bitfieldInfo = [], enum = [ChargeCurrentValue, ReverseChargeCurrentValue])\
    ]

Messaging.Register("Control.MaxSourceCurrent.Status", Control_MaxSourceCurrent_Status.ID, Control_MaxSourceCurrent_Status)

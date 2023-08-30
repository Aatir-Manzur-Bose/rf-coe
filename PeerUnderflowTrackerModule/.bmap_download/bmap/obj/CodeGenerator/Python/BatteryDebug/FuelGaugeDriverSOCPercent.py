#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeDriverSOCPercent.py
#    Created 27/07/2023 at 10:09:50 from:
#        Messages = messages/BatteryDebug/FuelGaugeDriverSOCPercent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeDriverSOCPercent_Get :
    ID = 103217
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 51), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (51, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Get.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Get.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeDriverSOCPercent_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeDriverSOCPercent_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeDriverSOCPercent.Get"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeID(self):
        """Fuel gauge ID"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Get.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeID(self, value):
        """Fuel gauge ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Get.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeID",type="int",units="",minVal="0",maxVal="255",description="Fuel gauge ID",get=GetFuelGaugeID,set=SetFuelGaugeID,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeDriverSOCPercent.Get", BatteryDebug_FuelGaugeDriverSOCPercent_Get.ID, BatteryDebug_FuelGaugeDriverSOCPercent_Get)
#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeDriverSOCPercent.py
#    Created 27/07/2023 at 10:09:50 from:
#        Messages = messages/BatteryDebug/FuelGaugeDriverSOCPercent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeDriverSOCPercent_Set :
    ID = 103216
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 51), ("Operator", 0)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (51, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Set.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Set.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Set.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeDriverSOCPercent_Set.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeDriverSOCPercent_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeDriverSOCPercent.Set"
    # Accessors
    @msg.units('Percent')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeDriverSOCPercent(self):
        """Fuel Gauge Driver SOC Percent"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Set.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('Percent')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeDriverSOCPercent(self, value):
        """Fuel Gauge Driver SOC Percent"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Set.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeDriverSOCPercent",type="int",units="Percent",minVal="0",maxVal="255",description="Fuel Gauge Driver SOC Percent",get=GetFuelGaugeDriverSOCPercent,set=SetFuelGaugeDriverSOCPercent,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeDriverSOCPercent.Set", BatteryDebug_FuelGaugeDriverSOCPercent_Set.ID, BatteryDebug_FuelGaugeDriverSOCPercent_Set)
#    obj/CodeGenerator/Python/BatteryDebug/FuelGaugeDriverSOCPercent.py
#    Created 27/07/2023 at 10:09:50 from:
#        Messages = messages/BatteryDebug/FuelGaugeDriverSOCPercent.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_FuelGaugeDriverSOCPercent_Status :
    ID = 103219
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 51), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (51, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_FuelGaugeDriverSOCPercent_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + BatteryDebug_FuelGaugeDriverSOCPercent_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_FuelGaugeDriverSOCPercent_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_FuelGaugeDriverSOCPercent_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.FuelGaugeDriverSOCPercent.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeID(self):
        """Fuel gauge ID"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('Percent')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetFuelGaugeDriverSOCPercent(self):
        """Fuel Gauge Driver SOC Percent"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeID(self, value):
        """Fuel gauge ID"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('Percent')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetFuelGaugeDriverSOCPercent(self, value):
        """Fuel Gauge Driver SOC Percent"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_FuelGaugeDriverSOCPercent_Status.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="FuelGaugeID",type="int",units="",minVal="0",maxVal="255",description="Fuel gauge ID",get=GetFuelGaugeID,set=SetFuelGaugeID,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="FuelGaugeDriverSOCPercent",type="int",units="Percent",minVal="0",maxVal="255",description="Fuel Gauge Driver SOC Percent",get=GetFuelGaugeDriverSOCPercent,set=SetFuelGaugeDriverSOCPercent,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("BatteryDebug.FuelGaugeDriverSOCPercent.Status", BatteryDebug_FuelGaugeDriverSOCPercent_Status.ID, BatteryDebug_FuelGaugeDriverSOCPercent_Status)

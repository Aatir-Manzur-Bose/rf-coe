#    obj/CodeGenerator/Python/BatteryDebug/CurrentRegionDefinitions.py
#    Created 27/07/2023 at 10:09:48 from:
#        Messages = messages/BatteryDebug/CurrentRegionDefinitions.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_CurrentRegionDefinitions_Get :
    ID = 102913
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 32), ("Operator", 1)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (32, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_CurrentRegionDefinitions_Get.MSG_OFFSET + BatteryDebug_CurrentRegionDefinitions_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_CurrentRegionDefinitions_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_CurrentRegionDefinitions_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_CurrentRegionDefinitions_Get.MSG_OFFSET + BatteryDebug_CurrentRegionDefinitions_Get.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_CurrentRegionDefinitions_Get.ID)
            self.hdr.SetDataLength(BatteryDebug_CurrentRegionDefinitions_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.CurrentRegionDefinitions.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("BatteryDebug.CurrentRegionDefinitions.Get", BatteryDebug_CurrentRegionDefinitions_Get.ID, BatteryDebug_CurrentRegionDefinitions_Get)
#    obj/CodeGenerator/Python/BatteryDebug/CurrentRegionDefinitions.py
#    Created 27/07/2023 at 10:09:48 from:
#        Messages = messages/BatteryDebug/CurrentRegionDefinitions.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class BatteryDebug_CurrentRegionDefinitions_Status :
    ID = 102915
    SIZE = 9
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    RegionType = OrderedDict([("QuickChargeDischarge", 0), ("QuickCharge", 1), ("FastChargeDischarge", 2), ("FastCharge", 3), ("StandardChargeDischarge", 4), ("StandardCharge", 5), ("PrechargeChargeDischarge", 6), ("PrechargeCharge", 7), ("TrickleCharge", 8), ("ZeroVoltTrickleCharge", 9), ("Discharge", 10), ("Brick", 11), ("LowPowerState", 12), ("ShipMode", 13), ("ShelfMode", 14), ("LowPowerStateHighVoltage", 15), ("LowPowerStateLowVoltage", 16), ("Preliminary", 17), ("QuickChargeDischargeVariant1", 18), ("QuickChargeDischargeVariant2", 19), ("QuickChargeDischargeVariant3", 20), ("QuickChargeDischargeVariant4", 21), ("FastChargeDischargeVariant1", 22), ("StandardChargeDischargeVariant1", 23), ("TrickleChargeVariant1", 24), ("SlowChargeDischarge", 25), ("Invalid", 26)])
    ReverseRegionType = OrderedDict([(0, "QuickChargeDischarge"), (1, "QuickCharge"), (2, "FastChargeDischarge"), (3, "FastCharge"), (4, "StandardChargeDischarge"), (5, "StandardCharge"), (6, "PrechargeChargeDischarge"), (7, "PrechargeCharge"), (8, "TrickleCharge"), (9, "ZeroVoltTrickleCharge"), (10, "Discharge"), (11, "Brick"), (12, "LowPowerState"), (13, "ShipMode"), (14, "ShelfMode"), (15, "LowPowerStateHighVoltage"), (16, "LowPowerStateLowVoltage"), (17, "Preliminary"), (18, "QuickChargeDischargeVariant1"), (19, "QuickChargeDischargeVariant2"), (20, "QuickChargeDischargeVariant3"), (21, "QuickChargeDischargeVariant4"), (22, "FastChargeDischargeVariant1"), (23, "StandardChargeDischargeVariant1"), (24, "TrickleChargeVariant1"), (25, "SlowChargeDischarge"), (26, "Invalid")])
    IDs = OrderedDict([("FunctionBlock", 25), ("Function", 32), ("Operator", 3)])
    ReverseIDs = OrderedDict([(25, "FunctionBlock"), (32, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + BatteryDebug_CurrentRegionDefinitions_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, BatteryDebug_CurrentRegionDefinitions_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, BatteryDebug_CurrentRegionDefinitions_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + BatteryDebug_CurrentRegionDefinitions_Status.SIZE)
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
            self.hdr.SetMessageID(BatteryDebug_CurrentRegionDefinitions_Status.ID)
            self.hdr.SetDataLength(BatteryDebug_CurrentRegionDefinitions_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "BatteryDebug.CurrentRegionDefinitions.Status"
    # Accessors
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetTemperatureLowerBound(self):
        """Temperature lower bound for current region"""
        value = struct.unpack_from('>h', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def GetTemperatureUpperBound(self):
        """Temperature upper bound for current region"""
        value = struct.unpack_from('>h', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('mV')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def GetVoltageLowerBound(self):
        """Voltage lower bound for current region"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('mV')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def GetVoltageUpperBound(self):
        """Voltage upper bound for current region"""
        value = struct.unpack_from('>H', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('8')
    @msg.size('1')
    @msg.count(1)
    def GetRegionType(self, enumAsInt=0):
        """Region type for current region"""
        value = struct.unpack_from('B', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 8)[0]
        if not enumAsInt:
            value = BatteryDebug_CurrentRegionDefinitions_Status.ReverseRegionType.get(value, value)
        return value
    
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetTemperatureLowerBound(self, value):
        """Temperature lower bound for current region"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('C')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def SetTemperatureUpperBound(self, value):
        """Temperature upper bound for current region"""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 2, tmp)
    
    @msg.units('mV')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('4')
    @msg.size('2')
    @msg.count(1)
    def SetVoltageLowerBound(self, value):
        """Voltage lower bound for current region"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 4, tmp)
    
    @msg.units('mV')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def SetVoltageUpperBound(self, value):
        """Voltage upper bound for current region"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 6, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('8')
    @msg.size('1')
    @msg.count(1)
    def SetRegionType(self, value):
        """Region type for current region"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = BatteryDebug_CurrentRegionDefinitions_Status.RegionType.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), BatteryDebug_CurrentRegionDefinitions_Status.MSG_OFFSET + 8, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="TemperatureLowerBound",type="int",units="C",minVal="-32768",maxVal="32767",description="Temperature lower bound for current region",get=GetTemperatureLowerBound,set=SetTemperatureLowerBound,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="TemperatureUpperBound",type="int",units="C",minVal="-32768",maxVal="32767",description="Temperature upper bound for current region",get=GetTemperatureUpperBound,set=SetTemperatureUpperBound,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="VoltageLowerBound",type="int",units="mV",minVal="0",maxVal="65535",description="Voltage lower bound for current region",get=GetVoltageLowerBound,set=SetVoltageLowerBound,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="VoltageUpperBound",type="int",units="mV",minVal="0",maxVal="65535",description="Voltage upper bound for current region",get=GetVoltageUpperBound,set=SetVoltageUpperBound,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegionType",type="enumeration",units="",minVal="0",maxVal="255",description="Region type for current region",get=GetRegionType,set=SetRegionType,count=1, bitfieldInfo = [], enum = [RegionType, ReverseRegionType])\
    ]

Messaging.Register("BatteryDebug.CurrentRegionDefinitions.Status", BatteryDebug_CurrentRegionDefinitions_Status.ID, BatteryDebug_CurrentRegionDefinitions_Status)

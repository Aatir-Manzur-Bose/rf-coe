#    obj/CodeGenerator/Python/Experimental/SwindonSAISrcSelAndTimingRefSel.py
#    Created 27/07/2023 at 10:10:41 from:
#        Messages = messages/Experimental/SwindonSAISrcSelAndTimingRefSel.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_SwindonSAISrcSelAndTimingRefSel_Get :
    ID = 79089
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 79), ("Operator", 1)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (79, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Get.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Get.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Get.SIZE)
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
            self.hdr.SetMessageID(Experimental_SwindonSAISrcSelAndTimingRefSel_Get.ID)
            self.hdr.SetDataLength(Experimental_SwindonSAISrcSelAndTimingRefSel_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.SwindonSAISrcSelAndTimingRefSel.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Experimental.SwindonSAISrcSelAndTimingRefSel.Get", Experimental_SwindonSAISrcSelAndTimingRefSel_Get.ID, Experimental_SwindonSAISrcSelAndTimingRefSel_Get)
#    obj/CodeGenerator/Python/Experimental/SwindonSAISrcSelAndTimingRefSel.py
#    Created 27/07/2023 at 10:10:41 from:
#        Messages = messages/Experimental/SwindonSAISrcSelAndTimingRefSel.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_SwindonSAISrcSelAndTimingRefSel_Set :
    ID = 79088
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SourceSelector = OrderedDict([("LeftPtoARM_RightPtoARM", 0), ("ARMtoLeftP_ARMtoRightP", 1), ("LeftPtoARM_ARMtoLeftP", 2), ("RightPtoARM_ARMtoRightP", 3)])
    ReverseSourceSelector = OrderedDict([(0, "LeftPtoARM_RightPtoARM"), (1, "ARMtoLeftP_ARMtoRightP"), (2, "LeftPtoARM_ARMtoLeftP"), (3, "RightPtoARM_ARMtoRightP")])
    TimingRefrence = OrderedDict([("ENABLE", 0), ("DISABLE", 1)])
    ReverseTimingRefrence = OrderedDict([(0, "ENABLE"), (1, "DISABLE")])
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 79), ("Operator", 0)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (79, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Set.SIZE)
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
            self.hdr.SetMessageID(Experimental_SwindonSAISrcSelAndTimingRefSel_Set.ID)
            self.hdr.SetDataLength(Experimental_SwindonSAISrcSelAndTimingRefSel_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.SwindonSAISrcSelAndTimingRefSel.Set"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSourceSelector(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Experimental_SwindonSAISrcSelAndTimingRefSel_Set.ReverseSourceSelector.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetTimingRefrence(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + 1)[0]
        if not enumAsInt:
            value = Experimental_SwindonSAISrcSelAndTimingRefSel_Set.ReverseTimingRefrence.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSourceSelector(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Experimental_SwindonSAISrcSelAndTimingRefSel_Set.SourceSelector.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetTimingRefrence(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Experimental_SwindonSAISrcSelAndTimingRefSel_Set.TimingRefrence.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Set.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SourceSelector",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetSourceSelector,set=SetSourceSelector,count=1, bitfieldInfo = [], enum = [SourceSelector, ReverseSourceSelector]),\
        FieldInfo(name="TimingRefrence",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetTimingRefrence,set=SetTimingRefrence,count=1, bitfieldInfo = [], enum = [TimingRefrence, ReverseTimingRefrence])\
    ]

Messaging.Register("Experimental.SwindonSAISrcSelAndTimingRefSel.Set", Experimental_SwindonSAISrcSelAndTimingRefSel_Set.ID, Experimental_SwindonSAISrcSelAndTimingRefSel_Set)
#    obj/CodeGenerator/Python/Experimental/SwindonSAISrcSelAndTimingRefSel.py
#    Created 27/07/2023 at 10:10:41 from:
#        Messages = messages/Experimental/SwindonSAISrcSelAndTimingRefSel.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Experimental_SwindonSAISrcSelAndTimingRefSel_Status :
    ID = 79091
    SIZE = 6
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SourceSelector = OrderedDict([("LeftPtoARM_RightPtoARM", 0), ("ARMtoLeftP_ARMtoRightP", 1), ("LeftPtoARM_ARMtoLeftP", 2), ("RightPtoARM_ARMtoRightP", 3)])
    ReverseSourceSelector = OrderedDict([(0, "LeftPtoARM_RightPtoARM"), (1, "ARMtoLeftP_ARMtoRightP"), (2, "LeftPtoARM_ARMtoLeftP"), (3, "RightPtoARM_ARMtoRightP")])
    TimingRefrence = OrderedDict([("ENABLE", 0), ("DISABLE", 1)])
    ReverseTimingRefrence = OrderedDict([(0, "ENABLE"), (1, "DISABLE")])
    IDs = OrderedDict([("FunctionBlock", 19), ("Function", 79), ("Operator", 3)])
    ReverseIDs = OrderedDict([(19, "FunctionBlock"), (79, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Experimental_SwindonSAISrcSelAndTimingRefSel_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + Experimental_SwindonSAISrcSelAndTimingRefSel_Status.SIZE)
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
            self.hdr.SetMessageID(Experimental_SwindonSAISrcSelAndTimingRefSel_Status.ID)
            self.hdr.SetDataLength(Experimental_SwindonSAISrcSelAndTimingRefSel_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Experimental.SwindonSAISrcSelAndTimingRefSel.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSourceSelector(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Experimental_SwindonSAISrcSelAndTimingRefSel_Status.ReverseSourceSelector.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetTimingRefrence(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 1)[0]
        if not enumAsInt:
            value = Experimental_SwindonSAISrcSelAndTimingRefSel_Status.ReverseTimingRefrence.get(value, value)
        return value
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('2')
    @msg.size('4')
    @msg.count(1)
    def GetVersion(self):
        """Version 32 bits"""
        value = struct.unpack_from('>L', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSourceSelector(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Experimental_SwindonSAISrcSelAndTimingRefSel_Status.SourceSelector.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetTimingRefrence(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Experimental_SwindonSAISrcSelAndTimingRefSel_Status.TimingRefrence.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('HEX')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('2')
    @msg.size('4')
    @msg.count(1)
    def SetVersion(self, value):
        """Version 32 bits"""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Experimental_SwindonSAISrcSelAndTimingRefSel_Status.MSG_OFFSET + 2, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SourceSelector",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetSourceSelector,set=SetSourceSelector,count=1, bitfieldInfo = [], enum = [SourceSelector, ReverseSourceSelector]),\
        FieldInfo(name="TimingRefrence",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetTimingRefrence,set=SetTimingRefrence,count=1, bitfieldInfo = [], enum = [TimingRefrence, ReverseTimingRefrence]),\
        FieldInfo(name="Version",type="int",units="HEX",minVal="0",maxVal="4294967295",description="Version 32 bits",get=GetVersion,set=SetVersion,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Experimental.SwindonSAISrcSelAndTimingRefSel.Status", Experimental_SwindonSAISrcSelAndTimingRefSel_Status.ID, Experimental_SwindonSAISrcSelAndTimingRefSel_Status)

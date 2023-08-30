#    obj/CodeGenerator/Python/AudioManagement/SpatialAudioMode.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/SpatialAudioMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_SpatialAudioMode_Get :
    ID = 20721
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 15), ("Operator", 1)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (15, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_Get.MSG_OFFSET + AudioManagement_SpatialAudioMode_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_SpatialAudioMode_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_SpatialAudioMode_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_Get.MSG_OFFSET + AudioManagement_SpatialAudioMode_Get.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_SpatialAudioMode_Get.ID)
            self.hdr.SetDataLength(AudioManagement_SpatialAudioMode_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.SpatialAudioMode.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("AudioManagement.SpatialAudioMode.Get", AudioManagement_SpatialAudioMode_Get.ID, AudioManagement_SpatialAudioMode_Get)
#    obj/CodeGenerator/Python/AudioManagement/SpatialAudioMode.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/SpatialAudioMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_SpatialAudioMode_SetGet :
    ID = 20722
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SpatialAudioModeTypes = OrderedDict([("SpatialAudioDisabled", 0), ("SpatialAudioFixedToRoom", 1), ("SpatialAudioFixedToHead", 2)])
    ReverseSpatialAudioModeTypes = OrderedDict([(0, "SpatialAudioDisabled"), (1, "SpatialAudioFixedToRoom"), (2, "SpatialAudioFixedToHead")])
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 15), ("Operator", 2)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (15, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_SetGet.MSG_OFFSET + AudioManagement_SpatialAudioMode_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_SpatialAudioMode_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_SpatialAudioMode_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_SetGet.MSG_OFFSET + AudioManagement_SpatialAudioMode_SetGet.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_SpatialAudioMode_SetGet.ID)
            self.hdr.SetDataLength(AudioManagement_SpatialAudioMode_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.SpatialAudioMode.SetGet"
    # Accessors
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetMode(self, enumAsInt=0):
        """Desired spatial audio mode."""
        value = struct.unpack_from('B', self.rawBuffer(), AudioManagement_SpatialAudioMode_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = AudioManagement_SpatialAudioMode_SetGet.ReverseSpatialAudioModeTypes.get(value, value)
        return value
    
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetMode(self, value):
        """Desired spatial audio mode."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = AudioManagement_SpatialAudioMode_SetGet.SpatialAudioModeTypes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), AudioManagement_SpatialAudioMode_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Mode",type="enumeration",units="Enum",minVal="0",maxVal="255",description="Desired spatial audio mode.",get=GetMode,set=SetMode,count=1, bitfieldInfo = [], enum = [SpatialAudioModeTypes, ReverseSpatialAudioModeTypes])\
    ]

Messaging.Register("AudioManagement.SpatialAudioMode.SetGet", AudioManagement_SpatialAudioMode_SetGet.ID, AudioManagement_SpatialAudioMode_SetGet)
#    obj/CodeGenerator/Python/AudioManagement/SpatialAudioMode.py
#    Created 27/07/2023 at 10:09:38 from:
#        Messages = messages/AudioManagement/SpatialAudioMode.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AudioManagement_SpatialAudioMode_Status :
    ID = 20723
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SpatialAudioModeTypes = OrderedDict([("SpatialAudioDisabled", 0), ("SpatialAudioFixedToRoom", 1), ("SpatialAudioFixedToHead", 2)])
    ReverseSpatialAudioModeTypes = OrderedDict([(0, "SpatialAudioDisabled"), (1, "SpatialAudioFixedToRoom"), (2, "SpatialAudioFixedToHead")])
    IDs = OrderedDict([("FunctionBlock", 5), ("Function", 15), ("Operator", 3)])
    ReverseIDs = OrderedDict([(5, "FunctionBlock"), (15, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_Status.MSG_OFFSET + AudioManagement_SpatialAudioMode_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, AudioManagement_SpatialAudioMode_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, AudioManagement_SpatialAudioMode_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AudioManagement_SpatialAudioMode_Status.MSG_OFFSET + AudioManagement_SpatialAudioMode_Status.SIZE)
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
            self.hdr.SetMessageID(AudioManagement_SpatialAudioMode_Status.ID)
            self.hdr.SetDataLength(AudioManagement_SpatialAudioMode_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AudioManagement.SpatialAudioMode.Status"
    # Accessors
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetDesired(self, enumAsInt=0):
        """Desired spatial audio mode (based, e.g., on BMAP API calls or user selection via physical interface)."""
        value = struct.unpack_from('B', self.rawBuffer(), AudioManagement_SpatialAudioMode_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = AudioManagement_SpatialAudioMode_Status.ReverseSpatialAudioModeTypes.get(value, value)
        return value
    
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetDesired(self, value):
        """Desired spatial audio mode (based, e.g., on BMAP API calls or user selection via physical interface)."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = AudioManagement_SpatialAudioMode_Status.SpatialAudioModeTypes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), AudioManagement_SpatialAudioMode_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Desired",type="enumeration",units="Enum",minVal="0",maxVal="255",description="Desired spatial audio mode (based, e.g., on BMAP API calls or user selection via physical interface).",get=GetDesired,set=SetDesired,count=1, bitfieldInfo = [], enum = [SpatialAudioModeTypes, ReverseSpatialAudioModeTypes])\
    ]

Messaging.Register("AudioManagement.SpatialAudioMode.Status", AudioManagement_SpatialAudioMode_Status.ID, AudioManagement_SpatialAudioMode_Status)

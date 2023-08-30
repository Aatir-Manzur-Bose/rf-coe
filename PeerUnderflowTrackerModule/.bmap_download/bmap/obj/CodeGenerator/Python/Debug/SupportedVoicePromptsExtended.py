#    obj/CodeGenerator/Python/Debug/SupportedVoicePromptsExtended.py
#    Created 27/07/2023 at 10:10:19 from:
#        Messages = messages/Debug/SupportedVoicePromptsExtended.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_SupportedVoicePromptsExtended_Get :
    ID = 33217
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 28), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (28, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_SupportedVoicePromptsExtended_Get.MSG_OFFSET + Debug_SupportedVoicePromptsExtended_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_SupportedVoicePromptsExtended_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_SupportedVoicePromptsExtended_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_SupportedVoicePromptsExtended_Get.MSG_OFFSET + Debug_SupportedVoicePromptsExtended_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_SupportedVoicePromptsExtended_Get.ID)
            self.hdr.SetDataLength(Debug_SupportedVoicePromptsExtended_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.SupportedVoicePromptsExtended.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.SupportedVoicePromptsExtended.Get", Debug_SupportedVoicePromptsExtended_Get.ID, Debug_SupportedVoicePromptsExtended_Get)
#    obj/CodeGenerator/Python/Debug/SupportedVoicePromptsExtended.py
#    Created 27/07/2023 at 10:10:19 from:
#        Messages = messages/Debug/SupportedVoicePromptsExtended.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_SupportedVoicePromptsExtended_Status :
    ID = 33219
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    VoicePromptsID = OrderedDict([("Connected", 0), ("ConnToDev", 1), ("ConnToDev2", 2), ("Disconnected", 3), ("DisconnDev", 4), ("ReadyToConn", 5), ("ReadyToConnDev2", 6), ("ConnectingToDev", 7), ("DevLost", 8), ("DevNotFound", 9), ("BTDevListCleared", 10), ("VoicePromptsOn", 11), ("VoicePromptsOff", 12), ("Language", 13), ("CallFromName", 14), ("CallFromNumber", 15), ("CallFromUnknown", 16), ("CallIgnored", 17), ("CallEnded", 18), ("SwitchingCalls", 19), ("ConfCall", 20), ("Muted", 21), ("Unmuted", 22), ("DownloadBoseApp", 23), ("BluetoothOff", 24), ("UsbAudio", 25), ("AuxAudio", 26)])
    ReverseVoicePromptsID = OrderedDict([(0, "Connected"), (1, "ConnToDev"), (2, "ConnToDev2"), (3, "Disconnected"), (4, "DisconnDev"), (5, "ReadyToConn"), (6, "ReadyToConnDev2"), (7, "ConnectingToDev"), (8, "DevLost"), (9, "DevNotFound"), (10, "BTDevListCleared"), (11, "VoicePromptsOn"), (12, "VoicePromptsOff"), (13, "Language"), (14, "CallFromName"), (15, "CallFromNumber"), (16, "CallFromUnknown"), (17, "CallIgnored"), (18, "CallEnded"), (19, "SwitchingCalls"), (20, "ConfCall"), (21, "Muted"), (22, "Unmuted"), (23, "DownloadBoseApp"), (24, "BluetoothOff"), (25, "UsbAudio"), (26, "AuxAudio")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 28), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (28, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_SupportedVoicePromptsExtended_Status.MSG_OFFSET + Debug_SupportedVoicePromptsExtended_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_SupportedVoicePromptsExtended_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_SupportedVoicePromptsExtended_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_SupportedVoicePromptsExtended_Status.MSG_OFFSET + Debug_SupportedVoicePromptsExtended_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_SupportedVoicePromptsExtended_Status.ID)
            self.hdr.SetDataLength(Debug_SupportedVoicePromptsExtended_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.SupportedVoicePromptsExtended.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetVoicePrompts(self, enumAsInt=0):
        """List of extended supported voice prompts."""
        value = struct.unpack_from('>H', self.rawBuffer(), Debug_SupportedVoicePromptsExtended_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_SupportedVoicePromptsExtended_Status.ReverseVoicePromptsID.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetVoicePrompts(self, value):
        """List of extended supported voice prompts."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_SupportedVoicePromptsExtended_Status.VoicePromptsID.get(value, defaultValue)
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), Debug_SupportedVoicePromptsExtended_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="VoicePrompts",type="enumeration",units="",minVal="0",maxVal="65535",description="List of extended supported voice prompts.",get=GetVoicePrompts,set=SetVoicePrompts,count=1, bitfieldInfo = [], enum = [VoicePromptsID, ReverseVoicePromptsID])\
    ]

Messaging.Register("Debug.SupportedVoicePromptsExtended.Status", Debug_SupportedVoicePromptsExtended_Status.ID, Debug_SupportedVoicePromptsExtended_Status)

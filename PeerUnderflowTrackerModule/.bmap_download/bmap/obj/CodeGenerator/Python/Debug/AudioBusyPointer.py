#    obj/CodeGenerator/Python/Debug/AudioBusyPointer.py
#    Created 27/07/2023 at 10:10:04 from:
#        Messages = messages/Debug/AudioBusyPointer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_AudioBusyPointer_Get :
    ID = 33473
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 44), ("Operator", 1)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (44, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_Get.MSG_OFFSET + Debug_AudioBusyPointer_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_AudioBusyPointer_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_AudioBusyPointer_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_Get.MSG_OFFSET + Debug_AudioBusyPointer_Get.SIZE)
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
            self.hdr.SetMessageID(Debug_AudioBusyPointer_Get.ID)
            self.hdr.SetDataLength(Debug_AudioBusyPointer_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.AudioBusyPointer.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Debug.AudioBusyPointer.Get", Debug_AudioBusyPointer_Get.ID, Debug_AudioBusyPointer_Get)
#    obj/CodeGenerator/Python/Debug/AudioBusyPointer.py
#    Created 27/07/2023 at 10:10:04 from:
#        Messages = messages/Debug/AudioBusyPointer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_AudioBusyPointer_Status :
    ID = 33475
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    AudioBusyTasks = OrderedDict([("NoTask", 0), ("csr_sbc_decoder_plugin", 1), ("csr_aptx_decoder_plugin", 2), ("csr_aptx_acl_sprint_decoder_plugin", 3), ("csr_aac_decoder_plugin", 4), ("csr_aptxhd_decoder_plugin", 5), ("csr_tws_master_sbc_decoder_plugin", 6), ("csr_tws_master_aptx_decoder_plugin", 7), ("csr_tws_master_aac_decoder_plugin", 8), ("csr_ba_sbc_decoder_plugin", 9), ("csr_ba_aac_decoder_plugin", 10), ("csr_tws_slave_sbc_decoder_plugin", 11), ("csr_tws_slave_aptx_decoder_plugin", 12), ("csr_tws_slave_aac_decoder_plugin", 13), ("non_a2dp_plugin", 14)])
    ReverseAudioBusyTasks = OrderedDict([(0, "NoTask"), (1, "csr_sbc_decoder_plugin"), (2, "csr_aptx_decoder_plugin"), (3, "csr_aptx_acl_sprint_decoder_plugin"), (4, "csr_aac_decoder_plugin"), (5, "csr_aptxhd_decoder_plugin"), (6, "csr_tws_master_sbc_decoder_plugin"), (7, "csr_tws_master_aptx_decoder_plugin"), (8, "csr_tws_master_aac_decoder_plugin"), (9, "csr_ba_sbc_decoder_plugin"), (10, "csr_ba_aac_decoder_plugin"), (11, "csr_tws_slave_sbc_decoder_plugin"), (12, "csr_tws_slave_aptx_decoder_plugin"), (13, "csr_tws_slave_aac_decoder_plugin"), (14, "non_a2dp_plugin")])
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 44), ("Operator", 3)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (44, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_Status.MSG_OFFSET + Debug_AudioBusyPointer_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_AudioBusyPointer_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_AudioBusyPointer_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_Status.MSG_OFFSET + Debug_AudioBusyPointer_Status.SIZE)
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
            self.hdr.SetMessageID(Debug_AudioBusyPointer_Status.ID)
            self.hdr.SetDataLength(Debug_AudioBusyPointer_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.AudioBusyPointer.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetAudioBusyPointer(self, enumAsInt=0):
        """Specifies which task is loaded for the Audio Busy pointer."""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_AudioBusyPointer_Status.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Debug_AudioBusyPointer_Status.ReverseAudioBusyTasks.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetAudioBusyPointer(self, value):
        """Specifies which task is loaded for the Audio Busy pointer."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Debug_AudioBusyPointer_Status.AudioBusyTasks.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_AudioBusyPointer_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="AudioBusyPointer",type="enumeration",units="",minVal="0",maxVal="255",description="Specifies which task is loaded for the Audio Busy pointer.",get=GetAudioBusyPointer,set=SetAudioBusyPointer,count=1, bitfieldInfo = [], enum = [AudioBusyTasks, ReverseAudioBusyTasks])\
    ]

Messaging.Register("Debug.AudioBusyPointer.Status", Debug_AudioBusyPointer_Status.ID, Debug_AudioBusyPointer_Status)
#    obj/CodeGenerator/Python/Debug/AudioBusyPointer.py
#    Created 27/07/2023 at 10:10:04 from:
#        Messages = messages/Debug/AudioBusyPointer.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Debug_AudioBusyPointer_SetGet :
    ID = 33474
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 8), ("Function", 44), ("Operator", 2)])
    ReverseIDs = OrderedDict([(8, "FunctionBlock"), (44, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_SetGet.MSG_OFFSET + Debug_AudioBusyPointer_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Debug_AudioBusyPointer_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Debug_AudioBusyPointer_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Debug_AudioBusyPointer_SetGet.MSG_OFFSET + Debug_AudioBusyPointer_SetGet.SIZE)
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
            self.hdr.SetMessageID(Debug_AudioBusyPointer_SetGet.ID)
            self.hdr.SetDataLength(Debug_AudioBusyPointer_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Debug.AudioBusyPointer.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetAudioBusyPointer(self):
        """Specifies which task is loaded for the Audio Busy pointer."""
        value = struct.unpack_from('B', self.rawBuffer(), Debug_AudioBusyPointer_SetGet.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetAudioBusyPointer(self, value):
        """Specifies which task is loaded for the Audio Busy pointer."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Debug_AudioBusyPointer_SetGet.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="AudioBusyPointer",type="int",units="",minVal="0",maxVal="255",description="Specifies which task is loaded for the Audio Busy pointer.",get=GetAudioBusyPointer,set=SetAudioBusyPointer,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Debug.AudioBusyPointer.SetGet", Debug_AudioBusyPointer_SetGet.ID, Debug_AudioBusyPointer_SetGet)

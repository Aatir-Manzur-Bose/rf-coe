#    obj/CodeGenerator/Python/Manufacturing/SpeakerTrim.py
#    Created 27/07/2023 at 10:10:55 from:
#        Messages = messages/Manufacturing/SpeakerTrim.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_SpeakerTrim_Get :
    ID = 94273
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 4), ("Operator", 1)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (4, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Get.MSG_OFFSET + Manufacturing_SpeakerTrim_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_SpeakerTrim_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_SpeakerTrim_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Get.MSG_OFFSET + Manufacturing_SpeakerTrim_Get.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_SpeakerTrim_Get.ID)
            self.hdr.SetDataLength(Manufacturing_SpeakerTrim_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.SpeakerTrim.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Manufacturing.SpeakerTrim.Get", Manufacturing_SpeakerTrim_Get.ID, Manufacturing_SpeakerTrim_Get)
#    obj/CodeGenerator/Python/Manufacturing/SpeakerTrim.py
#    Created 27/07/2023 at 10:10:55 from:
#        Messages = messages/Manufacturing/SpeakerTrim.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_SpeakerTrim_SetGet :
    ID = 94274
    SIZE = 3
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    SpeakerID = OrderedDict([("Speaker0", 0), ("Speaker1", 1), ("Speaker2", 2), ("Speaker3", 3)])
    ReverseSpeakerID = OrderedDict([(0, "Speaker0"), (1, "Speaker1"), (2, "Speaker2"), (3, "Speaker3")])
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 4), ("Operator", 2)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (4, "Function"), (2, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + Manufacturing_SpeakerTrim_SetGet.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_SpeakerTrim_SetGet.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_SpeakerTrim_SetGet.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + Manufacturing_SpeakerTrim_SetGet.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_SpeakerTrim_SetGet.ID)
            self.hdr.SetDataLength(Manufacturing_SpeakerTrim_SetGet.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.SpeakerTrim.SetGet"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetSpeaker(self, enumAsInt=0):
        """Which speaker."""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Manufacturing_SpeakerTrim_SetGet.ReverseSpeakerID.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetTrimValue(self):
        """Speaker Trim value. Valid range -5400 to 5400."""
        value = struct.unpack_from('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetSpeaker(self, value):
        """Which speaker."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Manufacturing_SpeakerTrim_SetGet.SpeakerID.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetTrimValue(self, value):
        """Speaker Trim value. Valid range -5400 to 5400."""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_SetGet.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Speaker",type="enumeration",units="",minVal="0",maxVal="255",description="Which speaker.",get=GetSpeaker,set=SetSpeaker,count=1, bitfieldInfo = [], enum = [SpeakerID, ReverseSpeakerID]),\
        FieldInfo(name="TrimValue",type="int",units="",minVal="-32768",maxVal="32767",description="Speaker Trim value. Valid range -5400 to 5400.",get=GetTrimValue,set=SetTrimValue,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.SpeakerTrim.SetGet", Manufacturing_SpeakerTrim_SetGet.ID, Manufacturing_SpeakerTrim_SetGet)
#    obj/CodeGenerator/Python/Manufacturing/SpeakerTrim.py
#    Created 27/07/2023 at 10:10:55 from:
#        Messages = messages/Manufacturing/SpeakerTrim.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_SpeakerTrim_Status :
    ID = 94275
    SIZE = 9
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 4), ("Operator", 3)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (4, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Status.MSG_OFFSET + Manufacturing_SpeakerTrim_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_SpeakerTrim_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_SpeakerTrim_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Status.MSG_OFFSET + Manufacturing_SpeakerTrim_Status.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_SpeakerTrim_Status.ID)
            self.hdr.SetDataLength(Manufacturing_SpeakerTrim_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.SpeakerTrim.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetNumSpeakersSupported(self):
        """Number of speakers supported by this product. Max is 4."""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def GetTrim0(self):
        """Trim Value of Speaker."""
        value = struct.unpack_from('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 1)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def GetTrim1(self):
        """Trim Value of Speaker."""
        value = struct.unpack_from('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 3)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('5')
    @msg.size('2')
    @msg.count(1)
    def GetTrim2(self):
        """Trim Value of Speaker."""
        value = struct.unpack_from('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('7')
    @msg.size('2')
    @msg.count(1)
    def GetTrim3(self):
        """Trim Value of Speaker."""
        value = struct.unpack_from('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 7)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetNumSpeakersSupported(self, value):
        """Number of speakers supported by this product. Max is 4."""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('1')
    @msg.size('2')
    @msg.count(1)
    def SetTrim0(self, value):
        """Trim Value of Speaker."""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 1, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('3')
    @msg.size('2')
    @msg.count(1)
    def SetTrim1(self, value):
        """Trim Value of Speaker."""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 3, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('5')
    @msg.size('2')
    @msg.count(1)
    def SetTrim2(self, value):
        """Trim Value of Speaker."""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 5, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('-32768')
    @msg.maxVal('32767')
    @msg.offset('7')
    @msg.size('2')
    @msg.count(1)
    def SetTrim3(self, value):
        """Trim Value of Speaker."""
        tmp = min(max(value, -32768), 32767)
        struct.pack_into('>h', self.rawBuffer(), Manufacturing_SpeakerTrim_Status.MSG_OFFSET + 7, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="NumSpeakersSupported",type="int",units="",minVal="0",maxVal="255",description="Number of speakers supported by this product. Max is 4.",get=GetNumSpeakersSupported,set=SetNumSpeakersSupported,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Trim0",type="int",units="",minVal="-32768",maxVal="32767",description="Trim Value of Speaker.",get=GetTrim0,set=SetTrim0,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Trim1",type="int",units="",minVal="-32768",maxVal="32767",description="Trim Value of Speaker.",get=GetTrim1,set=SetTrim1,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Trim2",type="int",units="",minVal="-32768",maxVal="32767",description="Trim Value of Speaker.",get=GetTrim2,set=SetTrim2,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Trim3",type="int",units="",minVal="-32768",maxVal="32767",description="Trim Value of Speaker.",get=GetTrim3,set=SetTrim3,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Manufacturing.SpeakerTrim.Status", Manufacturing_SpeakerTrim_Status.ID, Manufacturing_SpeakerTrim_Status)
#    obj/CodeGenerator/Python/Manufacturing/SpeakerTrim.py
#    Created 27/07/2023 at 10:10:55 from:
#        Messages = messages/Manufacturing/SpeakerTrim.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Manufacturing_SpeakerTrim_Error :
    ID = 94276
    SIZE = 1
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    ErrorResponseCodes = OrderedDict([("Length", 1), ("Checksum", 2), ("FBlockNotSupported", 3), ("FunctionNotSupported", 4), ("OperatorNotSupported", 5), ("InvalidData", 6), ("DataNotAvailable", 7), ("RunTime", 8), ("Timeout", 9), ("InvalidState", 10), ("DeviceNotFound", 11), ("Busy", 12), ("UnableToConnectTimeout", 13), ("UnableToConnectSourceDeviceKeyMissing", 14), ("OTAFirmwareUpdateInProgress", 15), ("LowBatteryVoltage", 16), ("ChargerNotConnected", 17), ("UpdateNotAllowed", 18), ("UnknownPortNumber", 19), ("InsecureTransport", 20), ("InvalidOTPKey", 21), ("OutOfMemory", 22), ("CryptoProcessingError", 23), ("FeatureLocked", 24), ("FunctionBlockSpecificErrorCode", 255)])
    ReverseErrorResponseCodes = OrderedDict([(1, "Length"), (2, "Checksum"), (3, "FBlockNotSupported"), (4, "FunctionNotSupported"), (5, "OperatorNotSupported"), (6, "InvalidData"), (7, "DataNotAvailable"), (8, "RunTime"), (9, "Timeout"), (10, "InvalidState"), (11, "DeviceNotFound"), (12, "Busy"), (13, "UnableToConnectTimeout"), (14, "UnableToConnectSourceDeviceKeyMissing"), (15, "OTAFirmwareUpdateInProgress"), (16, "LowBatteryVoltage"), (17, "ChargerNotConnected"), (18, "UpdateNotAllowed"), (19, "UnknownPortNumber"), (20, "InsecureTransport"), (21, "InvalidOTPKey"), (22, "OutOfMemory"), (23, "CryptoProcessingError"), (24, "FeatureLocked"), (255, "FunctionBlockSpecificErrorCode")])
    IDs = OrderedDict([("FunctionBlock", 23), ("Function", 4), ("Operator", 4)])
    ReverseIDs = OrderedDict([(23, "FunctionBlock"), (4, "Function"), (4, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Error.MSG_OFFSET + Manufacturing_SpeakerTrim_Error.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Manufacturing_SpeakerTrim_Error.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Manufacturing_SpeakerTrim_Error.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Manufacturing_SpeakerTrim_Error.MSG_OFFSET + Manufacturing_SpeakerTrim_Error.SIZE)
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
            self.hdr.SetMessageID(Manufacturing_SpeakerTrim_Error.ID)
            self.hdr.SetDataLength(Manufacturing_SpeakerTrim_Error.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Manufacturing.SpeakerTrim.Error"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetErrorCode(self, enumAsInt=0):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), Manufacturing_SpeakerTrim_Error.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Manufacturing_SpeakerTrim_Error.ReverseErrorResponseCodes.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetErrorCode(self, value):
        """"""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Manufacturing_SpeakerTrim_Error.ErrorResponseCodes.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Manufacturing_SpeakerTrim_Error.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ErrorCode",type="enumeration",units="",minVal="0",maxVal="255",description="",get=GetErrorCode,set=SetErrorCode,count=1, bitfieldInfo = [], enum = [ErrorResponseCodes, ReverseErrorResponseCodes])\
    ]

Messaging.Register("Manufacturing.SpeakerTrim.Error", Manufacturing_SpeakerTrim_Error.ID, Manufacturing_SpeakerTrim_Error)

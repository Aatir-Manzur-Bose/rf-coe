#    obj/CodeGenerator/Python/ProductInfo/GetAllFBlocks.py
#    Created 27/07/2023 at 10:11:00 from:
#        Messages = messages/ProductInfo/GetAllFBlocks.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_GetAllFBlocks_Start :
    ID = 37
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 2), ("Operator", 5)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (2, "Function"), (5, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Start.MSG_OFFSET + ProductInfo_GetAllFBlocks_Start.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_GetAllFBlocks_Start.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_GetAllFBlocks_Start.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Start.MSG_OFFSET + ProductInfo_GetAllFBlocks_Start.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_GetAllFBlocks_Start.ID)
            self.hdr.SetDataLength(ProductInfo_GetAllFBlocks_Start.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.GetAllFBlocks.Start"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("ProductInfo.GetAllFBlocks.Start", ProductInfo_GetAllFBlocks_Start.ID, ProductInfo_GetAllFBlocks_Start)
#    obj/CodeGenerator/Python/ProductInfo/GetAllFBlocks.py
#    Created 27/07/2023 at 10:11:00 from:
#        Messages = messages/ProductInfo/GetAllFBlocks.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_GetAllFBlocks_Processing :
    ID = 39
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 2), ("Operator", 7)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (2, "Function"), (7, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Processing.MSG_OFFSET + ProductInfo_GetAllFBlocks_Processing.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_GetAllFBlocks_Processing.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_GetAllFBlocks_Processing.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Processing.MSG_OFFSET + ProductInfo_GetAllFBlocks_Processing.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_GetAllFBlocks_Processing.ID)
            self.hdr.SetDataLength(ProductInfo_GetAllFBlocks_Processing.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.GetAllFBlocks.Processing"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("ProductInfo.GetAllFBlocks.Processing", ProductInfo_GetAllFBlocks_Processing.ID, ProductInfo_GetAllFBlocks_Processing)
#    obj/CodeGenerator/Python/ProductInfo/GetAllFBlocks.py
#    Created 27/07/2023 at 10:11:00 from:
#        Messages = messages/ProductInfo/GetAllFBlocks.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_GetAllFBlocks_Result :
    ID = 38
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 2), ("Operator", 6)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (2, "Function"), (6, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Result.MSG_OFFSET + ProductInfo_GetAllFBlocks_Result.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_GetAllFBlocks_Result.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_GetAllFBlocks_Result.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Result.MSG_OFFSET + ProductInfo_GetAllFBlocks_Result.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_GetAllFBlocks_Result.ID)
            self.hdr.SetDataLength(ProductInfo_GetAllFBlocks_Result.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.GetAllFBlocks.Result"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("ProductInfo.GetAllFBlocks.Result", ProductInfo_GetAllFBlocks_Result.ID, ProductInfo_GetAllFBlocks_Result)
#    obj/CodeGenerator/Python/ProductInfo/GetAllFBlocks.py
#    Created 27/07/2023 at 10:11:00 from:
#        Messages = messages/ProductInfo/GetAllFBlocks.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_GetAllFBlocks_Get :
    ID = 33
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 2), ("Operator", 1)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (2, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Get.MSG_OFFSET + ProductInfo_GetAllFBlocks_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_GetAllFBlocks_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_GetAllFBlocks_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Get.MSG_OFFSET + ProductInfo_GetAllFBlocks_Get.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_GetAllFBlocks_Get.ID)
            self.hdr.SetDataLength(ProductInfo_GetAllFBlocks_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.GetAllFBlocks.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("ProductInfo.GetAllFBlocks.Get", ProductInfo_GetAllFBlocks_Get.ID, ProductInfo_GetAllFBlocks_Get)
#    obj/CodeGenerator/Python/ProductInfo/GetAllFBlocks.py
#    Created 27/07/2023 at 10:11:00 from:
#        Messages = messages/ProductInfo/GetAllFBlocks.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class ProductInfo_GetAllFBlocks_Status :
    ID = 35
    SIZE = 4
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 0), ("Function", 2), ("Operator", 3)])
    ReverseIDs = OrderedDict([(0, "FunctionBlock"), (2, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Status.MSG_OFFSET + ProductInfo_GetAllFBlocks_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, ProductInfo_GetAllFBlocks_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, ProductInfo_GetAllFBlocks_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(ProductInfo_GetAllFBlocks_Status.MSG_OFFSET + ProductInfo_GetAllFBlocks_Status.SIZE)
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
            self.hdr.SetMessageID(ProductInfo_GetAllFBlocks_Status.ID)
            self.hdr.SetDataLength(ProductInfo_GetAllFBlocks_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "ProductInfo.GetAllFBlocks.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def GetSupportedFunctionBlocks(self):
        """Bitfield of supported Function Blocks (MSB first)."""
        value = struct.unpack_from('>L', self.rawBuffer(), ProductInfo_GetAllFBlocks_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetProductInfo(self):
        """ProductInfo"""
        value = (self.GetSupportedFunctionBlocks() >> 0) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetSettings(self):
        """Settings"""
        value = (self.GetSupportedFunctionBlocks() >> 1) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetStatus(self):
        """Status"""
        value = (self.GetSupportedFunctionBlocks() >> 2) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetFirmwareUpdate(self):
        """FirmwareUpdate"""
        value = (self.GetSupportedFunctionBlocks() >> 3) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetDeviceManagement(self):
        """DeviceManagement"""
        value = (self.GetSupportedFunctionBlocks() >> 4) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAudioManagement(self):
        """AudioManagement"""
        value = (self.GetSupportedFunctionBlocks() >> 5) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetCall(self):
        """Call"""
        value = (self.GetSupportedFunctionBlocks() >> 6) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetControl(self):
        """Control"""
        value = (self.GetSupportedFunctionBlocks() >> 7) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetDebug(self):
        """Debug"""
        value = (self.GetSupportedFunctionBlocks() >> 8) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetNotification(self):
        """Notification"""
        value = (self.GetSupportedFunctionBlocks() >> 9) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetReserved1(self):
        """Reserved1"""
        value = (self.GetSupportedFunctionBlocks() >> 10) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetReserved2(self):
        """Reserved2"""
        value = (self.GetSupportedFunctionBlocks() >> 11) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetHearingAssistance(self):
        """HearingAssistance"""
        value = (self.GetSupportedFunctionBlocks() >> 12) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetDataCollection(self):
        """DataCollection"""
        value = (self.GetSupportedFunctionBlocks() >> 13) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetHeartRateMonitor(self):
        """HeartRateMonitor"""
        value = (self.GetSupportedFunctionBlocks() >> 14) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetPeer(self):
        """Peer"""
        value = (self.GetSupportedFunctionBlocks() >> 15) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetVPA(self):
        """VPA"""
        value = (self.GetSupportedFunctionBlocks() >> 16) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetWiFi(self):
        """WiFi"""
        value = (self.GetSupportedFunctionBlocks() >> 17) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAuth(self):
        """Auth"""
        value = (self.GetSupportedFunctionBlocks() >> 18) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetExperimental(self):
        """Experimental"""
        value = (self.GetSupportedFunctionBlocks() >> 19) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetCloud(self):
        """Cloud"""
        value = (self.GetSupportedFunctionBlocks() >> 20) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAugmentedReality(self):
        """AugmentedReality"""
        value = (self.GetSupportedFunctionBlocks() >> 21) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetPrint(self):
        """Print"""
        value = (self.GetSupportedFunctionBlocks() >> 22) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetManufacturing(self):
        """Manufacturing"""
        value = (self.GetSupportedFunctionBlocks() >> 23) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetSensorInterface(self):
        """SensorInterface"""
        value = (self.GetSupportedFunctionBlocks() >> 24) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetBatteryDebug(self):
        """BatteryDebug"""
        value = (self.GetSupportedFunctionBlocks() >> 25) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetSmartANRPlatform(self):
        """SmartANRPlatform"""
        value = (self.GetSupportedFunctionBlocks() >> 26) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetEarbudDebug(self):
        """EarbudDebug"""
        value = (self.GetSupportedFunctionBlocks() >> 27) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAudioStream(self):
        """AudioStream"""
        value = (self.GetSupportedFunctionBlocks() >> 28) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetCaseDebug(self):
        """CaseDebug"""
        value = (self.GetSupportedFunctionBlocks() >> 29) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetMTIDVI(self):
        """MTIDVI"""
        value = (self.GetSupportedFunctionBlocks() >> 30) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def GetAudioModes(self):
        """AudioModes"""
        value = (self.GetSupportedFunctionBlocks() >> 31) & 0x1
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def SetSupportedFunctionBlocks(self, value):
        """Bitfield of supported Function Blocks (MSB first)."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), ProductInfo_GetAllFBlocks_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetProductInfo(self, value):
        """ProductInfo"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 0)) | ((tmp & 0x1) << 0))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetSettings(self, value):
        """Settings"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 1)) | ((tmp & 0x1) << 1))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetStatus(self, value):
        """Status"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 2)) | ((tmp & 0x1) << 2))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetFirmwareUpdate(self, value):
        """FirmwareUpdate"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 3)) | ((tmp & 0x1) << 3))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetDeviceManagement(self, value):
        """DeviceManagement"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 4)) | ((tmp & 0x1) << 4))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAudioManagement(self, value):
        """AudioManagement"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 5)) | ((tmp & 0x1) << 5))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetCall(self, value):
        """Call"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 6)) | ((tmp & 0x1) << 6))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetControl(self, value):
        """Control"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 7)) | ((tmp & 0x1) << 7))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetDebug(self, value):
        """Debug"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 8)) | ((tmp & 0x1) << 8))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetNotification(self, value):
        """Notification"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 9)) | ((tmp & 0x1) << 9))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetReserved1(self, value):
        """Reserved1"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 10)) | ((tmp & 0x1) << 10))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetReserved2(self, value):
        """Reserved2"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 11)) | ((tmp & 0x1) << 11))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetHearingAssistance(self, value):
        """HearingAssistance"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 12)) | ((tmp & 0x1) << 12))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetDataCollection(self, value):
        """DataCollection"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 13)) | ((tmp & 0x1) << 13))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetHeartRateMonitor(self, value):
        """HeartRateMonitor"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 14)) | ((tmp & 0x1) << 14))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetPeer(self, value):
        """Peer"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 15)) | ((tmp & 0x1) << 15))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetVPA(self, value):
        """VPA"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 16)) | ((tmp & 0x1) << 16))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetWiFi(self, value):
        """WiFi"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 17)) | ((tmp & 0x1) << 17))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAuth(self, value):
        """Auth"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 18)) | ((tmp & 0x1) << 18))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetExperimental(self, value):
        """Experimental"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 19)) | ((tmp & 0x1) << 19))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetCloud(self, value):
        """Cloud"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 20)) | ((tmp & 0x1) << 20))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAugmentedReality(self, value):
        """AugmentedReality"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 21)) | ((tmp & 0x1) << 21))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetPrint(self, value):
        """Print"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 22)) | ((tmp & 0x1) << 22))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetManufacturing(self, value):
        """Manufacturing"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 23)) | ((tmp & 0x1) << 23))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetSensorInterface(self, value):
        """SensorInterface"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 24)) | ((tmp & 0x1) << 24))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetBatteryDebug(self, value):
        """BatteryDebug"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 25)) | ((tmp & 0x1) << 25))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetSmartANRPlatform(self, value):
        """SmartANRPlatform"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 26)) | ((tmp & 0x1) << 26))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetEarbudDebug(self, value):
        """EarbudDebug"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 27)) | ((tmp & 0x1) << 27))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAudioStream(self, value):
        """AudioStream"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 28)) | ((tmp & 0x1) << 28))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetCaseDebug(self, value):
        """CaseDebug"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 29)) | ((tmp & 0x1) << 29))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetMTIDVI(self, value):
        """MTIDVI"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 30)) | ((tmp & 0x1) << 30))
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('1')
    @msg.offset('0')
    @msg.size('0')
    @msg.count(1)
    def SetAudioModes(self, value):
        """AudioModes"""
        tmp = min(max(value, 0), 1)
        self.SetSupportedFunctionBlocks((self.GetSupportedFunctionBlocks() & ~(0x1 << 31)) | ((tmp & 0x1) << 31))
    

    # Reflection information
    fields = [ \
        FieldInfo(name="SupportedFunctionBlocks",type="int",units="",minVal="0",maxVal="4294967295",description="Bitfield of supported Function Blocks (MSB first).",get=GetSupportedFunctionBlocks,set=SetSupportedFunctionBlocks,count=1, bitfieldInfo = [\
            BitFieldInfo(name="ProductInfo",type="int",units="",minVal="0",maxVal="1",description="ProductInfo",get=GetProductInfo,set=SetProductInfo, enum = []),\
            BitFieldInfo(name="Settings",type="int",units="",minVal="0",maxVal="1",description="Settings",get=GetSettings,set=SetSettings, enum = []),\
            BitFieldInfo(name="Status",type="int",units="",minVal="0",maxVal="1",description="Status",get=GetStatus,set=SetStatus, enum = []),\
            BitFieldInfo(name="FirmwareUpdate",type="int",units="",minVal="0",maxVal="1",description="FirmwareUpdate",get=GetFirmwareUpdate,set=SetFirmwareUpdate, enum = []),\
            BitFieldInfo(name="DeviceManagement",type="int",units="",minVal="0",maxVal="1",description="DeviceManagement",get=GetDeviceManagement,set=SetDeviceManagement, enum = []),\
            BitFieldInfo(name="AudioManagement",type="int",units="",minVal="0",maxVal="1",description="AudioManagement",get=GetAudioManagement,set=SetAudioManagement, enum = []),\
            BitFieldInfo(name="Call",type="int",units="",minVal="0",maxVal="1",description="Call",get=GetCall,set=SetCall, enum = []),\
            BitFieldInfo(name="Control",type="int",units="",minVal="0",maxVal="1",description="Control",get=GetControl,set=SetControl, enum = []),\
            BitFieldInfo(name="Debug",type="int",units="",minVal="0",maxVal="1",description="Debug",get=GetDebug,set=SetDebug, enum = []),\
            BitFieldInfo(name="Notification",type="int",units="",minVal="0",maxVal="1",description="Notification",get=GetNotification,set=SetNotification, enum = []),\
            BitFieldInfo(name="Reserved1",type="int",units="",minVal="0",maxVal="1",description="Reserved1",get=GetReserved1,set=SetReserved1, enum = []),\
            BitFieldInfo(name="Reserved2",type="int",units="",minVal="0",maxVal="1",description="Reserved2",get=GetReserved2,set=SetReserved2, enum = []),\
            BitFieldInfo(name="HearingAssistance",type="int",units="",minVal="0",maxVal="1",description="HearingAssistance",get=GetHearingAssistance,set=SetHearingAssistance, enum = []),\
            BitFieldInfo(name="DataCollection",type="int",units="",minVal="0",maxVal="1",description="DataCollection",get=GetDataCollection,set=SetDataCollection, enum = []),\
            BitFieldInfo(name="HeartRateMonitor",type="int",units="",minVal="0",maxVal="1",description="HeartRateMonitor",get=GetHeartRateMonitor,set=SetHeartRateMonitor, enum = []),\
            BitFieldInfo(name="Peer",type="int",units="",minVal="0",maxVal="1",description="Peer",get=GetPeer,set=SetPeer, enum = []),\
            BitFieldInfo(name="VPA",type="int",units="",minVal="0",maxVal="1",description="VPA",get=GetVPA,set=SetVPA, enum = []),\
            BitFieldInfo(name="WiFi",type="int",units="",minVal="0",maxVal="1",description="WiFi",get=GetWiFi,set=SetWiFi, enum = []),\
            BitFieldInfo(name="Auth",type="int",units="",minVal="0",maxVal="1",description="Auth",get=GetAuth,set=SetAuth, enum = []),\
            BitFieldInfo(name="Experimental",type="int",units="",minVal="0",maxVal="1",description="Experimental",get=GetExperimental,set=SetExperimental, enum = []),\
            BitFieldInfo(name="Cloud",type="int",units="",minVal="0",maxVal="1",description="Cloud",get=GetCloud,set=SetCloud, enum = []),\
            BitFieldInfo(name="AugmentedReality",type="int",units="",minVal="0",maxVal="1",description="AugmentedReality",get=GetAugmentedReality,set=SetAugmentedReality, enum = []),\
            BitFieldInfo(name="Print",type="int",units="",minVal="0",maxVal="1",description="Print",get=GetPrint,set=SetPrint, enum = []),\
            BitFieldInfo(name="Manufacturing",type="int",units="",minVal="0",maxVal="1",description="Manufacturing",get=GetManufacturing,set=SetManufacturing, enum = []),\
            BitFieldInfo(name="SensorInterface",type="int",units="",minVal="0",maxVal="1",description="SensorInterface",get=GetSensorInterface,set=SetSensorInterface, enum = []),\
            BitFieldInfo(name="BatteryDebug",type="int",units="",minVal="0",maxVal="1",description="BatteryDebug",get=GetBatteryDebug,set=SetBatteryDebug, enum = []),\
            BitFieldInfo(name="SmartANRPlatform",type="int",units="",minVal="0",maxVal="1",description="SmartANRPlatform",get=GetSmartANRPlatform,set=SetSmartANRPlatform, enum = []),\
            BitFieldInfo(name="EarbudDebug",type="int",units="",minVal="0",maxVal="1",description="EarbudDebug",get=GetEarbudDebug,set=SetEarbudDebug, enum = []),\
            BitFieldInfo(name="AudioStream",type="int",units="",minVal="0",maxVal="1",description="AudioStream",get=GetAudioStream,set=SetAudioStream, enum = []),\
            BitFieldInfo(name="CaseDebug",type="int",units="",minVal="0",maxVal="1",description="CaseDebug",get=GetCaseDebug,set=SetCaseDebug, enum = []),\
            BitFieldInfo(name="MTIDVI",type="int",units="",minVal="0",maxVal="1",description="MTIDVI",get=GetMTIDVI,set=SetMTIDVI, enum = []),\
            BitFieldInfo(name="AudioModes",type="int",units="",minVal="0",maxVal="1",description="AudioModes",get=GetAudioModes,set=SetAudioModes, enum = [])], enum = [])\
    ]

Messaging.Register("ProductInfo.GetAllFBlocks.Status", ProductInfo_GetAllFBlocks_Status.ID, ProductInfo_GetAllFBlocks_Status)

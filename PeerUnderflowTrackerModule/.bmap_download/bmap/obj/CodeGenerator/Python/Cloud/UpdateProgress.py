#    obj/CodeGenerator/Python/Cloud/UpdateProgress.py
#    Created 27/07/2023 at 10:09:59 from:
#        Messages = messages/Cloud/UpdateProgress.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Cloud_UpdateProgress_Get :
    ID = 82017
    SIZE = 0
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 20), ("Function", 6), ("Operator", 1)])
    ReverseIDs = OrderedDict([(20, "FunctionBlock"), (6, "Function"), (1, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Cloud_UpdateProgress_Get.MSG_OFFSET + Cloud_UpdateProgress_Get.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Cloud_UpdateProgress_Get.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Cloud_UpdateProgress_Get.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Cloud_UpdateProgress_Get.MSG_OFFSET + Cloud_UpdateProgress_Get.SIZE)
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
            self.hdr.SetMessageID(Cloud_UpdateProgress_Get.ID)
            self.hdr.SetDataLength(Cloud_UpdateProgress_Get.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Cloud.UpdateProgress.Get"
    # Accessors

    # Reflection information
    fields = [ \
    ]

Messaging.Register("Cloud.UpdateProgress.Get", Cloud_UpdateProgress_Get.ID, Cloud_UpdateProgress_Get)
#    obj/CodeGenerator/Python/Cloud/UpdateProgress.py
#    Created 27/07/2023 at 10:09:59 from:
#        Messages = messages/Cloud/UpdateProgress.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Cloud_UpdateProgress_Status :
    ID = 82019
    SIZE = 21
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    CloudUpdateStates = OrderedDict([("Error", 0), ("CheckingForCloudUpdate", 1), ("NoUpdate", 2), ("Downloading", 3), ("InstallationPending", 4), ("Installing", 5), ("CheckingForLocalUpdate", 6), ("CancelInstallationPending", 7)])
    ReverseCloudUpdateStates = OrderedDict([(0, "Error"), (1, "CheckingForCloudUpdate"), (2, "NoUpdate"), (3, "Downloading"), (4, "InstallationPending"), (5, "Installing"), (6, "CheckingForLocalUpdate"), (7, "CancelInstallationPending")])
    IDs = OrderedDict([("FunctionBlock", 20), ("Function", 6), ("Operator", 3)])
    ReverseIDs = OrderedDict([(20, "FunctionBlock"), (6, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Cloud_UpdateProgress_Status.MSG_OFFSET + Cloud_UpdateProgress_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Cloud_UpdateProgress_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Cloud_UpdateProgress_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Cloud_UpdateProgress_Status.MSG_OFFSET + Cloud_UpdateProgress_Status.SIZE)
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
            self.hdr.SetMessageID(Cloud_UpdateProgress_Status.ID)
            self.hdr.SetDataLength(Cloud_UpdateProgress_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Cloud.UpdateProgress.Status"
    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def GetbytesToDownload(self):
        """Total bytes to download. Valid only for Downloading status."""
        value = struct.unpack_from('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('4')
    @msg.size('4')
    @msg.count(1)
    def GetbytesDownloaded(self):
        """Total bytes already downloaded. Valid only for Downloading status."""
        value = struct.unpack_from('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('8')
    @msg.size('4')
    @msg.count(1)
    def GetestimatedInstallDuration(self):
        """Estimated install duration (not including download time) in seconds. This will be 0 for all statuses except Installing and InstallationPending."""
        value = struct.unpack_from('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 8)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('12')
    @msg.size('1')
    @msg.count(1)
    def GetpreviousStatus(self, enumAsInt=0):
        """Previous firmware update status of product."""
        value = struct.unpack_from('B', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 12)[0]
        if not enumAsInt:
            value = Cloud_UpdateProgress_Status.ReverseCloudUpdateStates.get(value, value)
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('13')
    @msg.size('4')
    @msg.count(1)
    def GetpreviousStatusTimestamp(self):
        """Unix timestamp (32-bit unix epoch) when previous status was entered, if known. 0x0 if this value is not known."""
        value = struct.unpack_from('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 13)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('17')
    @msg.size('4')
    @msg.count(1)
    def GetcurrentStatusTimestamp(self):
        """Unix timestamp (32-bit unix epoch) when current status was entered, if known. 0x0 if this value is not known."""
        value = struct.unpack_from('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 17)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('0')
    @msg.size('4')
    @msg.count(1)
    def SetbytesToDownload(self, value):
        """Total bytes to download. Valid only for Downloading status."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('4')
    @msg.size('4')
    @msg.count(1)
    def SetbytesDownloaded(self, value):
        """Total bytes already downloaded. Valid only for Downloading status."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('8')
    @msg.size('4')
    @msg.count(1)
    def SetestimatedInstallDuration(self, value):
        """Estimated install duration (not including download time) in seconds. This will be 0 for all statuses except Installing and InstallationPending."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 8, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('12')
    @msg.size('1')
    @msg.count(1)
    def SetpreviousStatus(self, value):
        """Previous firmware update status of product."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Cloud_UpdateProgress_Status.CloudUpdateStates.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 12, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('13')
    @msg.size('4')
    @msg.count(1)
    def SetpreviousStatusTimestamp(self, value):
        """Unix timestamp (32-bit unix epoch) when previous status was entered, if known. 0x0 if this value is not known."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 13, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('4294967295')
    @msg.offset('17')
    @msg.size('4')
    @msg.count(1)
    def SetcurrentStatusTimestamp(self, value):
        """Unix timestamp (32-bit unix epoch) when current status was entered, if known. 0x0 if this value is not known."""
        tmp = min(max(value, 0), 4294967295)
        struct.pack_into('>L', self.rawBuffer(), Cloud_UpdateProgress_Status.MSG_OFFSET + 17, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="bytesToDownload",type="int",units="",minVal="0",maxVal="4294967295",description="Total bytes to download. Valid only for Downloading status.",get=GetbytesToDownload,set=SetbytesToDownload,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="bytesDownloaded",type="int",units="",minVal="0",maxVal="4294967295",description="Total bytes already downloaded. Valid only for Downloading status.",get=GetbytesDownloaded,set=SetbytesDownloaded,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="estimatedInstallDuration",type="int",units="",minVal="0",maxVal="4294967295",description="Estimated install duration (not including download time) in seconds. This will be 0 for all statuses except Installing and InstallationPending.",get=GetestimatedInstallDuration,set=SetestimatedInstallDuration,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="previousStatus",type="enumeration",units="",minVal="0",maxVal="255",description="Previous firmware update status of product.",get=GetpreviousStatus,set=SetpreviousStatus,count=1, bitfieldInfo = [], enum = [CloudUpdateStates, ReverseCloudUpdateStates]),\
        FieldInfo(name="previousStatusTimestamp",type="int",units="",minVal="0",maxVal="4294967295",description="Unix timestamp (32-bit unix epoch) when previous status was entered, if known. 0x0 if this value is not known.",get=GetpreviousStatusTimestamp,set=SetpreviousStatusTimestamp,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="currentStatusTimestamp",type="int",units="",minVal="0",maxVal="4294967295",description="Unix timestamp (32-bit unix epoch) when current status was entered, if known. 0x0 if this value is not known.",get=GetcurrentStatusTimestamp,set=SetcurrentStatusTimestamp,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("Cloud.UpdateProgress.Status", Cloud_UpdateProgress_Status.ID, Cloud_UpdateProgress_Status)

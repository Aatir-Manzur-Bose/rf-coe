#    obj/CodeGenerator/Python/SmartANRPlatform/Assert.py
#    Created 27/07/2023 at 10:11:10 from:
#        Messages = messages/SmartANRPlatform/Assert.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class SmartANRPlatform_Assert_Status :
    ID = 107027
    SIZE = 250
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    IDs = OrderedDict([("FunctionBlock", 26), ("Function", 33), ("Operator", 3)])
    ReverseIDs = OrderedDict([(26, "FunctionBlock"), (33, "Function"), (3, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(SmartANRPlatform_Assert_Status.MSG_OFFSET + SmartANRPlatform_Assert_Status.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, SmartANRPlatform_Assert_Status.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, SmartANRPlatform_Assert_Status.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(SmartANRPlatform_Assert_Status.MSG_OFFSET + SmartANRPlatform_Assert_Status.SIZE)
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
            self.hdr.SetMessageID(SmartANRPlatform_Assert_Status.ID)
            self.hdr.SetDataLength(SmartANRPlatform_Assert_Status.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "SmartANRPlatform.Assert.Status"
    # Accessors
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(250)
    def GetLog(self):
        """Assert log message (UTF-8 String)"""
        count = 250
        if count > len(self.rawBuffer())-(SmartANRPlatform_Assert_Status.MSG_OFFSET + 0):
            count = len(self.rawBuffer())-(SmartANRPlatform_Assert_Status.MSG_OFFSET + 0)
    
        value = struct.unpack_from(str(count)+'s', self.rawBuffer(), SmartANRPlatform_Assert_Status.MSG_OFFSET + 0)[0]
        ascii_len = str(value).find("\\x00")
        value = str(value)[2:ascii_len]
        return value
    
    @msg.units('ASCII')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(250)
    def SetLog(self, value):
        """Assert log message (UTF-8 String)"""
        tmp = value.encode('utf-8')
        struct.pack_into('250s', self.rawBuffer(), SmartANRPlatform_Assert_Status.MSG_OFFSET + 0, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="Log",type="string",units="ASCII",minVal="0",maxVal="255",description="Assert log message (UTF-8 String)",get=GetLog,set=SetLog,count=1, bitfieldInfo = [], enum = [])\
    ]

Messaging.Register("SmartANRPlatform.Assert.Status", SmartANRPlatform_Assert_Status.ID, SmartANRPlatform_Assert_Status)

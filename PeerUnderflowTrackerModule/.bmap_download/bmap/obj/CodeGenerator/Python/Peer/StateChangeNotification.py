#    obj/CodeGenerator/Python/Peer/StateChangeNotification.py
#    Created 27/07/2023 at 10:10:58 from:
#        Messages = messages/Peer/StateChangeNotification.yaml
#        Template = Template.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class Peer_StateChangeNotification_Set :
    ID = 61504
    SIZE = 2
    MSG_OFFSET = Messaging.hdrSize
    # Enumerations
    PeerSource = OrderedDict([("Reserved", 0), ("Master", 1), ("Puppet", 2)])
    ReversePeerSource = OrderedDict([(0, "Reserved"), (1, "Master"), (2, "Puppet")])
    PeerState = OrderedDict([("Reserved", 0), ("Hibernation", 1), ("Discoverable", 2), ("Connecting", 3), ("ConnectedIdleFromConnecting", 4), ("ConnectedIncomingCall", 5), ("ConnectedInCallFromConnecting", 6), ("Update", 7), ("Error", 8)])
    ReversePeerState = OrderedDict([(0, "Reserved"), (1, "Hibernation"), (2, "Discoverable"), (3, "Connecting"), (4, "ConnectedIdleFromConnecting"), (5, "ConnectedIncomingCall"), (6, "ConnectedInCallFromConnecting"), (7, "Update"), (8, "Error")])
    IDs = OrderedDict([("FunctionBlock", 15), ("Function", 4), ("Operator", 0)])
    ReverseIDs = OrderedDict([(15, "FunctionBlock"), (4, "Function"), (0, "Operator")])
    
    
    #@staticmethod
    #def Create():
    #    message_buffer = ctypes.create_string_buffer(Peer_StateChangeNotification_Set.MSG_OFFSET + Peer_StateChangeNotification_Set.SIZE)
    #
    #    Messaging.hdr.SetMessageID(message_buffer, Peer_StateChangeNotification_Set.ID)
    #    Messaging.hdr.SetDataLength(message_buffer, Peer_StateChangeNotification_Set.SIZE)
    #
    #    return message_buffer

    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(Peer_StateChangeNotification_Set.MSG_OFFSET + Peer_StateChangeNotification_Set.SIZE)
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
            self.hdr.SetMessageID(Peer_StateChangeNotification_Set.ID)
            self.hdr.SetDataLength(Peer_StateChangeNotification_Set.SIZE)
            self.initialize()

    def initialize(self):
            pass

    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "Peer.StateChangeNotification.Set"
    # Accessors
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def GetPeerSource(self, enumAsInt=0):
        """Peer Source."""
        value = struct.unpack_from('B', self.rawBuffer(), Peer_StateChangeNotification_Set.MSG_OFFSET + 0)[0]
        if not enumAsInt:
            value = Peer_StateChangeNotification_Set.ReversePeerSource.get(value, value)
        return value
    
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def GetPeerState(self, enumAsInt=0):
        """Peer State."""
        value = struct.unpack_from('B', self.rawBuffer(), Peer_StateChangeNotification_Set.MSG_OFFSET + 1)[0]
        if not enumAsInt:
            value = Peer_StateChangeNotification_Set.ReversePeerState.get(value, value)
        return value
    
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('0')
    @msg.size('1')
    @msg.count(1)
    def SetPeerSource(self, value):
        """Peer Source."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Peer_StateChangeNotification_Set.PeerSource.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Peer_StateChangeNotification_Set.MSG_OFFSET + 0, tmp)
    
    @msg.units('Enum')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('1')
    @msg.size('1')
    @msg.count(1)
    def SetPeerState(self, value):
        """Peer State."""
        defaultValue = 0
        try:
            value = int(float(value))
        except ValueError:
            pass
        if isinstance(value, int) or value.isdigit():
            defaultValue = int(value)
        value = Peer_StateChangeNotification_Set.PeerState.get(value, defaultValue)
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), Peer_StateChangeNotification_Set.MSG_OFFSET + 1, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="PeerSource",type="enumeration",units="Enum",minVal="0",maxVal="255",description="Peer Source.",get=GetPeerSource,set=SetPeerSource,count=1, bitfieldInfo = [], enum = [PeerSource, ReversePeerSource]),\
        FieldInfo(name="PeerState",type="enumeration",units="Enum",minVal="0",maxVal="255",description="Peer State.",get=GetPeerState,set=SetPeerState,count=1, bitfieldInfo = [], enum = [PeerState, ReversePeerState])\
    ]

Messaging.Register("Peer.StateChangeNotification.Set", Peer_StateChangeNotification_Set.ID, Peer_StateChangeNotification_Set)

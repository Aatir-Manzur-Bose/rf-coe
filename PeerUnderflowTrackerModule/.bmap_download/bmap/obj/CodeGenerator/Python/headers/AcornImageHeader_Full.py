#    obj/CodeGenerator/Python/headers/AcornImageHeader_Full.py
#    Created 27/07/2023 at 10:10:45 from:
#        Messages = messages/headers/AcornImageHeader_Full.yaml
#        Template = HeaderTemplate.py
#        Language = python
#
#                     AUTOGENERATED FILE, DO NOT EDIT
import struct
import ctypes
from collections import OrderedDict
from msgtools.lib.messaging import *
import msgtools.lib.messaging as msg

class AcornImageHeader_Full :
    SIZE = 76
    MSG_OFFSET = 0
    # Enumerations

    #@staticmethod
    #def Create() :
    #    message_buffer = ctypes.create_string_buffer(AcornImageHeader_Full.SIZE)
    #    return message_buffer
    
    def __init__(self, messageBuffer=None):
        doInit = 0
        if messageBuffer == None:
            doInit = 1
            messageBuffer = ctypes.create_string_buffer(AcornImageHeader_Full.SIZE)
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
        if doInit:
            self.initialize()

    def initialize(self):
            pass
    
    def rawBuffer(self):
        # this is a trick to get us to store a copy of a pointer to a buffer, rather than making a copy of the buffer
        return self.msg_buffer_wrapper["msg_buffer"]

    @staticmethod
    def MsgName():
        return "AcornImageHeader_Full"

    def SetMessageID(self, id):
        self.SetImageType(id & 0xffff)

    def GetMessageID(self):
        id = self.GetImageType()
        return id

    # Accessors
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def GetImageType(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 0)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def GetMajorRev(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 2)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def GetMinorRev(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 4)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def GetPatchRev(self):
        """"""
        value = struct.unpack_from('B', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 5)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def GetOffsetStart(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 6)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def GetLenStart(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 8)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def GetDataStart(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 10)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('12')
    @msg.size('2')
    @msg.count(1)
    def GetClockSetupStart(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 12)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('14')
    @msg.size('2')
    @msg.count(1)
    def GetRegisterSetupStart(self):
        """Register start offset from DataStart"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 14)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('16')
    @msg.size('2')
    @msg.count(1)
    def GetProgramStart(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 16)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('18')
    @msg.size('2')
    @msg.count(1)
    def GetBankA_B0_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 18)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('20')
    @msg.size('2')
    @msg.count(1)
    def GetBankA_B1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 20)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('22')
    @msg.size('2')
    @msg.count(1)
    def GetBankA_B2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 22)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('24')
    @msg.size('2')
    @msg.count(1)
    def GetBankA_A1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 24)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('26')
    @msg.size('2')
    @msg.count(1)
    def GetBankA_A2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 26)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('28')
    @msg.size('2')
    @msg.count(1)
    def GetBankB_B0_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 28)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('30')
    @msg.size('2')
    @msg.count(1)
    def GetBankB_B1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 30)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('32')
    @msg.size('2')
    @msg.count(1)
    def GetBankB_B2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 32)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('34')
    @msg.size('2')
    @msg.count(1)
    def GetBankB_A1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 34)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('36')
    @msg.size('2')
    @msg.count(1)
    def GetBankB_A2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 36)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('38')
    @msg.size('2')
    @msg.count(1)
    def GetBankC_B0_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 38)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('40')
    @msg.size('2')
    @msg.count(1)
    def GetBankC_B1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 40)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('42')
    @msg.size('2')
    @msg.count(1)
    def GetBankC_B2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 42)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('44')
    @msg.size('2')
    @msg.count(1)
    def GetBankC_A1_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 44)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('46')
    @msg.size('2')
    @msg.count(1)
    def GetBankC_A2_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 46)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('48')
    @msg.size('2')
    @msg.count(1)
    def GetPreRel_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 48)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('50')
    @msg.size('2')
    @msg.count(1)
    def GetPostRel_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 50)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('52')
    @msg.size('2')
    @msg.count(1)
    def GetComment_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 52)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('54')
    @msg.size('2')
    @msg.count(1)
    def GetCoefficientMap_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 54)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('56')
    @msg.size('2')
    @msg.count(1)
    def GetCRC_Start(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 56)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('58')
    @msg.size('2')
    @msg.count(1)
    def GetClockSetup_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 58)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('60')
    @msg.size('2')
    @msg.count(1)
    def GetRegisterSetup_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 60)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('62')
    @msg.size('2')
    @msg.count(1)
    def GetProgram_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 62)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('64')
    @msg.size('2')
    @msg.count(1)
    def GetCoefficients_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 64)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('66')
    @msg.size('2')
    @msg.count(1)
    def GetPreRel_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 66)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('68')
    @msg.size('2')
    @msg.count(1)
    def GetPostRel_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 68)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('70')
    @msg.size('2')
    @msg.count(1)
    def GetComment_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 70)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('72')
    @msg.size('2')
    @msg.count(1)
    def GetCoefficientMap_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 72)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('74')
    @msg.size('2')
    @msg.count(1)
    def GetCRC_Len(self):
        """"""
        value = struct.unpack_from('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 74)[0]
        return value
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('0')
    @msg.size('2')
    @msg.count(1)
    def SetImageType(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 0, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('2')
    @msg.size('2')
    @msg.count(1)
    def SetMajorRev(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 2, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('4')
    @msg.size('1')
    @msg.count(1)
    def SetMinorRev(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 4, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('255')
    @msg.offset('5')
    @msg.size('1')
    @msg.count(1)
    def SetPatchRev(self, value):
        """"""
        tmp = min(max(value, 0), 255)
        struct.pack_into('B', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 5, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('6')
    @msg.size('2')
    @msg.count(1)
    def SetOffsetStart(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 6, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('8')
    @msg.size('2')
    @msg.count(1)
    def SetLenStart(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 8, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('10')
    @msg.size('2')
    @msg.count(1)
    def SetDataStart(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 10, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('12')
    @msg.size('2')
    @msg.count(1)
    def SetClockSetupStart(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 12, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('14')
    @msg.size('2')
    @msg.count(1)
    def SetRegisterSetupStart(self, value):
        """Register start offset from DataStart"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 14, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('16')
    @msg.size('2')
    @msg.count(1)
    def SetProgramStart(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 16, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('18')
    @msg.size('2')
    @msg.count(1)
    def SetBankA_B0_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 18, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('20')
    @msg.size('2')
    @msg.count(1)
    def SetBankA_B1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 20, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('22')
    @msg.size('2')
    @msg.count(1)
    def SetBankA_B2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 22, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('24')
    @msg.size('2')
    @msg.count(1)
    def SetBankA_A1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 24, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('26')
    @msg.size('2')
    @msg.count(1)
    def SetBankA_A2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 26, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('28')
    @msg.size('2')
    @msg.count(1)
    def SetBankB_B0_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 28, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('30')
    @msg.size('2')
    @msg.count(1)
    def SetBankB_B1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 30, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('32')
    @msg.size('2')
    @msg.count(1)
    def SetBankB_B2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 32, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('34')
    @msg.size('2')
    @msg.count(1)
    def SetBankB_A1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 34, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('36')
    @msg.size('2')
    @msg.count(1)
    def SetBankB_A2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 36, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('38')
    @msg.size('2')
    @msg.count(1)
    def SetBankC_B0_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 38, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('40')
    @msg.size('2')
    @msg.count(1)
    def SetBankC_B1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 40, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('42')
    @msg.size('2')
    @msg.count(1)
    def SetBankC_B2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 42, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('44')
    @msg.size('2')
    @msg.count(1)
    def SetBankC_A1_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 44, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('46')
    @msg.size('2')
    @msg.count(1)
    def SetBankC_A2_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 46, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('48')
    @msg.size('2')
    @msg.count(1)
    def SetPreRel_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 48, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('50')
    @msg.size('2')
    @msg.count(1)
    def SetPostRel_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 50, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('52')
    @msg.size('2')
    @msg.count(1)
    def SetComment_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 52, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('54')
    @msg.size('2')
    @msg.count(1)
    def SetCoefficientMap_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 54, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('56')
    @msg.size('2')
    @msg.count(1)
    def SetCRC_Start(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 56, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('58')
    @msg.size('2')
    @msg.count(1)
    def SetClockSetup_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 58, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('60')
    @msg.size('2')
    @msg.count(1)
    def SetRegisterSetup_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 60, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('62')
    @msg.size('2')
    @msg.count(1)
    def SetProgram_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 62, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('64')
    @msg.size('2')
    @msg.count(1)
    def SetCoefficients_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 64, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('66')
    @msg.size('2')
    @msg.count(1)
    def SetPreRel_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 66, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('68')
    @msg.size('2')
    @msg.count(1)
    def SetPostRel_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 68, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('70')
    @msg.size('2')
    @msg.count(1)
    def SetComment_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 70, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('72')
    @msg.size('2')
    @msg.count(1)
    def SetCoefficientMap_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 72, tmp)
    
    @msg.units('')
    @msg.default('')
    @msg.minVal('0')
    @msg.maxVal('65535')
    @msg.offset('74')
    @msg.size('2')
    @msg.count(1)
    def SetCRC_Len(self, value):
        """"""
        tmp = min(max(value, 0), 65535)
        struct.pack_into('>H', self.rawBuffer(), AcornImageHeader_Full.MSG_OFFSET + 74, tmp)
    

    # Reflection information
    fields = [ \
        FieldInfo(name="ImageType",type="int",units="",minVal="0",maxVal="65535",description="",get=GetImageType,set=SetImageType,count=1, idbits=16,bitfieldInfo = [], enum = []),\
        FieldInfo(name="MajorRev",type="int",units="",minVal="0",maxVal="65535",description="",get=GetMajorRev,set=SetMajorRev,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="MinorRev",type="int",units="",minVal="0",maxVal="255",description="",get=GetMinorRev,set=SetMinorRev,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="PatchRev",type="int",units="",minVal="0",maxVal="255",description="",get=GetPatchRev,set=SetPatchRev,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="OffsetStart",type="int",units="",minVal="0",maxVal="65535",description="",get=GetOffsetStart,set=SetOffsetStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="LenStart",type="int",units="",minVal="0",maxVal="65535",description="",get=GetLenStart,set=SetLenStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="DataStart",type="int",units="",minVal="0",maxVal="65535",description="",get=GetDataStart,set=SetDataStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ClockSetupStart",type="int",units="",minVal="0",maxVal="65535",description="",get=GetClockSetupStart,set=SetClockSetupStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterSetupStart",type="int",units="",minVal="0",maxVal="65535",description="Register start offset from DataStart",get=GetRegisterSetupStart,set=SetRegisterSetupStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ProgramStart",type="int",units="",minVal="0",maxVal="65535",description="",get=GetProgramStart,set=SetProgramStart,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankA_B0_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankA_B0_Start,set=SetBankA_B0_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankA_B1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankA_B1_Start,set=SetBankA_B1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankA_B2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankA_B2_Start,set=SetBankA_B2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankA_A1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankA_A1_Start,set=SetBankA_A1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankA_A2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankA_A2_Start,set=SetBankA_A2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankB_B0_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankB_B0_Start,set=SetBankB_B0_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankB_B1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankB_B1_Start,set=SetBankB_B1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankB_B2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankB_B2_Start,set=SetBankB_B2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankB_A1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankB_A1_Start,set=SetBankB_A1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankB_A2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankB_A2_Start,set=SetBankB_A2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankC_B0_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankC_B0_Start,set=SetBankC_B0_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankC_B1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankC_B1_Start,set=SetBankC_B1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankC_B2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankC_B2_Start,set=SetBankC_B2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankC_A1_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankC_A1_Start,set=SetBankC_A1_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="BankC_A2_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetBankC_A2_Start,set=SetBankC_A2_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="PreRel_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetPreRel_Start,set=SetPreRel_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="PostRel_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetPostRel_Start,set=SetPostRel_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Comment_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetComment_Start,set=SetComment_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CoefficientMap_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetCoefficientMap_Start,set=SetCoefficientMap_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CRC_Start",type="int",units="",minVal="0",maxVal="65535",description="",get=GetCRC_Start,set=SetCRC_Start,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="ClockSetup_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetClockSetup_Len,set=SetClockSetup_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="RegisterSetup_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetRegisterSetup_Len,set=SetRegisterSetup_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Program_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetProgram_Len,set=SetProgram_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Coefficients_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetCoefficients_Len,set=SetCoefficients_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="PreRel_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetPreRel_Len,set=SetPreRel_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="PostRel_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetPostRel_Len,set=SetPostRel_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="Comment_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetComment_Len,set=SetComment_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CoefficientMap_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetCoefficientMap_Len,set=SetCoefficientMap_Len,count=1, bitfieldInfo = [], enum = []),\
        FieldInfo(name="CRC_Len",type="int",units="",minVal="0",maxVal="65535",description="",get=GetCRC_Len,set=SetCRC_Len,count=1, bitfieldInfo = [], enum = [])\
    ]

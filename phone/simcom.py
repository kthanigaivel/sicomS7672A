from phone.com import Com
from machine import UART
from phone.modeinfo.info import Info
from phone.sms.message import Msg
from phone.voice.call import Call
class A7672S(Com):
    TIMEOUT = 1
    def __init__(self,path,baudrate,t,r):
        self.port = UART(path, baudrate,tx=t,rx=r,timeout=A7672S.TIMEOUT)
        super().__init__(self.port)
        self.Info = Info(self.port)
        self.Msg = Msg(self.port)
        self.Call = Call(self.port)
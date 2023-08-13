from phone.com import Com

from phone.modeinfo.info import Info
from phone.sms.message import Msg
from phone.voice.call import Call
from phone.control.control import Ctrl



class A7672S(Com):
    def __init__(self):
        self.Info = Info()
        self.Msg = Msg()
        self.Call = Call()
        self.Ctrl = Ctrl()

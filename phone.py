from phone.simcom import A7672S
import time
gsm=A7672S(path=2,baudrate=115200,t=17,r=16)

#*****INFO*****
print(gsm.Info.all())
# print(gsm.Info.getRSSI())
# print(gsm.Info.DATETIME)
# print(gsm.Info.simoprator)
# print(gsm.Info.simstats)


#*****messages*****
#gsm.Msg.send(9865116823,'HI HOW ARE YOU?')
#print(gsm.Msg.readOne(9))
#read all 0=unread 1=read 2=all
#print(gsm.Msg.readAll(2))
#print(gsm.Msg.delAll())

#*****voice call*****
#gsm.Call.dial(9865116823)
#gsm.Call.answer()
#gsm.Call.hangup()


#*****check before voice call*****
# if (gsm.Info.CPSI[1]=='Online'):
#     print(gsm.Call.dial(9865116823))

#*****control device*****
#gsm.Ctrl.dtmf(9)
#gsm.Ctrl.flight()
print(gsm.Ctrl.me_status())
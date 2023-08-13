from phone.simcom import A7672S
gsm=A7672S()

#*****INFO*****
print(gsm.Info.all())
#print((gsm.Info.RSSI))
#print(gsm.Info.DATETIME)
#print(gsm.Info.simoprator)
#print(gsm.Info.simstats)
#print(gsm.Info.getCPSI())


#*****messages*****
#gsm.Msg.send(9865116823,'HI HOW ARE YOU?')
#print(gsm.Msg.readOne(2))
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
#gsm.Ctrl.reset()
#gsm.Ctrl.spk_mute(True)
#gsm.Ctrl.mic_mute(False)
print(gsm.Ctrl.config())
#print(gsm.Ctrl.me_status())
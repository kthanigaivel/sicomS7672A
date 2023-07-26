from phone.simcom import A7672S
gsm=A7672S(path=2,baudrate=115200,t=17,r=16)

#*****INFO*****
print(gsm.Info.all())
#print(gsm.Info.RSSI)
# print(gsm.Info.DATETIME)
# print(gsm.Info.simoprator)
# print(gsm.Info.simstats)
# print(gsm.Info.CPSI)

#*****messages*****
#gsm.Msg.send(7603826664,'HI HOW ARE YOU?')
#print(gsm.port)
# x=(gsm.Msg.readOne(1))
# print(x['head'][1])
# print(x['head'][3])
# print(x['body'])
for m in range(1,10):
   print(gsm.Msg.readOne(m))

#print(gsm.Msg.delAll())

#*****voice call*****
#gsm.Call.dial(9003474373)
#gsm.Call.answer()
#gsm.Call.hangup()




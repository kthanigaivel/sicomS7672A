from phone.com import Com

class Msg(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send(self, number, sms):
        cmd='AT+CMGF=1'
        # Sets the GSM Module in Text Mode
        self.write(cmd)
        cmd = 'AT+CMGS="{}"'.format(number)
        self.write(cmd,0.5)
        self.write(sms,0.1)
        cmd = '\x1a'
        data= self.command(cmd,'OK')
        return data

    def readOne(self,index=0):
        cmd = 'AT+CMGF=1;'
        self.write(cmd)
        cmd = 'AT+CMGR='+str(index)
        data= self.command(cmd,' ')
        
        return data
    def readAll(self,index=0):
        params=["REC UNREAD","REC READ","ALL"]
        cmd = 'AT+CMGF=1;'
        self.write(cmd)
        cmd = 'AT+CMGL='+str(params[index])
        data= self.command(cmd,' ')
        
        return data
    
    
    def delAll(self):
        cmd = 'AT+CMGD=1,3'
        self.write(cmd)
        return "ALL MESSAGES DELETED SUCCESSFULLY"
        
        
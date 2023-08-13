from phone.com import Com

class Msg(Com):
    def send(self, number, sms):
        cmd=b'AT+CMGF=1\r'
        # Sets the GSM Module in Text Mode
        self.write(cmd)
        cmd = b'AT+CMGS="{}"\r'.format(number)
        self.write(cmd)
        self.write(sms,0.1)
        cmd = b'\x1a\r'
        data= self.command(cmd)
        return data

    def readOne(self,index=0):
        cmd = b'AT+CMGF=1\r'
        self.write(cmd)
        cmd = b'AT+CMGR='+str(index)+b'\r'
        data= self.command(cmd)
        
        return data.decode().partition(':')
    def readAll(self,index=0):
        params=["REC UNREAD","REC READ","ALL"]
        cmd = b'AT+CMGF=1\r'
        self.write(cmd)
        cmd = b'AT+CMGL='+str(params[index])+b'\r'
        data= self.command(cmd)
        
        return data
    
    
    def delAll(self):
        cmd = b'AT+CMGD=1,3\r'
        self.write(cmd)
        return "ALL MESSAGES DELETED SUCCESSFULLY"
        
        
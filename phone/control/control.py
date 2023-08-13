from phone.com import Com
class Ctrl(Com):
    def config(self):
        return self.command(b'AT&V\r')
        
    def spk_mute(self,bool):
        cmd = b'AT+VMUTE='+str(bool)+b'\r'
        return self.write(cmd)
    def mic_mute(self,bool):
        cmd = b'AT+CMUTE='+str(bool)+b'\r'
        return self.write(cmd)
    
    def dtmf(self,char):
        cmd = b'AT+VTS='+str(char)+b'\r'
        return self.write(cmd)
    def flight(self):
        cmd = b'AT+CFUN=7\r'
        self.write(cmd)
    def online(self):
        cmd = b'AT+CFUN=6\r' 
        self.write(cmd)
        cmd = b'AT+CFUN=1\r' 
        self.write(cmd)  
    def poweroff(self):
        cmd = b'AT+CPOF\r' 
        self.write(cmd)
    def reset(self):
        cmd = b'AT+CRESET\r'
        self.write(cmd)
    def me_status(self):
        #0 ready
        #3 ringing
        #4 call in progress
        cmd = b'AT+CPAS\r' 
        return self.command(cmd)
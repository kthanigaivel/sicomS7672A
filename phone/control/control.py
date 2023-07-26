from phone.com import Com
class Ctrl(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dtmf(self,char):
        cmd = 'AT+VTS='+str(char)
        return self.write(cmd)
    def flight(self):
        cmd = 'AT+CFUN=7'
        self.write(cmd)
    def online(self):
        cmd = 'AT+CFUN=6'
        self.write(cmd)
        cmd = 'AT+CFUN=1'
        self.write(cmd)  
    def poweroff(self):
        cmd = 'AT+CPOF'
        self.write(cmd)
    def reset(self):
        cmd = 'AT+CRESET'
        self.write(cmd)
    def me_status(self):
        #0 ready
        #3 ringing
        #4 call in progress
        cmd = 'AT+CPAS'
        return self.command(cmd,'OK')
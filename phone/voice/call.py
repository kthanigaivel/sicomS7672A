from phone.com import Com

class Call(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dial(self, number):
        cmd = 'ATD"{}";'.format(number)
        return self.command(cmd,t=9000,read=False) 

    def hangup(self):
        cmd = "AT+CHUP"
        return self.command(cmd,t=9000,read=False)
    
    def answer(self):
        cmd = "ATA"
        return self.command(cmd,t=9000,read=False)
        return True
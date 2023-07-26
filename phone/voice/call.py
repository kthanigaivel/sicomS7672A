from phone.com import Com
class Call(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def dial(self, number):
        cmd = 'ATD"{}";'.format(number)
        return self.write(cmd) 

    def hangup(self):
        cmd = "AT+CHUP"
        return self.write(cmd)
    
    def answer(self):
        cmd = "ATA"
        return self.write(cmd)
        return True
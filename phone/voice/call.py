from phone.com import Com
class Call(Com):
    def dial(self, number):
        cmd = b'ATD"{}";\r'.format(number)
        return self.write(cmd) 

    def hangup(self):
        cmd = b"AT+CHUP\r"
        return self.write(cmd)
    
    def answer(self):
        cmd = b"ATA\r"
        return self.write(cmd)
        return True
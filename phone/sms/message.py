from phone.com import Com

def _try_decode_utf16_encoded_string(s):
    # Check if the input string is a valid UTF-16 hex string. If it is, decode it. Otherwise, return it as-is. 
    #   is_utf16_encoded_string('60A87684') == '您的'
    #   is_utf16_encoded_string('hello') == 'hello'
    # Recolic K <root@recolic.net>
    prepared = s.strip().lower()
    if len(prepared) % 4 != 0:
        return s
    for c in prepared:
        if c not in '0123456789abcdef':
            return s
    # It is an utf16 encoded string. Let's decode it. 
    result_str = ''
    for i in range(len(prepared)//4):
        decoded_char = chr(int(prepared[i*4:(i+1)*4], 16))
        result_str += decoded_char
    return result_str

def _parse_cmgl_response(cmgl_response_str,prefix='+CMGR: '):
    ENTRY_HEADLINE_PREFIX = prefix
    # List entry headline format: ENTRY_HEADLINE_PREFIX ID ," READ_OR_UNREAD "," NUMBER ",""," DATETIME "
    result_dict = {}
    curr_entry =None
    
    for line in cmgl_response_str.replace('\r','\n').split('\n'):
        if line.startswith(ENTRY_HEADLINE_PREFIX):
             headline_fields = line.split(',"')
             result_dict['head']=(headline_fields)
             pass
        else:
            if line.strip() == '':
                continue
            if line.strip().lower() == 'ok':
                continue
            else:
                result_dict['body']=line
    return result_dict
   



    
class Msg(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send(self, number, sms):
        cmd='AT+CMGF=1'
        # Sets the GSM Module in Text Mode
        self.command(cmd,t=100000,read=True)
        cmd = 'AT+CMGS="{}"'.format(number)
        self.command(cmd,t=100000,read=True)
        self.command(sms,t=500000,read=False)
        cmd = '\x1a'
        self.command(cmd,t=100000)
        return True

    def readOne(self,index=0):
        cmd = 'AT+CMGF=1'
        self.command(cmd)
        cmd = 'AT+CMGR='+str(index)
        self.command(cmd,t=1000000,read=False)
        data = self._readtill("OK")
        return _parse_cmgl_response(data,prefix='+CMGR: ')
    
    def readAll(self):
        cmd = 'AT+CMGF=1'
        self.command(cmd)
        cmd = 'AT+CMGL="ALL"'
        self.command(cmd,t=1000000,read=False)
        data = self._readtill("OK")
        return _parse_cmgl_response(data,prefix='+CMGL: ')
    
    def delAll(self):
        cmd = 'AT+CMGD=1,3'
        self.command(cmd)
        return "ALL MESSAGES DELETED SUCCESSFULLY"
        
        
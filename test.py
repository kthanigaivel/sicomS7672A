from uart import  Com
print(Com.run1(b'AT\r'))
print(Com.run1(b'AT+CSQ\r'))
print(Com.run1(b'AT+COPS?\r'))




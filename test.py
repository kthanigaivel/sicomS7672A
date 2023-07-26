from machine import UART
import time
uart=UART(2,baudrate=115200,tx=17,rx=16)

def writedata(command):
    TERMINATION_CHAR = '\r'
    rxData=bytes()
    uart.write(b''+command+ b'' + TERMINATION_CHAR)
    time.sleep(2)
    while uart.any()>0:
        rxData += uart.readline()
    print(rxData.decode('utf-8'))
#CONNECTION SUCCESS IF RETURN OK
writedata('AT+Creset')
writedata('AT+CMGL=all')
#writedata('AT+CMGD=1,3')

import uasyncio as asyncio
from machine import UART
from time import sleep
class Com:
    DELIMITER = b'\r\n'
    def __init__(self, a=b'at\r'):
        self.a = a
        self.uart = UART(2, baudrate=115200,tx=17,rx=16)
        self.sreader = asyncio.StreamReader(self.uart)
        self.swriter = asyncio.StreamWriter(self.uart,{})
    def __iter__(self):
        data=b'\r\n'
        self.swriter.write(self.a)
        
        while not data.endswith(b'OK\r\n'):
#             if data:
#                 print(data)
            data +=await self.sreader.readline()
            if data.endswith(b'END\r\n'):
                return data
            elif data.endswith(b'OK\r\n'):
                return data
            elif data.endswith(b'PB DONE\r\n'):
                return data
            elif data.endswith(b'ERROR\r\n'):
                return data
            
            else:
                continue
            
            yield from asyncio.sleep(0)
    def write(self,comm,slp=0.1):
        self.swriter.write(comm)
        sleep(slp)
        
        
               
    @staticmethod
    async def bar(a):
        res = await Com(a)  # Retrieve result
        return res
        
    @staticmethod
    def command(a):
        return asyncio.run(Com.bar(a))
import uasyncio as asyncio
from machine import UART
class Com():
    DELIMITER = b'\r\n'
    def __init__(self):
        self.uart = UART(2, 115200)
        self.data = b''
        self.asyncio = asyncio
      
    def __iter__(self):  # Not __await__ issue #2678
        data = b''
        while not data.endswith(self.DELIMITER):
            yield from asyncio.sleep(0) # Necessary because:
            while not self.uart.any():
                yield from self.asyncio.sleep(0) # timing may mean this is never called
            data = b''.join((data, self.uart.read(self.uart.any())))
        self.data = data

    async def send_record(self, data):
        self.uart.write(data)
        await self._send_complete()

    # In a real device driver we would poll the hardware
    # for completion in a loop with await asyncio.sleep(0)
    async def _send_complete(self):
        await self.asyncio.sleep(0)

    def read_record(self):  # Synchronous: await the object before calling
        return self.data # Discard delimiter
    
    @staticmethod
    def run(com):
        inter=Com()
        await inter.send_record(com)
        await inter
        rx_data = inter.read_record()
        return (rx_data)
    @staticmethod
    def run1(com):
        return asyncio.run(Com.run(com))

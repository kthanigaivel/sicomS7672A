import time
import uasyncio as asyncio

class Com:
    def __init__(self, port):
        self._port = port
        self.loop = asyncio.get_event_loop()
        self.deadline = None
        self.result = ''

    async def app_loop(self,comm,exp):
        await self.command1(comm,exp)

        
    def command(self,comm,exp):
        self.loop.create_task(self.app_loop(comm,exp))
        self.loop.run_forever()
        return self.result[:-2]
        
       
    def write(self, command,slp=0.1):
        self._port.write("{}\r".format(command))
        time.sleep(slp)
    
       
    async def writeline(self, command):
        self._port.write("{}\r".format(command))
                
    def stop(self, in_advance=False):
        self.deadline = None
        
    def running(self):
        return self.deadline is not None
    
    def postpone(self, duration = 1000):
        self.deadline = time.ticks_add(time.ticks_ms(), duration)
        
    def read(self, expect=None, duration=1000):
        self.result = ''
        self.postpone(duration)
        self.loop.create_task(self.read_killer(expect, duration))
    
    async def read_killer(self, expect=None, duration=1000):
        time_left = time.ticks_diff(self.deadline, time.ticks_ms())
        while time_left > 0:
            line = self._port.readline()
            if line:
                line = convert_to_string(line)
                self.result += line
                if expect and line.find(expect)==0:
                # if expect and expect in line:
                    self.stop(True)
                    return True
                self.postpone(duration)
            time_left = time.ticks_diff(self.deadline, time.ticks_ms())
        self.stop()
        
        
    async def command1(self, command, expect=None, duration=1000):
        await self.writeline(command)
        
        self.read(expect, duration)
        while self.running():
            await asyncio.sleep(0) # Pause 0.2s
            
        result = self.result
        return result
    
    async def reading(self,expect=None,duration=1000):
        self.read(expect,duration)
        while self.running():
            await asyncio.sleep(0)
        result = self.result
        return result

def convert_to_string(buf):
    try:
        tt =  buf.decode('utf-8').strip()
        return tt
    except UnicodeError:
        tmp = bytearray(buf)
        for i in range(len(tmp)):
            if tmp[i]>127:
                tmp[i] = ord('#')
        return bytes(tmp).decode('utf-8').strip()

    
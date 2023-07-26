import time
class Com:
    def __init__(self, port):
        self._port = port

    def command(self, cmd, t=9000, bytes=14816, return_data=False,
                printio=False, get_decode_data=False,read=True):
        #assert isinstance(cmd, str)

        cmd =cmd+'\r'
        self._port.write(cmd)  
        time.sleep_us(t)
        
        if (read==True):
            if (not get_decode_data):
                rcv = self._port.read(bytes)
                self._port.flush()
            else:
                rcv = None
            if (printio):
                print(rcv)
            if (return_data):
                return rcv


    def _readtill(self,till='OK'):
        rcv = self._port.read(14816)
        rcvd = rcv.decode()
        while till not in rcvd: 
            rcvd += rcv.decode()
            rcv = self._port.read(14816)
        return rcvd
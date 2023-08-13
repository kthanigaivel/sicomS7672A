from phone.com import Com
class Info(Com):
    def __init__(self):
        self._RSSI = None
        self._simoprator = None
        self._simstats = None
        self._DATETIME= None
        self._cpsi = None  
    
    @property
    def RSSI(self):
        self.getRSSI()
        return self._RSSI

    @property
    def DATETIME(self):
        self.getDATETIME()
        return self._DATETIME

    @property
    def simoprator(self):
        self.getOprator()
        return self._simoprator

    @property
    def simstats(self):
        self.checkSim()
        return self._simstats

    @property
    def CPSI(self):
        self.getCPSI()
        return self._cpsi
    
    
    
    def getRSSI(self):
        """
        Get the current signal strength in 'bars'
        """
        data = self.command(b'AT+CSQ\r')
        try:
            RSSI = data.decode().split()[2]
        except:
            RSSI = None
        self._RSSI = RSSI
        return self._RSSI
    
    def getOprator(self):
        # https://stackoverflow.com/questions/39930218/sim7670-gsm-module-returns-0-on-atcops
        data = self.command(b'AT+CSPN?\r')
        print()
        try:
            simoprator = data.decode().split()[2].split(',')[0].upper().replace('"', "")
        except:
            simoprator = None
        self._simoprator = simoprator
        return self._simoprator
    

    def checkSim(self):
        # enable the extended error codes to get a verbose format
        #self.command('AT+CMEE=2',t=9000,read=False)
        data = self.command(b'AT+CMEE=2;+CPIN?\r')
        try:
            simstats =data.decode().split()[2]
        except:
            simstats = None
        self._simstats = simstats
        return self._simstats
    
    def getDATETIME(self):
        """
        Get the current Time'
        """
        data = self.command(b'AT+CNTP;+CCLK?\r')
        try:
            date = data.decode().split()[2].split(',')[0]
            time = data.decode().split()[2].split(',')[1]
            self._DATETIME=[date,time]
        except:
            self._DATETIME = None
        return self._DATETIME

    def getCPSI(self):
        data = self.command(b'AT+CPSI?\r')
        try:
            self._cpsi = data.decode().split()[2].split(',')[0:2]
        except:
            self._cpsi=None
        return self._cpsi
    
    def all(self):
        data=[]
        data.append(self.RSSI)
        data.append(self.simstats)
        data.append(self.simoprator)
        data.append(self.DATETIME)
        data.append(self.CPSI)
        return data
    
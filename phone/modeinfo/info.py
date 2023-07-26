from phone.com import Com
class Info(Com):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        data = self.command('AT+CSQ','OK')
        try:
            RSSI = data.split()[1][0:5]
        except:
            RSSI = None
        self._RSSI = RSSI
        return self._RSSI
    
    def getOprator(self):
        # https://stackoverflow.com/questions/39930218/sim7670-gsm-module-returns-0-on-atcops
        data = self.command('AT+CSPN?','OK')
        try:
            simoprator = data.split(":")[1].split(",")[0].replace('"', "")
            simoprator = simoprator.strip().upper()
        except:
            simoprator = None
        self._simoprator = simoprator
        return self._simoprator
    

    def checkSim(self):
        # enable the extended error codes to get a verbose format
        #self.command('AT+CMEE=2',t=9000,read=False)
        data = self.command('AT+CMEE=2;+CPIN?','OK')
        try:
            simstats = data.split(":")[1].split()[0][0:5]
        except:
            simstats = None
        self._simstats = simstats
        return self._simstats
    
    def getDATETIME(self):
        """
        Get the current Time'
        """
        data = self.command('AT+CNTP;+CCLK?','OK')
        try:
            date = data.split(" ")[1].split(",")[0]
            time = data.split(" ")[1].split(",")[1][0:8]
            self._DATETIME=[date,time]
        except:
            self._DATETIME = None
        return self._DATETIME

    def getCPSI(self):
        cmd = 'AT+CPSI?'
        data = self.command(cmd,'OK')
        try:
            self._cpsi = data.split(':')[1].split(",")
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
    
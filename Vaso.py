class Vaso:
    def _init_(self, volume, limite):
        self._volume = volume
        self._limite = limite
    
#__________geters and seters_____________________
    def setVolume(self, x):
        self._volume = x

    def getVolume(self):
        return self._volume

    def setLimite(self, x):
        self._limite = x

    def getLimite(self):
        return self._limite

#________________despejar um vaso no outro_______________
    def despejaNoOutro(self, x):
        sobraTotal = 0
        if (self._volume + x <= self._limite):
            self._volume += x
        elif(self._volume + x > self._limite):
            sobraAtual = self._limite - self._volume
            sobraTotal = x - sobraAtual
            self._volume += sobraAtual
        return sobraTotal


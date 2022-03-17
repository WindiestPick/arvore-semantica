from Vaso import Vaso

class Regras:
    def _init_ (self, vaso1, vaso2):
        self._vaso1 = vaso1
        self._vaso2 = vaso2

#___________geters end seters______________  
    def setVaso1(self, vaso):
        self._vaso1 = vaso
    def getVaso1(self):
        return self._vaso1
    def setVaso2(self, vaso):
        self._vaso2 = vaso
    def getVaso2(self):
        return self._vaso2

#_____________Metodos Regra_________________
    def encheV1(self):
        self._vaso1.setVolume(self._vaso1.getLimite())

    def encheV2(self):
        self._vaso2.setVolume(self._vaso2.getLimite())
    
    def esvaziaV1(self):
        self._vaso1.setVolume(0)
    
    def esvaziaV2(self):
        self._vaso2.setVolume(0)
    
    def despejarV1noV2(self):
        sobra = self._vaso2.despejaNoOutro(self._vaso1.getVolume())
        self._vaso1.setVolume(sobra)
    
    def despejarV2noV1(self):
        sobra = self._vaso1.despejaNoOutro(self._vaso2.getVolume())
        self._vaso2.setVolume(sobra)
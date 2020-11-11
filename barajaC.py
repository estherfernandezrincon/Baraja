import Baraja

class MiBaraja():

    def __init__(self,palos, numeros):
        self.palos= palos
        self.numeros= numeros
        self.mazacote=Baraja.creaBaraja(palos,numeros)
        
    def barajar(self):
        Baraja.barajar(self.mazacote)

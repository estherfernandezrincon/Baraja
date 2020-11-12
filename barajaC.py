import Baraja

class MiBaraja():

    def __init__(self,palos, numeros):
        self.palos= palos
        self.numeros= numeros
        self.mazacote= Baraja.creaBaraja(palos,numeros)
        
    def barajar(self):
        Baraja.barajar(self.mazacote)

    def repartir(self,num_jugadores, num_cartas):
        jugadores =[]
        for i in range(num_jugadores):
            jugadores.append([])


        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                #carta=self.mazacote.pop()#aqui guarda la carta sacada con pop.
                #jugadores[jugador].append(carta)
                jugadores[jugador].append(self.mazacote.pop())
        return jugadores 

#pop extrae el elemento del indice. Si no lo pones quita la ultima.    
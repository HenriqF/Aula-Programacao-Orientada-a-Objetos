class Numero:
    def __init__(self, numero):
        self.numero = numero
    
    def tipo(self):
        if self.numero > 0:
            print(f"{self.numero} é Positivo")
        elif self.numero < 0:
            print(f"{self.numero} é Negativo")
        else:
            print("O numero é nulo!")
        return
    
Numero(0).tipo()
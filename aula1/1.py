class conversor:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def converterFparaC(self):

        return ((5*(self.temperatura-32))/9)
    

conv = conversor(float(input()))
print(conv.converterFparaC())
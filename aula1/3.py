class Analisador:
    def __init__(self, precoCompra, precoVenda):
        self.precoCompra = precoCompra
        self.precoVenda = precoVenda

        if precoCompra > precoVenda:
            print("Teve lucro")
        elif precoVenda > precoCompra:
            print("Teve perca")
        else:
            print("Os valores são iguais")
    
Analisador(precoCompra=10, precoVenda=5)
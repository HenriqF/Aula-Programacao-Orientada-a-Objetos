class operacao:
    def __init__(self, notas):
        self.notas = notas
        self.media = None
        self.alunoAprovado = False

    def calcularMedia(self):
        div = 0
        soma = 0
        for nota in self.notas:
            soma += nota
            div += 1
        resultado = (soma)/div
        self.media = resultado
        return (f"{resultado:.2f}")
    
    def aprovado(self):
        if round(self.media, 2) >= 7:
            self.alunoAprovado = True
            return("Aprovado!")
        else:
            return("Reprovado.")

op = operacao(notas=(list(map(float, (input().split())))))
print(op.calcularMedia())
print(op.aprovado())
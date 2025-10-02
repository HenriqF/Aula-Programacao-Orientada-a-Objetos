class Aluno():
    def __init__(self, nome, idade, mensalidade=500):
        self.nome = nome
        self.idade = idade
        self.mensalidade = mensalidade

    def alterar(self, valor, atributo):
        if atributo == "nome":
            self.nome = valor
        elif atributo == "idade":
            self.idade = valor
        elif atributo == "mensalidade":
            self.mensalidade = valor

    def consultar_mensalidade(self) -> str:
        return "Tudo certo!" if ((self.nome == "Joao" and self.mensalidade >= 1984) or (self.nome != "Joao" and self.mensalidade >= 500)) else f"Aluno {self.nome} com mensalidad erada!"

    def __str__(self) -> str:
        return (f"Dados do aluno:\n  Nome: {self.nome}\n  Idade: {self.idade}\n  Mensalidade: R${self.mensalidade}\n\n")

if __name__ == "__main__":
    alunos = [Aluno(nome="Pedro", idade=18), Aluno(nome="Joao", idade=18, mensalidade=1934)]
    [x.alterar(x.mensalidade+5, "mensalidade") for x in alunos]
    [(print(x), print(x.consultar_mensalidade())) for x in alunos]

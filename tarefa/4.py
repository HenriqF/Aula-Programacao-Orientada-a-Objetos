#4.	Elabore a função (def) valor absoluto que recebe um número qualquer e retorna o valor absoluto (módulo) correspondente. O programa lê o número digitado pelo usuário, chama a função valor absoluto passando o número lido e depois gera a tela de saída com o valor retornado pela função valor absoluto. Lembrando que valor absoluto de um número positivo é ele mesmo e o valor absoluto de um número negativo é ele multiplicado por -1. Não use a função abs nativa da linguagem.

#Henrique de Figueiredo Reinaldi - 22501841

if __name__ == '__main__':
    f = lambda x : int(x) if int(x) == x else x
    def ab(x):
        return (f(x*-1 if x < 0 else x))
    print(ab(float(input())))
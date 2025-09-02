#3.	Desenvolva a função (def) positivo nulo negativo que recebe um número qualquer real e não retorna nada. Ela mostra a mensagem “Valor Positivo”, se o número recebido for positivo; mostra a mensagem “Valor nulo”, se o número recebido for nulo e mostra a mensagem “Valor negativo”, se o número recebido for negativo. O programa (main) lê o número, chama a função positivo nulo negativo passando o valor lido (argumento). 

#Henrique de Figueiredo Reinaldi - 22501841

if __name__ == '__main__':
    def pnn(x):
        print("nulo" if x == 0 else "positivo" if x > 0 else "negativo")
    pnn(float(input()))
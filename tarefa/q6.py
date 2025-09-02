#Henrique de Figueiredo Reinaldi - 22501841
#6. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário.

n = [int(input())] + [x for x in range(1, 11)]
[print(f"{x} x {n[0]} = {x * n[0]}") for x in n[1:]]
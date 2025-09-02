#Henrique de Figueiredo Reinaldi - 22501841
#5. Elabore o programa que imprima a tabuada de multiplicação do número cinco de um até dez. Gere o seguinte layout:                           

n = [x for x in range(1, 11)]
[print(f"{x} x 5 = {x * 5}") for x in n]
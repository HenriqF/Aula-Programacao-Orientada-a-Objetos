#Henrique de Figueiredo Reinaldi - 22501841
#2.	Elabore o programa que gere a sequência do dobro dos números naturais até 10 na ordem crescente. Mostre também a soma da sequência gerada. 

n = [x*2 for x in range(11)]
print("\n".join(map(str, n)),f"Soma dos valores: {sum(n)}", sep="\n")
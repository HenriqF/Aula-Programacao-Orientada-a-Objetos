#Henrique de Figueiredo Reinaldi - 22501841
#4. Elabore o programa para somar todos os números inteiros que são ao mesmo tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos.

print(sum([x for x in range(501) if x%2 != 0 and x%3 == 0]))
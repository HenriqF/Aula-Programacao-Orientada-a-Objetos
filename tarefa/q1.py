#Henrique de Figueiredo Reinaldi - 22501841
#1.	Projete o programa que leia vários valores reais digitados pelo usuário e no final mostre as seguintes informações:

numeros = list(map(int, input().split()))
print(sum(numeros), len(numeros), sum(numeros)/len(numeros), len([x for x in numeros if x > 20]), sep="\n")
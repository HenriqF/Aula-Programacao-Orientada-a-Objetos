#1.	Crie uma função para somar três valores. Ela recebe os três valores, calcula a soma e retorna o resultado do cálculo. 
#A função main lê os três valores inteiros, chama a função passando os valores lidos e depois mostra o valor retornado pela função, ou seja, o resultado obtido.

#Henrique de Figueiredo Reinaldi - 22501841

if __name__ == '__main__':
    x,y,z,f = list(map(int,input().split())) + [lambda x, y, z: print(x+y+z)]
    f(x,y,z)

#2.	Simule uma calculadora com as quatro operações aritméticas. Implemente uma função para cada operação aritmética. Ela recebe dois valores e não retorna nada. A função executa o cálculo e mostra o resultado do cálculo. O usuário fornecerá a operação desejada (operador: +, -, x, / ) e os dois valores dentro do programa (função main) que chamará uma das quatro funções. O resultado do cálculo será mostrado dentro de cada função. Use variável local.

#Henrique de Figueiredo Reinaldi - 22501841

if __name__ == '__main__':
    ops, input, enum = {"c": lambda x : int(x) if int(x) == x else x, "+": lambda x, y : print(ops["c"](x+y)), "-": lambda x, y : print(ops["c"](x-y)), "*":lambda x, y : print(ops["c"](x*y)), "/":lambda x, y : print(ops["c"](x/y))}, [x for x in input("Operação: x operador y (1 + 2)... > ").split(" ")], lambda n : (n.replace(".","",1).replace("-","",1).isdigit()) and (n[0] == '-' or '-' not in n)
    ops[input[1]](float(input[0]), float(input[2])) if input[1] in "+-*/" and enum(input[0]) and enum(input[2]) else print("Formato errado, por favor use como 'x operador y'. Ex.: (1 + 2)")
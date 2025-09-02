t = ["-"]*9
gabarito = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
posicoes = {0:[0,3,6],
            1:[0,4],
            2:[0,5,7],
            3:[1,3],
            4:[1,4,6,7],
            5:[1,5],
            6:[2,3,7],
            7:[2,4],
            8:[2,5,6]}

def mostrar():
    for i in range(9):
        if i % 3 == 0:
            print("")
        print(t[i]," ",end="")
    print("")

def jogar(turn):
    char = 'O' if turn == 0 else 'X'
    square = int(input(f"{char}, escolha quadrado (1... 9)-->"))-1
    if square < 0 or square >= 9:
        print("Posição não existe.")
        return(-1)
    elif t[square] != "-":
        print("Quadrado já ocupado!") 
        return(-1)
    else:
        t[square] = char
        return(check(square))

def check(square):
    for pos in posicoes[square]:
        if (t[gabarito[pos][0]] == t[gabarito[pos][1]] == t[gabarito[pos][2]] == t[square]):
            return -2

if __name__ == '__main__':
    turn = 0
    while True:
        mostrar()
        val = jogar(turn)
        while val == -1:
            val = jogar(turn)

        if val == -2:
            mostrar()
            print("Vitoria!")
            
            exit(0)
        turn = 1 if turn == 0 else 0
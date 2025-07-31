class operacao:
    def __init__(self, operador, op1, op2):
        self.operador = operador
        self.op1 = op1
        self.op2 = op2

    def operate(self):
        esquerda = self.op1
        direita = self.op2
        if isinstance(self.op1, operacao):
            esquerda = self.op1.operate()
        if isinstance(self.op2, operacao):
            direita = self.op2.operate()

        match self.operador:
            case "u-":
                return(direita * -1)
            case "!":
                if direita == 1:
                    return(0)
                if direita == 0:
                    return(1)
                return(~ direita)
            case "+":
                return(esquerda + direita)
            case "-":
                return(esquerda - direita)
            case "*":
                return(esquerda * direita)
            case "/":
                return(esquerda / direita)

while True:
    unario = {"!","u-"}
    binario = {"+","-","*","/"}

    precedencia = {"+":1,"-":1,"*":2,"/":2,"!":3,"u-":3}
    final = []
    stacksinal = []

    equacao = input("--->")

    i = 0
    current = ""
    tokens = []
    while i < len(equacao):
        char = equacao[i]
        lastchar = None
        if i-1 >= 0:
            lastchar = equacao[i-1]

        if char.isdigit():
            current += char
        elif char in precedencia or char in {"(",")"}:
            if current != "":
                tokens.append(int(current))
                current = ""

            
            if char == "-" and ((lastchar in precedencia or lastchar in {"(",")"}) or (lastchar == None)):
                tokens.append("u-")
            else:
                tokens.append(char)
        i += 1
    if current != "":
        tokens.append(int(current))
        current = ""

    for token in tokens: #poe em ordem reversa polonesa
        if isinstance(token, (float, int)):
            final.append(token)
        elif token in precedencia:
            while stacksinal and (stacksinal[-1] not in "()") and (precedencia[stacksinal[-1]] >= precedencia[token]):
                final.append(stacksinal.pop())
            stacksinal.append(token)
        elif token == "(":
            stacksinal.append("(")
        elif token == ")":
            while stacksinal[-1] != "(":
                final.append(stacksinal.pop())
            stacksinal.pop()
            pass

    while stacksinal:
        final.append(stacksinal.pop())

    resultado = [] #AST root
    for token in final: #Cria a AST
        if token in binario:
            b = resultado.pop()
            a = resultado.pop()
            resultado.append(operacao(operador=token, op1=a, op2=b))
        elif token in unario:
            b = resultado.pop()
            resultado.append(operacao(operador=token, op1=None, op2=b))
        else:
            resultado.append(token)

    print(resultado[0].operate())
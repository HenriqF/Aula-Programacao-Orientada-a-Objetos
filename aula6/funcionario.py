class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def set_nome(self, nome:str) -> None:
        self.nome = nome

    def set_salario(self, salario:float) -> None:
        self.salario = salario

    def get_nome(self) -> str:
        return self.nome
    
    def get_salario(self) -> float:
        return self.salario


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, gerenciados: int) -> None:
                   
        super().__init__(nome, salario)
        self.gerenciados = gerenciados 
        
    def set_nome(self, nome:str) -> None:
        self.nome = nome

    def set_salario(self, salario:float) -> None:
        self.salario = salario

    def set_gerenciados(self, gerenciados:int) -> None:
        self.gerenciados = gerenciados

    def get_nome(self) -> str:
        return self.nome
    
    def get_salario(self) -> float:
        return self.salario
    
    def get_gerenciados(self) -> int:
        return self.gerenciados


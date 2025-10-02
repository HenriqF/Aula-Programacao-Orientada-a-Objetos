class Veiculo:
    def __init__(self, modelo: str, ano: int, valor: float) -> None:
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self) -> str:
        return self.modelo
    def get_ano(self) -> int:
        return self.ano
    def get_valor(self) -> float:
        return self.valor
    
    def set_modelo(self, modelo: str) -> None:
        self.modelo = modelo if type(modelo) == str else self.modelo
    def set_ano(self, ano: int) -> None:
        self.ano = ano if type(ano) == int else self.ano
    def set_valor(self, valor: float) -> None:
        self.valor = valor if type(valor) == float else self.valor

    def __str__(self) -> None:
        return(f"\nmodelo: {self.get_modelo()}\nano: {self.get_ano()}\nvalor: {self.get_valor()}")

def main() -> None:
    a, b = Veiculo(modelo="moto", ano=2023, valor=35.6), Veiculo(modelo="carro", ano=1973, valor=123904.23)
    a.set_modelo("bicicleta")
    print(a, b)
    pass

if __name__ == '__main__':
    main()
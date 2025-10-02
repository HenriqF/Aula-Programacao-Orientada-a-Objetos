from funcionario import *

if __name__ == "__main__":
    funcionarios = [Funcionario(nome=f"Func{x}", salario=12.5*x) for x in range(0, 10)]
    Gerente = Gerente(nome="Pedro", salario=1234.523, gerenciados=len(funcionarios))

    print([(f.nome, f.salario) for f in funcionarios])

    
    print(Gerente.get_nome(), Gerente.get_salario(), Gerente.get_gerenciados())
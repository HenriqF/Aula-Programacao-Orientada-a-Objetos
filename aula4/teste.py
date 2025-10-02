class AnimalEstimacao:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def __len__(self):
        return len(self.nome)
        

if __name__ == "__main__":
    animal1 = AnimalEstimacao("Melância", "Citrullus lanatus")
    animal2 = AnimalEstimacao("Pedro", "Homo sapiens sapiens")

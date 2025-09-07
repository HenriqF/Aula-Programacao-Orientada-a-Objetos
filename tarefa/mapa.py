#Resolva os problemas abaixo usando os conceitos de Programação Orientada a Objetos e pense numa entidade (uma classe) para desenvolver os itens abaixo.

#Henrique de Figueiredo Reinaldi - 22501841
import random

class Mapa():
    """Serve para definir mapas."""
    def __init__(self, nome:str, mapa:list[list[int]], detalhes:int) -> None:
        if type(nome) != str or type(mapa) != list:
            raise TypeError("Por favor, use os tipos da classe corretamente.")
        self.nome = nome
        self.mapa = mapa
        self.tamanho = 0
        self.altitudeMedia = 0.0
        self.detalhes = 0
        self.updateStats()

    #Metodos para manipular mapas.
    def mostrarMapa(self, modo: str) -> None:
        """Mostra o mapa. | Modos: 'hei', 'praias', 'montanhas', 'lava'"""
        if type(modo) != str:
            raise TypeError("modo deve ser str.")
        hei = ["⬛","⬛","⬛","🟪","🟦","🟩","🟨","🟧","🟥"]
        praias = ["🟦","🟦","🟦","🟦","🟨","🟩","🟩","🟩","⬛","⬛","⬜"]
        montanhas = ["🟩","🟩","🟩","🟩","⬛","⬜","⬜","⬜","⬜","⬜","⬜"]
        lava = ["🟧","🟧","🟧","🟥","🟧","🟨","🟨","🟨","🟧","🟧","🟨","🟧","🟧"]
        t = hei if modo == "hei" else praias if modo == "praias" else montanhas if modo == "montanhas" else lava if modo == "lava" else []
        if t == []:
            return
        
        for y in self.mapa:
            for x in y:
                index = x * len(t) // self.detalhes
                index = len(t) - 1 if index >= len(t) else index
                index = 0 if index <= 0 else index
                print(t[index], end="")
            print()
    def erodirMapa(self) -> None:
        """Aplica uma função "erosiva" ao mapa: Para toda célula no mapa, seu valor agora é a média de sí com seus vizinhos."""
        adjacentes = {(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)}

        buffer = self.mapa.copy()
        for y in range(0, len(self.mapa)):
            for x in range(0, len(self.mapa[y])):
                count = 1
                media = 0
                media += self.mapa[y][x]
                for adj in adjacentes:
                    dx, dy = x+adj[0], y+adj[1]
                    if (0 <= dx < len(self.mapa[y])) and (0 <= dy < len(self.mapa)):
                        media += self.mapa[dy][dx]
                        count += 1

                buffer[y][x] = int(media/count)

        self.mapa = buffer
    def aplicarRuido(self) -> None:
        """Salpica ruido no mapa. Toda célula receberá um valor inteiro entre -1 e 1."""
        for y in range(0, len(self.mapa)):
            for x in range(0, len(self.mapa[y])):
                self.mapa[x][y] += random.randint(-1,1)
    def updateStats(self) -> None:
        """Atualiza o tamanho e a altitudeMedia do mapa. Se o mapa for vazio, nao faz nada."""
        celulas = 0
        media = 0
        for y in self.mapa:
            for x in y:
                celulas += 1
                media += x
        if celulas == 0:
            return
        self.tamanho = celulas
        self.altitudeMedia = media/celulas


    #Metodos get
    def getNome(self) -> str:
        return(self.nome)
    def getTamanho(self) -> int:
        return(self.tamanho)
    def getMapa(self) -> list:
        return(self.mapa)
    def getAltitudeMedia(self) -> float:
        return(self.altitudeMedia)
    def getDetalhes(self) -> int:
        return(self.detalhes)
 
    #Metodos set (Nao coloquei altitudeMedia e tamanho pq são derivados de self.mapa. Uso a funcao updateStats() para poder altera-los.)
    def setNome(self, value: str) -> None:
        if type(value) != str:
            raise TypeError("valor deve ser str.")
        self.nome = value
    def setMapa(self, value: list) -> None:
        """Além de atualizar mapa para value, também chama a função updateStats"""
        if type(value) != list:
            raise TypeError("valor deve ser list.")
        self.mapa = value
        self.updateStats()
    def setDetalhes(self, value: int) -> None:
        if type(value) != int:
            raise TypeError("valor deve ser int.")
        self.detalhes = value

def showcase(mapas):
    for m in mapas:
        print(f"Valores de {m.getNome()} : " , "\nTamanho:", m.getTamanho() ,"\nMédia de Altitude:", m.getAltitudeMedia(), "\nDetalhes:", m.getDetalhes())
        mapa = m.getMapa()
        m.mostrarMapa("praias")
        print("\n\n")

def main() -> None:
    detalhes = 15
    quantiaMapas = 5
    tamX = 70
    tamY = 70

    criarNoiseMapa = lambda : [[(random.randint(1,detalhes)) for x in range(0, tamX)] for y in range(0, tamY)]
    mapas = [Mapa(nome="", mapa=[], detalhes=0) for x in range(0,quantiaMapas)]
    [m.setNome(f"Mapa {i+1}") for i, m in enumerate(mapas)]
    [m.setMapa(criarNoiseMapa()) for m in mapas]
    [m.setDetalhes(detalhes) for m in mapas]

    [m.aplicarRuido() for m in mapas]
    for i in range(0, 3):
        [m.erodirMapa() for m in mapas]
    showcase(mapas)
    
if __name__ == "__main__":
    main()
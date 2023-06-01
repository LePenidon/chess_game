from pecas.Rainha import Rainha
from pecas.Rei import Rei
from pecas.Torre import Torre
from pecas.Bispo import Bispo
from pecas.Cavalo import Cavalo
from pecas.Peao import Peao


class Conjuntos():
    pecas = 0
    movimentos_validos = 0
    capturadas = 0
    cor = 0
    imagens = []

    def __init__(self, cor):
        if cor == 'brancas':
            self.pecas = [Torre('brancas', 'TorreBranca', (0, 0)), Cavalo('brancas', 'CavaloBranco', (1, 0)), Bispo('brancas', 'BispoBranco', (2, 0)), Rei('brancas', 'ReiBranco', (3, 0)), Rainha('brancas', 'RainhaBranca', (4, 0)), Bispo('brancas', 'BispoBranco', (5, 0)), Cavalo('brancas', 'CavaloBranco', (6, 0)), Torre(
                'brancas', 'TorreBranca', (7, 0)), Peao('brancas', 'PeaoBranco', (0, 1)), Peao('brancas', 'PeaoBranco', (1, 1)), Peao('brancas', 'PeaoBranco', (2, 1)), Peao('brancas', 'PeaoBranco', (3, 1)), Peao('brancas', 'PeaoBranco', (4, 1)), Peao('brancas', 'PeaoBranco', (5, 1)), Peao('brancas', 'PeaoBranco', (6, 1)), Peao('brancas', 'PeaoBranco', (7, 1))]

        elif cor == 'negras':
            self.pecas = [Torre('negras', 'TorrePreta', (0, 7)), Cavalo('negras', 'CavaloPreto', (1, 7)), Bispo('negras', 'BispoPreto', (2, 7)), Rei('negras', 'ReiPreto', (3, 7)), Rainha('negras', 'RainhaPreta', (4, 7)), Bispo('negras', 'BispoPreto', (5, 7)), Cavalo('negras', 'CavaloPreto', (6, 7)), Torre(
                'negras', 'TorrePreta', (7, 7)), Peao('negras', 'PeaoPreto', (0, 6)), Peao('negras', 'PeaoPreto', (1, 6)), Peao('negras', 'PeaoPreto', (2, 6)), Peao('negras', 'PeaoPreto', (3, 6)), Peao('negras', 'PeaoPreto', (4, 6)), Peao('negras', 'PeaoPreto', (5, 6)), Peao('negras', 'PeaoPreto', (6, 6)), Peao('negras', 'PeaoPreto', (7, 6))]

        self.capturadas = []
        self.movimentos_validos = []
        self.cor = cor
        self.imagens = [i.imagem for i in self.pecas]

        for i in self.pecas:
            self.imagens.append(i.imagem)

        return

    def __iter__(self):
        return iter(self.pecas)

    def __getitem__(self, index):
        return self.pecas[index]

    def get_nomes_pecas(self):
        nomes = [i.nome for i in self.pecas]

        return nomes

    def get_posicoes_pecas(self):
        posicoes = [i.posicao for i in self.pecas]

        return posicoes

    def index_nome(self, nome):
        for i in range(len(self.pecas)):
            if self.pecas[i].nome == nome:
                return i

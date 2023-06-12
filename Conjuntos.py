from pecas.Rainha import Rainha
from pecas.Rei import Rei
from pecas.Torre import Torre
from pecas.Bispo import Bispo
from pecas.Cavalo import Cavalo
from pecas.Peao import Peao


class Conjuntos():
    pecas = 0
    movimentos_validos = 0

    brancas = 0
    negras = 0

    loc_brancas = 0
    loc_negras = 0

    cap_brancas = 0
    cap_negras = 0

    def __init__(self):
        self.brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                        'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
        self.loc_brancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

        self.negras = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                       'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
        self.loc_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                           (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

        self.cap_brancas = []
        self.cap_negras = []

        self.movimentos_validos = []

        self.pecas = ['peao', 'rainha', 'rei', 'cavalo', 'torre', 'bispo']

    def verifica_movimentos(self, turno):
        movimentos = []
        todos_movimentos = []

        if turno == 'brancas':
            localizacoes = self.loc_brancas
            pecas = self.brancas
        else:
            localizacoes = self.loc_negras
            pecas = self.negras

        for i in range((len(pecas))):
            loc = localizacoes[i]
            peca = pecas[i]
            if peca == 'peao':
                movimentos = Peao.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)
            elif peca == 'torre':
                movimentos = Torre.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)
            elif peca == 'cavalo':
                movimentos = Cavalo.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)
            elif peca == 'bispo':
                movimentos = Bispo.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)
            elif peca == 'rainha':
                movimentos = Rainha.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)
            elif peca == 'rei':
                movimentos = Rei.movimentos(
                    loc, turno, self.loc_brancas, self.loc_negras)

            todos_movimentos.append(movimentos)

        return todos_movimentos

from pecas.Peca import Peca
from pecas.Bispo import Bispo
from pecas.Torre import Torre


class Rainha(Peca):

    # construtor
    def __init__(self, uma_cor, uma_imagem, uma_posicao):
        super().__init__(uma_cor, "rainha", uma_imagem, uma_posicao)

        return

    # retorna os movimentos possiveis para esse tipo de peca
    def movimentos(posicao, turno, loc_brancas, loc_negras):
        movimentos_bispo = Bispo.movimentos(
            posicao, turno, loc_brancas, loc_negras)
        movimentos_torre = Torre.movimentos(
            posicao, turno, loc_brancas, loc_negras)

        for i in range(len(movimentos_torre)):
            movimentos_bispo.append(movimentos_torre[i])

        return movimentos_bispo

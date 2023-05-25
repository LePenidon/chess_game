from classes.Peca import Peca


class Rei(Peca):

    def __init__(self, uma_cor, uma_imagem):
        super().__init__(uma_cor, "rei", uma_imagem)

        return

    def movimentos(posicao, turno, loc_brancas, loc_negras):
        movimentos = []
        if turno == 'brancas':
            pecas_da_cor = loc_brancas
        else:
            pecas_da_cor = loc_negras

        anda = [(1, 0), (1, 1), (1, -1), (-1, 0),
                (-1, 1), (-1, -1), (0, 1), (0, -1)]

        for i in range(8):
            mov_possivel = (posicao[0] + anda[i][0], posicao[1] + anda[i][1])

            if mov_possivel not in pecas_da_cor and 0 <= mov_possivel[0] <= 7 and 0 <= mov_possivel[1] <= 7:

                movimentos.append(mov_possivel)

        return movimentos

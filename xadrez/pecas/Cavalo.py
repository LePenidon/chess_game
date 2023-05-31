from pecas.Peca import Peca


class Cavalo(Peca):

    def __init__(self, uma_cor, uma_imagem, uma_loc):
        super().__init__(uma_cor, "cavalo", uma_imagem, uma_loc)

        return

    def movimentos(posicao, turno, loc_brancas, loc_negras):
        movimentos = []
        if turno == 'brancas':
            pecas_da_cor = loc_brancas
        else:
            pecas_da_cor = loc_negras

        # 8 squares to check for knights, they can go two squares in one direction and one in another
        anda = [(1, 2), (1, -2), (2, 1), (2, -1),
                (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(8):
            mov_possivel = (posicao[0] + anda[i][0], posicao[1] + anda[i][1])
            if mov_possivel not in pecas_da_cor and 0 <= mov_possivel[0] <= 7 and 0 <= mov_possivel[1] <= 7:
                movimentos.append(mov_possivel)
        return movimentos

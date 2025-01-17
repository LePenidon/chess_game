from pecas.Peca import Peca


class Cavalo(Peca):
    # construtor
    def __init__(self, uma_cor, uma_imagem, uma_posicao):
        super().__init__(uma_cor, "cavalo", uma_imagem, uma_posicao)

        return

    # retorna os movimentos possiveis para esse tipo de peca
    def movimentos(self, loc_brancas, loc_negras):
        movimentos = []
        if self.cor == 'brancas':
            pecas_da_cor = loc_brancas
        else:
            pecas_da_cor = loc_negras

        anda = [(1, 2), (1, -2), (2, 1), (2, -1),
                (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

        for i in range(8):
            mov_possivel = (self.posicao[0] + anda[i]
                            [0], self.posicao[1] + anda[i][1])
            if mov_possivel not in pecas_da_cor and 0 <= mov_possivel[0] <= 7 and 0 <= mov_possivel[1] <= 7:
                movimentos.append(mov_possivel)

        return movimentos

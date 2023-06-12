from pecas.Peca import Peca


class Peao(Peca):

    # construtor
    def __init__(self, uma_cor, uma_imagem, uma_posicao):
        super().__init__(uma_cor, "peao", uma_imagem, uma_posicao)

        return

    # retorna os movimentos possiveis para esse tipo de peca
    def movimentos(self, loc_brancas, loc_negras):
        movimentos = []
        if self.cor == 'brancas':
            if (self.posicao[0], self.posicao[1] + 1) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] + 1) not in loc_negras and self.posicao[1] < 7:
                movimentos.append((self.posicao[0], self.posicao[1] + 1))
            if (self.posicao[0], self.posicao[1] + 2) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] + 2) not in loc_negras and (self.posicao[0], self.posicao[1] + 1) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] + 1) not in loc_negras and self.posicao[1] == 1:
                movimentos.append((self.posicao[0], self.posicao[1] + 2))
            if (self.posicao[0] + 1, self.posicao[1] + 1) in loc_negras:
                movimentos.append((self.posicao[0] + 1, self.posicao[1] + 1))
            if (self.posicao[0] - 1, self.posicao[1] + 1) in loc_negras:
                movimentos.append((self.posicao[0] - 1, self.posicao[1] + 1))
        else:
            if (self.posicao[0], self.posicao[1] - 1) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] - 1) not in loc_negras and self.posicao[1] > 0:
                movimentos.append((self.posicao[0], self.posicao[1] - 1))
            if (self.posicao[0], self.posicao[1] - 2) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] - 2) not in loc_negras and (self.posicao[0], self.posicao[1] - 1) not in loc_brancas and \
                    (self.posicao[0], self.posicao[1] - 1) not in loc_negras and self.posicao[1] == 6:
                movimentos.append((self.posicao[0], self.posicao[1] - 2))
            if (self.posicao[0] + 1, self.posicao[1] - 1) in loc_brancas:
                movimentos.append((self.posicao[0] + 1, self.posicao[1] - 1))
            if (self.posicao[0] - 1, self.posicao[1] - 1) in loc_brancas:
                movimentos.append((self.posicao[0] - 1, self.posicao[1] - 1))

        return movimentos

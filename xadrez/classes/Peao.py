from classes.Peca import Peca


class Peao(Peca):

    def __init__(self, uma_cor, uma_imagem):
        super().__init__(uma_cor, "peao", uma_imagem)

        return

    def movimentos(posicao, turno, loc_brancas, loc_negras):
        movimentos = []
        if turno == 'brancas':
            if (posicao[0], posicao[1] + 1) not in loc_brancas and \
                    (posicao[0], posicao[1] + 1) not in loc_negras and posicao[1] < 7:
                movimentos.append((posicao[0], posicao[1] + 1))
            if (posicao[0], posicao[1] + 2) not in loc_brancas and \
                    (posicao[0], posicao[1] + 2) not in loc_negras and posicao[1] == 1:
                movimentos.append((posicao[0], posicao[1] + 2))
            if (posicao[0] + 1, posicao[1] + 1) in loc_negras:
                movimentos.append((posicao[0] + 1, posicao[1] + 1))
            if (posicao[0] - 1, posicao[1] + 1) in loc_negras:
                movimentos.append((posicao[0] - 1, posicao[1] + 1))
        else:
            if (posicao[0], posicao[1] - 1) not in loc_brancas and \
                    (posicao[0], posicao[1] - 1) not in loc_negras and posicao[1] > 0:
                movimentos.append((posicao[0], posicao[1] - 1))
            if (posicao[0], posicao[1] - 2) not in loc_brancas and \
                    (posicao[0], posicao[1] - 2) not in loc_negras and posicao[1] == 6:
                movimentos.append((posicao[0], posicao[1] - 2))
            if (posicao[0] + 1, posicao[1] - 1) in loc_brancas:
                movimentos.append((posicao[0] + 1, posicao[1] - 1))
            if (posicao[0] - 1, posicao[1] - 1) in loc_brancas:
                movimentos.append((posicao[0] - 1, posicao[1] - 1))

        return movimentos

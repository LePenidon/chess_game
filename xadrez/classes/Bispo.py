from classes.Peca import Peca


class Bispo(Peca):

    def __init__(self, uma_cor, uma_imagem):
        super().__init__(uma_cor, "bispo", uma_imagem)

        return

    def movimentos(posicao, turno, loc_brancas, loc_negras):
        movimentos = []
        if turno == 'brancas':
            pecas_outra_cor = loc_negras
            pecas_da_cor = loc_brancas
        else:
            pecas_da_cor = loc_negras
            pecas_outra_cor = loc_brancas

        # up-right, up-left, down-right, down-left
        for i in range(4):
            passa = True
            sequencia = 1
            if i == 0:
                x = 1
                y = -1
            elif i == 1:
                x = -1
                y = -1
            elif i == 2:
                x = 1
                y = 1
            else:
                x = -1
                y = 1

            while passa:
                if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) not in pecas_da_cor and \
                        0 <= posicao[0] + (sequencia * x) <= 7 and 0 <= posicao[1] + (sequencia * y) <= 7:
                    movimentos.append(
                        (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)))

                    if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) in pecas_outra_cor:
                        passa = False
                    sequencia += 1
                else:
                    passa = False

        return movimentos

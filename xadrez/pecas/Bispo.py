from pecas.Peca import Peca


class Bispo(Peca):

    # construtor
    def __init__(self, uma_cor, uma_imagem, uma_posicao):
        super().__init__(uma_cor, "bispo", uma_imagem, uma_posicao)

        return

    # retorna os movimentos possiveis para esse tipo de peca
    def movimentos(self, loc_brancas, loc_negras):
        movimentos = []

        if self.cor == 'brancas':
            pecas_outra_cor = loc_negras
            pecas_da_cor = loc_brancas
        else:
            pecas_da_cor = loc_negras
            pecas_outra_cor = loc_brancas

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
                if (self.posicao[0] + (sequencia * x), self.posicao[1] + (sequencia * y)) not in pecas_da_cor and \
                        0 <= self.posicao[0] + (sequencia * x) <= 7 and 0 <= self.posicao[1] + (sequencia * y) <= 7:
                    movimentos.append(
                        (self.posicao[0] + (sequencia * x), self.posicao[1] + (sequencia * y)))

                    if (self.posicao[0] + (sequencia * x), self.posicao[1] + (sequencia * y)) in pecas_outra_cor:
                        passa = False
                    sequencia += 1
                else:
                    passa = False

        return movimentos

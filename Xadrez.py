import pygame
from pecas.Rainha import Rainha
from pecas.Rei import Rei
from pecas.Torre import Torre
from pecas.Bispo import Bispo
from pecas.Cavalo import Cavalo
from pecas.Peao import Peao
from Conjuntos import Conjuntos


class Xadrez():
    conjuntos = 0

    comprimento = 0
    altura = 0
    tela = 0
    fonte = 0
    fonte_media = 0
    tempo = 0
    fps = 0
    turno = 0
    selecao = 0

    imagens_brancas = 0
    imagens_negras = 0

    contador = 0
    vencedor = 0
    fim = 0

    som_mov = 0
    som_inicio = 0
    som_fim = 0

    def __init__(self):
        self.conjuntos = Conjuntos()

        self.comprimento = 480
        self.altura = 600
        self.tela = pygame.display.set_mode((self.comprimento, self.altura))
        pygame.display.set_caption('Xadrez 1v1')

        self.fonte = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.fonte_media = pygame.font.Font(pygame.font.get_default_font(), 40)
        self.tempo = pygame.time.Clock()
        self.fps = 60

        self.turno = 0
        self.selecao = 100

        rainha_brancas = Rainha('brancas', 'RainhaBranca')
        rainha_negras = Rainha('negras', 'RainhaPreta')

        rei_brancas = Rei('brancas', 'ReiBranco')
        rei_negras = Rei('negras', 'ReiPreto')

        torre_brancas = Torre('brancas', 'TorreBranca')
        torre_negras = Torre('negras', 'TorrePreta')

        bispo_brancas = Bispo('brancas', 'BispoBranco')
        bispo_negras = Bispo('negras', 'BispoPreto')

        cavalo_brancas = Cavalo('brancas', 'CavaloBranco')
        cavalo_negras = Cavalo('negras', 'CavaloPreto')

        peao_brancas = Peao('brancas', 'PeaoBranco')
        peao_negras = Peao('negras', 'PeaoPreto')

        self.imagens_brancas = [peao_brancas.imagem, rainha_brancas.imagem, rei_brancas.imagem,
                                cavalo_brancas.imagem, torre_brancas.imagem, bispo_brancas.imagem]

        self.imagens_negras = [peao_negras.imagem, rainha_negras.imagem, rei_negras.imagem,
                               cavalo_negras.imagem, torre_negras.imagem, bispo_negras.imagem]

        self.contador = 0
        self.vencedor = ''
        self.fim = False

        self.som_mov = pygame.mixer.Sound("./sons/movimento.mp3")
        self.som_inicio = pygame.mixer.Sound("./sons/inicio.mp3")
        self.som_fim = pygame.mixer.Sound("./sons/fim.mp3")

        return

    def inicio_jogo():
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        jogo = Xadrez()
        jogo.som_inicio.play()

        return jogo

    def mostra_tabuleiro(jogo):
        for i in range(32):
            coluna = i % 4
            linha = i // 4
            if linha % 2 == 0:
                pygame.draw.rect(jogo.tela, 'light gray', [
                    (coluna * 120), linha * 60, 60, 60])
            else:
                pygame.draw.rect(jogo.tela, 'light gray', [
                    60+(coluna * 120), linha * 60, 60, 60])

            texto = ['Brancas', 'Brancas',
                     'Negras', 'Negras']

            if jogo.turno < 2:
                jogo.tela.blit(jogo.fonte_media.render(
                    texto[jogo.turno], True, 'white'), (160, 530))
            else:
                jogo.tela.blit(jogo.fonte_media.render(
                    texto[jogo.turno], True, 'black'), (160, 530))

            for i in range(9):
                pygame.draw.line(jogo.tela, 'black',
                                 (0, 60 * i), (480, 60 * i), 2)
                pygame.draw.line(jogo.tela, 'black',
                                 (60 * i, 0), (60 * i, 480), 2)

    def mostra_pecas(jogo):
        for i in range(len(jogo.conjuntos.brancas)):
            index = jogo.conjuntos.pecas.index(jogo.conjuntos.brancas[i])
            if jogo.conjuntos.brancas[i] == 'peao':
                jogo.tela.blit(
                    jogo.imagens_brancas[0], ((jogo.conjuntos.loc_brancas[i][0] * 60)+10, (jogo.conjuntos.loc_brancas[i][1] * 60)+10))
            else:
                jogo.tela.blit(jogo.imagens_brancas[index], ((jogo.conjuntos.loc_brancas[i]
                                                              [0] * 60)+10, (jogo.conjuntos.loc_brancas[i][1] * 60)+10))
            if jogo.turno < 2:
                if jogo.selecao == i:
                    pygame.draw.rect(jogo.tela, 'blue', [
                                    (jogo.conjuntos.loc_brancas[i][0] * 60)+2, (jogo.conjuntos.loc_brancas[i][1] * 60)+2, 60, 60], 2)

        for i in range(len(jogo.conjuntos.negras)):
            index = jogo.conjuntos.pecas.index(jogo.conjuntos.negras[i])
            if jogo.conjuntos.negras[i] == 'peao':
                jogo.tela.blit(
                    jogo.imagens_negras[0], ((jogo.conjuntos.loc_negras[i][0] * 60)+10, (jogo.conjuntos.loc_negras[i][1] * 60)+10))
            else:
                jogo.tela.blit(jogo.imagens_negras[index], ((jogo.conjuntos.loc_negras[i]
                                                            [0] * 60)+10, (jogo.conjuntos.loc_negras[i][1] * 60)+10))
            if jogo.turno >= 2:
                if jogo.selecao == i:
                    pygame.draw.rect(jogo.tela, 'blue', [
                                    (jogo.conjuntos.loc_negras[i][0] * 60)+2, (jogo.conjuntos.loc_negras[i][1] * 60)+2, 60, 60], 2)

    def mostra_cheque(jogo, opcoes_negras, opcoes_brancas):
        if jogo.turno < 2:
            if 'rei' in jogo.conjuntos.brancas:
                index_rei = jogo.conjuntos.brancas.index('rei')
                loc_rei = jogo.conjuntos.loc_brancas[index_rei]
                for i in range(len(opcoes_negras)):
                    if loc_rei in opcoes_negras[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [jogo.conjuntos.loc_brancas[index_rei][0] * 60 + 1,
                                                                jogo.conjuntos.loc_brancas[index_rei][1] * 60 + 1, 60, 60], 5)
        else:
            if 'rei' in jogo.conjuntos.negras:
                index_rei = jogo.conjuntos.negras.index('rei')
                loc_rei = jogo.conjuntos.loc_negras[index_rei]
                for i in range(len(opcoes_brancas)):
                    if loc_rei in opcoes_brancas[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [jogo.conjuntos.loc_negras[index_rei][0] * 60 + 1,
                                                                jogo.conjuntos.loc_negras[index_rei][1] * 60 + 1, 60, 60], 5)

    def mostra_mov_possiveis(movimentos, jogo):
        for i in range(len(movimentos)):
            pygame.draw.circle(
                jogo.tela, 'blue', (movimentos[i][0] * 60+30, movimentos[i][1] * 60+30), 5)

    def mostra_final(jogo):
        jogo.som_fim.play()
        jogo.som_fim.set_volume(0.1)

        pygame.draw.rect(jogo.tela, 'red', [90, 200, 340, 70])

        if jogo.vencedor == 'brancas':
            jogo.tela.blit(jogo.fonte.render(
                f'{jogo.vencedor} venceu!', True, 'white'), (100, 210))
            jogo.tela.blit(jogo.fonte.render(
                f'Aperte ENTER para recomeçar!', True, 'white'), (100, 240))

        elif jogo.vencedor == 'negras':
            jogo.tela.blit(jogo.fonte.render(
                f'{jogo.vencedor} venceu!', True, 'black'), (100, 210))
            jogo.tela.blit(jogo.fonte.render(
                f'Aperte ENTER para recomeçar!', True, 'black'), (100, 240))

    def verificar_mov_possiveis(opcoes_negras, opcoes_brancas, jogo):
        if jogo.turno < 2:
            opcoes = opcoes_brancas
        else:
            opcoes = opcoes_negras

        opcoes_validas = opcoes[jogo.selecao]

        return opcoes_validas

    def fim_jogo():
        pygame.quit()

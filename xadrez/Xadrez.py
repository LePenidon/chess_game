import pygame
from pecas.Rainha import Rainha
from pecas.Rei import Rei
from pecas.Torre import Torre
from pecas.Bispo import Bispo
from pecas.Cavalo import Cavalo
from pecas.Peao import Peao


class Xadrez():
    comprimento = 0
    altura = 0
    tela = 0
    fonte = 0
    fonte_media = 0
    tempo = 0
    fps = 0
    brancas = 0
    negras = 0
    loc_brancas = 0
    loc_negras = 0
    cap_brancas = 0
    cap_negras = 0
    turno = 0
    selecao = 0
    movimentos_validos = 0

    imagens_brancas = 0
    imagens_negras = 0

    pecas = 0
    contador = 0
    vencedor = 0
    fim = 0

    def __init__(self):
        self.comprimento = 480
        self.altura = 600
        self.tela = pygame.display.set_mode((self.comprimento, self.altura))
        pygame.display.set_caption('Xadrez 1v1')

        self.fonte = pygame.font.Font('freesansbold.ttf', 20)
        self.fonte_media = pygame.font.Font('freesansbold.ttf', 40)
        self.tempo = pygame.time.Clock()
        self.fps = 60

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
        self.turno = 0
        self.selecao = 100
        self.movimentos_validos = []

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

        self.pecas = ['peao', 'rainha', 'rei', 'cavalo', 'torre', 'bispo']

        self.contador = 0
        self.vencedor = ''
        self.fim = False

        return

    def inicio_jogo():
        pygame.init()
        pygame.font.init()
        jogo = Xadrez()

        return jogo

    def verifica_movimentos(pecas, localizacoes, jogo, turno):
        movimentos = []
        todos_movimentos = []
        for i in range((len(pecas))):
            loc = localizacoes[i]
            peca = pecas[i]
            if peca == 'peao':
                movimentos = Peao.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)
            elif peca == 'torre':
                movimentos = Torre.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)
            elif peca == 'cavalo':
                movimentos = Cavalo.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)
            elif peca == 'bispo':
                movimentos = Bispo.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)
            elif peca == 'rainha':
                movimentos = Rainha.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)
            elif peca == 'rei':
                movimentos = Rei.movimentos(
                    loc, turno, jogo.loc_brancas, jogo.loc_negras)

            todos_movimentos.append(movimentos)

        return todos_movimentos

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
        for i in range(len(jogo.brancas)):
            index = jogo.pecas.index(jogo.brancas[i])
            if jogo.brancas[i] == 'peao':
                jogo.tela.blit(
                    jogo.imagens_brancas[0], ((jogo.loc_brancas[i][0] * 60)+10, (jogo.loc_brancas[i][1] * 60)+10))
            else:
                jogo.tela.blit(jogo.imagens_brancas[index], ((jogo.loc_brancas[i]
                                                              [0] * 60)+10, (jogo.loc_brancas[i][1] * 60)+10))
            if jogo.turno < 2:
                if jogo.selecao == i:
                    pygame.draw.rect(jogo.tela, 'blue', [
                                    (jogo.loc_brancas[i][0] * 60)+2, (jogo.loc_brancas[i][1] * 60)+2, 60, 60], 2)

        for i in range(len(jogo.negras)):
            index = jogo.pecas.index(jogo.negras[i])
            if jogo.negras[i] == 'peao':
                jogo.tela.blit(
                    jogo.imagens_negras[0], ((jogo.loc_negras[i][0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
            else:
                jogo.tela.blit(jogo.imagens_negras[index], ((jogo.loc_negras[i]
                                                            [0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
            if jogo.turno >= 2:
                if jogo.selecao == i:
                    pygame.draw.rect(jogo.tela, 'blue', [
                                    (jogo.loc_negras[i][0] * 60)+2, (jogo.loc_negras[i][1] * 60)+2, 60, 60], 2)

    def mostra_cheque(jogo, opcoes_negras, opcoes_brancas):
        if jogo.turno < 2:
            if 'rei' in jogo.brancas:
                index_rei = jogo.brancas.index('rei')
                loc_rei = jogo.loc_brancas[index_rei]
                for i in range(len(opcoes_negras)):
                    if loc_rei in opcoes_negras[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [jogo.loc_brancas[index_rei][0] * 60 + 1,
                                                                jogo.loc_brancas[index_rei][1] * 60 + 1, 60, 60], 5)
        else:
            if 'rei' in jogo.negras:
                index_rei = jogo.negras.index('rei')
                loc_rei = jogo.loc_negras[index_rei]
                for i in range(len(opcoes_brancas)):
                    if loc_rei in opcoes_brancas[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [jogo.loc_negras[index_rei][0] * 60 + 1,
                                                                jogo.loc_negras[index_rei][1] * 60 + 1, 60, 60], 5)

    def verificar_mov_possiveis(opcoes_negras, opcoes_brancas, jogo):
        if jogo.turno < 2:
            opcoes = opcoes_brancas
        else:
            opcoes = opcoes_negras

        opcoes_validas = opcoes[jogo.selecao]

        return opcoes_validas

    def mostra_mov_possiveis(moves, jogo):
        for i in range(len(moves)):
            pygame.draw.circle(
                jogo.tela, 'blue', (moves[i][0] * 60+30, moves[i][1] * 60+30), 5)

    def mostra_final(jogo):
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

    def fim_jogo():
        pygame.quit()

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

    som_mov = 0
    som_inicio = 0
    som_fim = 0

    def __init__(self):
        self.comprimento = 480
        self.altura = 600
        self.tela = pygame.display.set_mode((self.comprimento, self.altura))
        pygame.display.set_caption('Xadrez 1v1')

        self.fonte = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.fonte_media = pygame.font.Font(pygame.font.get_default_font(), 40)
        self.tempo = pygame.time.Clock()
        self.fps = 60

        self.cap_brancas = []
        self.cap_negras = []
        self.turno = 0
        self.selecao = 100
        self.movimentos_validos = []

        rainha_brancas = Rainha('brancas', 'RainhaBranca', (4, 0))
        rainha_negras = Rainha('negras', 'RainhaPreta', (4, 7))

        rei_brancas = Rei('brancas', 'ReiBranco', (3, 0))
        rei_negras = Rei('negras', 'ReiPreto', (3, 7))

        torre_brancas_1 = Torre('brancas', 'TorreBranca', (0, 0))
        torre_brancas_2 = Torre('brancas', 'TorreBranca', (7, 0))
        torre_negras_1 = Torre('negras', 'TorrePreta', (0, 7))
        torre_negras_2 = Torre('negras', 'TorrePreta', (7, 7))

        bispo_brancas_1 = Bispo('brancas', 'BispoBranco', (2, 0))
        bispo_brancas_2 = Bispo('brancas', 'BispoBranco', (5, 0))
        bispo_negras_1 = Bispo('negras', 'BispoPreto', (2, 7))
        bispo_negras_2 = Bispo('negras', 'BispoPreto', (5, 7))

        cavalo_brancas_1 = Cavalo('brancas', 'CavaloBranco', (1, 0))
        cavalo_brancas_2 = Cavalo('brancas', 'CavaloBranco', (6, 0))
        cavalo_negras_1 = Cavalo('negras', 'CavaloPreto', (1, 7))
        cavalo_negras_2 = Cavalo('negras', 'CavaloPreto', (6, 7))

        peao_brancas_1 = Peao('brancas', 'PeaoBranco', (0, 1),)
        peao_brancas_2 = Peao('brancas', 'PeaoBranco', (1, 1),)
        peao_brancas_3 = Peao('brancas', 'PeaoBranco', (2, 1),)
        peao_brancas_4 = Peao('brancas', 'PeaoBranco', (3, 1),)
        peao_brancas_5 = Peao('brancas', 'PeaoBranco', (4, 1),)
        peao_brancas_6 = Peao('brancas', 'PeaoBranco', (5, 1),)
        peao_brancas_7 = Peao('brancas', 'PeaoBranco', (6, 1),)
        peao_brancas_8 = Peao('brancas', 'PeaoBranco', (7, 1),)

        peao_negras_1 = Peao('negras', 'PeaoPreto', (0, 6))
        peao_negras_2 = Peao('negras', 'PeaoPreto', (1, 6))
        peao_negras_3 = Peao('negras', 'PeaoPreto', (2, 6))
        peao_negras_4 = Peao('negras', 'PeaoPreto', (3, 6))
        peao_negras_5 = Peao('negras', 'PeaoPreto', (4, 6))
        peao_negras_6 = Peao('negras', 'PeaoPreto', (5, 6))
        peao_negras_7 = Peao('negras', 'PeaoPreto', (6, 6))
        peao_negras_8 = Peao('negras', 'PeaoPreto', (7, 6))

        self.brancas = [torre_brancas_1, cavalo_brancas_1, bispo_brancas_1, rei_brancas, rainha_brancas, bispo_brancas_2, cavalo_brancas_2, torre_brancas_2,
                        peao_brancas_1, peao_brancas_2, peao_brancas_3, peao_brancas_4, peao_brancas_5, peao_brancas_6, peao_brancas_7, peao_brancas_8]

        self.negras = [torre_negras_1, cavalo_negras_1, bispo_negras_1, rei_negras, rainha_negras, bispo_negras_2, cavalo_negras_2, torre_negras_2,
                       peao_negras_1, peao_negras_2, peao_negras_3, peao_negras_4, peao_negras_5, peao_negras_6, peao_negras_7, peao_negras_8]

        self.pecas = ['peao', 'rainha', 'rei', 'cavalo', 'torre', 'bispo']

        self.contador = 0
        self.vencedor = ''
        self.fim = False

        self.som_mov = pygame.mixer.Sound("./sons/movimento.mp3")
        self.som_inicio = pygame.mixer.Sound("./sons/inicio.mp3")
        self.som_fim = pygame.mixer.Sound("./sons/fim.mp3")

        return

    def loc_brancas(self):
        localizacoes = []

        for i in self.brancas:
            localizacoes.append(i.loc)

        return localizacoes

    def loc_negras(self):
        localizacoes = []

        for i in self.negras:
            localizacoes.append(i.loc)

        return localizacoes

    def inicio_jogo():
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        jogo = Xadrez()
        jogo.som_inicio.play()

        return jogo

    def verifica_movimentos(pecas, jogo, turno):
        localizacoes = []

        for i in pecas:
            localizacoes.append(i.loc)

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
        for i in jogo.brancas:

            if i.nome == 'peao':
                jogo.tela.blit(
                    i.imagem, ((i.loc[0] * 60)+10, (i.loc[1] * 60)+10))
            else:
                jogo.tela.blit(
                    i.imagem, ((i.loc[0] * 60)+10, (i.loc[1] * 60)+10))
            if jogo.turno < 2:
                if jogo.selecao == i:
                    pygame.draw.rect(jogo.tela, 'blue', [
                                     (i.loc[0] * 60)+2, (i.loc[1] * 60)+2, 60, 60], 2)

        # for i in jogo.negras:
        #     index = jogo.pecas.index(jogo.negras[i])
        #     if jogo.negras[i.nome] == 'peao':
        #         jogo.tela.blit(
        #             jogo.imagens_negras[0], ((jogo.loc_negras[i][0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
        #     else:
        #         jogo.tela.blit(jogo.imagens_negras[index], ((jogo.loc_negras[i]
        #                                                     [0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
        #     if jogo.turno >= 2:
        #         if jogo.selecao == i:
        #             pygame.draw.rect(jogo.tela, 'blue', [
        #                             (jogo.loc_negras[i][0] * 60)+2, (jogo.loc_negras[i][1] * 60)+2, 60, 60], 2)

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

    def fim_jogo():
        pygame.quit()

import pygame
from classes.Rainha import Rainha
from classes.Rei import Rei
from classes.Torre import Torre
from classes.Bispo import Bispo
from classes.Cavalo import Cavalo
from classes.Peao import Peao


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

    pass

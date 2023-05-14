import pygame


class Xadrez:
    comprimento = 0
    altura = 0
    tela = 0
    fonte = 0
    fonte_media = 0
    fonte_grande = 0
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
    imagens_brancas_p = 0
    imagens_negras = 0
    imagens_negras_p = 0

    pecas = 0
    contador = 0
    vencedor = 0
    fim = 0

    def __init__(self):
        self.comprimento = 1000
        self.altura = 900
        self.tela = pygame.display.set_mode((self.comprimento, self.altura))
        pygame.display.set_caption('Xadrez 1v1')

        self.fonte = pygame.font.Font('freesansbold.ttf', 20)
        self.fonte_media = pygame.font.Font('freesansbold.ttf', 40)
        self.fonte_grande = pygame.font.Font('freesansbold.ttf', 50)
        self.tempo = pygame.time.Clock()
        self.fps = 60
        self.brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavlo', 'torre',
                        'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
        self.loc_brancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        self.negras = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavlo', 'torre',
                       'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
        self.loc_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                           (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
        self.cap_brancas = []
        self.cap_negras = []
        self.turno = 0
        self.selecao = 100
        self.movimentos_validos = []

        rainha_brancas = pygame.image.load(
            'imgs/RainhaBranca.png')
        rainha_brancas = pygame.transform.scale(
            rainha_brancas, (80, 80))
        rainha_brancas_p = pygame.transform.scale(
            rainha_brancas, (45, 45))
        rei_brancas = pygame.image.load('imgs/ReiBranco.png')
        rei_brancas = pygame.transform.scale(rei_brancas, (80, 80))
        rei_brancas_p = pygame.transform.scale(
            rei_brancas, (45, 45))
        torre_negras = pygame.image.load('imgs/TorrePreta.png')
        torre_negras = pygame.transform.scale(torre_negras, (80, 80))
        torre_negras_p = pygame.transform.scale(
            torre_negras, (45, 45))
        bispo_negras = pygame.image.load('imgs/BispoPreto.png')
        bispo_negras = pygame.transform.scale(bispo_negras, (80, 80))
        bispo_negras_p = pygame.transform.scale(
            bispo_negras, (45, 45))
        cavalo_negras = pygame.image.load('imgs/CavaloPreto.png')
        cavalo_negras = pygame.transform.scale(
            cavalo_negras, (80, 80))
        cavalo_negras_p = pygame.transform.scale(
            cavalo_negras, (45, 45))
        peao_negras = pygame.image.load('imgs/PeaoPreto.png')
        peao_negras = pygame.transform.scale(peao_negras, (65, 65))
        peao_negras_p = pygame.transform.scale(peao_negras, (45, 45))
        torre_brancas = pygame.image.load('imgs/TorreBranca.png')
        torre_brancas = pygame.transform.scale(
            torre_brancas, (80, 80))
        torre_brancas_p = pygame.transform.scale(
            torre_brancas, (45, 45))
        bispo_brancas = pygame.image.load(
            'imgs/BispoBranco.png')
        bispo_brancas = pygame.transform.scale(
            bispo_brancas, (80, 80))
        bispo_brancas_p = pygame.transform.scale(
            bispo_brancas, (45, 45))
        cavalo_brancas = pygame.image.load(
            'imgs/CavaloBranco.png')
        cavalo_brancas = pygame.transform.scale(
            cavalo_brancas, (80, 80))
        cavalo_brancas_p = pygame.transform.scale(
            cavalo_brancas, (45, 45))
        peao_brancas = pygame.image.load('imgs/PeaoBranco.png')
        peao_brancas = pygame.transform.scale(peao_brancas, (65, 65))
        peao_brancas_p = pygame.transform.scale(
            peao_brancas, (45, 45))

        self.imagens_brancas = [peao_brancas, rainha_brancas, rei_brancas,
                                cavalo_brancas, torre_brancas, bispo_brancas]

        self.imagens_brancas_p = [peao_brancas_p, rainha_brancas_p, rei_brancas_p, cavalo_brancas_p,
                                  torre_brancas_p, bispo_brancas_p]

        self.imagens_negras = [peao_negras, rainha_brancas, rei_brancas,
                               cavalo_negras, torre_negras, bispo_negras]

        self.imagens_negras_p = [peao_negras_p, rainha_brancas_p, rei_brancas_p, cavalo_negras_p,
                                 torre_negras_p, bispo_negras_p]

        self.pecas = ['peao', 'rainha', 'rei', 'cavalo', 'torre', 'bispo']

        self.contador = 0
        self.vencedor = ''
        self.fim = False

        return

    pass

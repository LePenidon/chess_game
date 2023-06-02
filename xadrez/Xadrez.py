import pygame
from pecas.Rainha import Rainha
from Conjuntos import Conjuntos


class Xadrez():
    # atributos
    brancas = 0
    negras = 0
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
    movimentos_validos = 0
    contador = 0
    vencedor = 0
    fim = 0
    som_mov = 0
    som_inicio = 0
    som_fim = 0

    # construtor
    def __init__(self):
        self.brancas = Conjuntos("brancas")
        self.negras = Conjuntos("negras")

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
        self.movimentos_validos = []
        self.contador = 0
        self.vencedor = ''
        self.fim = False
        self.som_mov = pygame.mixer.Sound("./sons/movimento.mp3")
        self.som_inicio = pygame.mixer.Sound("./sons/inicio.mp3")
        self.som_fim = pygame.mixer.Sound("./sons/fim.mp3")

        return

    # inicia o jogo
    def inicio_jogo():
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        jogo = Xadrez()
        jogo.som_inicio.play()

        return jogo

    # mostra o tabuleiro
    def mostra_tabuleiro(self):
        for i in range(32):
            coluna = i % 4
            linha = i // 4
            if linha % 2 == 0:
                pygame.draw.rect(self.tela, 'light gray', [
                    (coluna * 120), linha * 60, 60, 60])
            else:
                pygame.draw.rect(self.tela, 'light gray', [
                    60+(coluna * 120), linha * 60, 60, 60])

            texto = ['Brancas', 'Brancas',
                     'Negras', 'Negras']

            if self.turno < 2:
                self.tela.blit(self.fonte_media.render(
                    texto[self.turno], True, 'white'), (160, 530))
            else:
                self.tela.blit(self.fonte_media.render(
                    texto[self.turno], True, 'black'), (160, 530))

            for i in range(9):
                pygame.draw.line(self.tela, 'black',
                                 (0, 60 * i), (480, 60 * i), 2)
                pygame.draw.line(self.tela, 'black',
                                 (60 * i, 0), (60 * i, 480), 2)

    # mostra as peças
    def mostra_pecas(self):
        for i in self.brancas:
            if i.nome == 'peao':
                self.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            else:
                self.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            if self.turno < 2:
                if self.selecao == self.brancas.index_posicao(i.posicao):
                    pygame.draw.rect(self.tela, 'blue', [
                                     (i.posicao[0] * 60)+2, (i.posicao[1] * 60)+2, 60, 60], 2)

        for i in self.negras:
            if i.nome == 'peao':
                self.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            else:
                self.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            if self.turno >= 2:
                if self.selecao == self.negras.index_posicao(i.posicao):
                    pygame.draw.rect(self.tela, 'blue', [
                                     (i.posicao[0] * 60)+2, (i.posicao[1] * 60)+2, 60, 60], 2)

    # mostra se há cheque
    def mostra_cheque(self, opcoes_negras, opcoes_brancas):
        if self.turno < 2:
            if 'rei' in self.brancas.get_nomes_pecas():
                index = self.brancas.index_nome('rei')
                rei = self.brancas[index]
                for i in range(len(opcoes_negras)):
                    if rei.posicao in opcoes_negras[i]:
                        if self.contador < 15:
                            pygame.draw.rect(self.tela, 'red', [
                                             rei.posicao[0] * 60 + 1, rei.posicao[1] * 60 + 1, 60, 60], 5)
        else:
            if 'rei' in self.negras.get_nomes_pecas():
                index = self.negras.index_nome('rei')
                rei = self.negras[index]
                for i in range(len(opcoes_brancas)):
                    if rei.posicao in opcoes_brancas[i]:
                        if self.contador < 15:
                            pygame.draw.rect(self.tela, 'red', [
                                             rei.posicao[0] * 60 + 1, rei.posicao[1] * 60 + 1, 60, 60], 5)

    # mostra os movimentos possíveis
    def mostra_mov_possiveis(self, movimentos):
        movimentos = self.movimentos_validos
        for i in range(len(movimentos)):
            pygame.draw.circle(
                self.tela, 'blue', (movimentos[i][0] * 60+30, movimentos[i][1] * 60+30), 5)

    # mostra o vencedor
    def mostra_final(self):
        self.som_fim.play()
        self.som_fim.set_volume(0.1)

        pygame.draw.rect(self.tela, 'red', [90, 200, 340, 70])

        if self.vencedor == 'brancas':
            self.tela.blit(self.fonte.render(
                f'{self.vencedor} venceu!', True, 'white'), (100, 210))
            self.tela.blit(self.fonte.render(
                f'Aperte ENTER para recomeçar!', True, 'white'), (100, 240))

        elif self.vencedor == 'negras':
            self.tela.blit(self.fonte.render(
                f'{self.vencedor} venceu!', True, 'black'), (100, 210))
            self.tela.blit(self.fonte.render(
                f'Aperte ENTER para recomeçar!', True, 'black'), (100, 240))

    # verifica os movimentos possíveis para a peça selecionada
    def verificar_mov_possiveis(self, opcoes_negras, opcoes_brancas):
        if self.turno < 2:
            opcoes = opcoes_brancas
        else:
            opcoes = opcoes_negras

        opcoes_validas = opcoes[self.selecao]

        return opcoes_validas

    # verifica promoção do peão
    def verifica_promocao(self):
        if self.turno <= 1:
            if self.brancas[self.selecao].nome == 'peao' and self.brancas[self.selecao].posicao[1] == 7:
                self.brancas[self.selecao] = Rainha(
                    'brancas', 'RainhaBranca', self.brancas[self.selecao].posicao)

        elif self.turno > 1:
            if self.negras[self.selecao].nome == 'peao' and self.negras[self.selecao].posicao[1] == 0:
                self.negras[self.selecao] = Rainha(
                    'negras', 'RainhaPreta', self.negras[self.selecao].posicao)

    def verifica_movimentos(self, turno):
        movimentos = []
        todos_movimentos = []

        if turno == 'brancas':
            pecas = self.brancas
        else:
            pecas = self.negras

        for i in pecas:
            movimentos = i.movimentos(self.brancas.get_posicoes_pecas(
            ), self.negras.get_posicoes_pecas())

            todos_movimentos.append(movimentos)

        return todos_movimentos

    # encerra o jogo
    def fim_jogo():
        pygame.quit()

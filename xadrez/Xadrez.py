import pygame
from pecas.Rainha import Rainha
from pecas.Rei import Rei
from pecas.Torre import Torre
from pecas.Bispo import Bispo
from pecas.Cavalo import Cavalo
from pecas.Peao import Peao
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

    # mostra as peças
    def mostra_pecas(jogo):
        for i in jogo.brancas:
            if i.nome == 'peao':
                jogo.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            else:
                jogo.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            if jogo.turno < 2:
                if jogo.selecao == jogo.brancas.index_posicao(i.posicao):
                    pygame.draw.rect(jogo.tela, 'blue', [
                                     (i.posicao[0] * 60)+2, (i.posicao[1] * 60)+2, 60, 60], 2)

        for i in jogo.negras:
            if i.nome == 'peao':
                jogo.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            else:
                jogo.tela.blit(
                    i.imagem, ((i.posicao[0] * 60)+10, (i.posicao[1] * 60)+10))
            if jogo.turno >= 2:
                if jogo.selecao == jogo.negras.index_posicao(i.posicao):
                    pygame.draw.rect(jogo.tela, 'blue', [
                                     (i.posicao[0] * 60)+2, (i.posicao[1] * 60)+2, 60, 60], 2)

    # mostra se há cheque
    def mostra_cheque(jogo, opcoes_negras, opcoes_brancas):
        if jogo.turno < 2:
            if 'rei' in jogo.brancas.get_nomes_pecas():
                index = jogo.brancas.index_nome('rei')
                rei = jogo.brancas[index]
                for i in range(len(opcoes_negras)):
                    if rei.posicao in opcoes_negras[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [
                                             rei.posicao[0] * 60 + 1, rei.posicao[1] * 60 + 1, 60, 60], 5)
        else:
            if 'rei' in jogo.negras.get_nomes_pecas():
                index = jogo.negras.index_nome('rei')
                rei = jogo.negras[index]
                for i in range(len(opcoes_brancas)):
                    if rei.posicao in opcoes_brancas[i]:
                        if jogo.contador < 15:
                            pygame.draw.rect(jogo.tela, 'red', [
                                             rei.posicao[0] * 60 + 1, rei.posicao[1] * 60 + 1, 60, 60], 5)

    # mostra os movimentos possíveis
    def mostra_mov_possiveis(movimentos, jogo):
        for i in range(len(movimentos)):
            pygame.draw.circle(
                jogo.tela, 'blue', (movimentos[i][0] * 60+30, movimentos[i][1] * 60+30), 5)

    # mostra o vencedor
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

    # verifica os movimentos possíveis para a peça selecionada
    def verificar_mov_possiveis(opcoes_negras, opcoes_brancas, jogo):
        if jogo.turno < 2:
            opcoes = opcoes_brancas
        else:
            opcoes = opcoes_negras

        opcoes_validas = opcoes[jogo.selecao]

        return opcoes_validas

    # verifica os movimentos possíveis para todas as peças
    def verifica_movimentos(self, turno):
        movimentos = []
        todos_movimentos = []

        if turno == 'brancas':
            pecas = self.brancas
        else:
            pecas = self.negras

        for i in pecas:
            if i.nome == 'peao':
                movimentos = Peao.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())
            elif i.nome == 'torre':
                movimentos = Torre.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())
            elif i.nome == 'cavalo':
                movimentos = Cavalo.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())
            elif i.nome == 'bispo':
                movimentos = Bispo.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())
            elif i.nome == 'rainha':
                movimentos = Rainha.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())
            elif i.nome == 'rei':
                movimentos = Rei.movimentos(
                    i.posicao, turno, self.brancas.get_posicoes_pecas(), self.negras.get_posicoes_pecas())

            todos_movimentos.append(movimentos)

        return todos_movimentos

    # encerra o jogo
    def fim_jogo():
        pygame.quit()

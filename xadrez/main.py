import pygame
from Xadrez import Xadrez
from Conjuntos import Conjuntos

# cria o objeto jogo
jogo = Xadrez.inicio_jogo()

# cria os conjuntos de peças
opcoes_negras = jogo.verifica_movimentos('negras')
opcoes_brancas = jogo.verifica_movimentos('brancas')

rodando = True

# loop principal
while rodando:

    # atualiza o jogo
    jogo.tempo.tick(jogo.fps)
    if jogo.contador < 30:
        jogo.contador += 1
    else:
        jogo.contador = 0
    jogo.tela.fill('dark grey')

    # mostra o tabuleiro e as peças
    Xadrez.mostra_tabuleiro(jogo)
    Xadrez.mostra_pecas(jogo)
    Xadrez.mostra_cheque(jogo, opcoes_negras, opcoes_brancas)

    # mostra os movimentos possíveis
    if jogo.selecao != 100:
        jogo.movimentos_validos = Xadrez.verificar_mov_possiveis(
            opcoes_negras, opcoes_brancas, jogo)
        Xadrez.mostra_mov_possiveis(jogo.movimentos_validos, jogo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # verifica se o jogador clicou em uma peça
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not jogo.fim:

            x_coord = evento.pos[0] // 60
            y_coord = evento.pos[1] // 60

            clicou = (x_coord, y_coord)

            jogo.som_fim.stop()
            jogo.som_inicio.stop()

            # realiza o movimento para o turno das brancas
            if jogo.turno <= 1:

                # verifica se o jogador clicou em uma peça
                if clicou in jogo.brancas.get_posicoes_pecas():
                    jogo.selecao = jogo.brancas.get_posicoes_pecas().index(clicou)
                    if jogo.turno == 0:
                        jogo.turno = 1

                # verifica se o jogador clicou em um movimento válido
                if clicou in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.brancas[jogo.selecao].posicao = clicou
                    jogo.som_mov.play()

                    # verifica se o movimento é um xeque-mate
                    if clicou in jogo.negras.get_posicoes_pecas():
                        peca_negra = jogo.negras[jogo.negras.index_posicao(
                            clicou)]

                        if peca_negra.nome == 'rei':
                            jogo.vencedor = 'brancas'

                        jogo.negras.pecas.pop(
                            jogo.negras.index_posicao(peca_negra.posicao))

                    # atualiza o jogo
                    opcoes_negras = jogo.verifica_movimentos('negras')
                    opcoes_brancas = jogo.verifica_movimentos('brancas')
                    jogo.turno = 2
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

            # realiza o movimento para o turno das negras
            if jogo.turno > 1:
                # verifica se o jogador clicou em uma peça
                if clicou in jogo.negras.get_posicoes_pecas():
                    jogo.selecao = jogo.negras.get_posicoes_pecas().index(clicou)

                    if jogo.turno == 2:
                        jogo.turno = 3

                # verifica se o jogador clicou em um movimento válido
                if clicou in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.negras[jogo.selecao].posicao = clicou
                    jogo.som_mov.play()

                    # verifica se o movimento é um xeque-mate
                    if clicou in jogo.brancas.get_posicoes_pecas():
                        peca_branca = jogo.brancas[jogo.brancas.index_posicao(
                            clicou)]

                        if peca_branca.nome == 'rei':
                            jogo.vencedor = 'negras'

                        jogo.brancas.pecas.pop(
                            jogo.brancas.index_posicao(peca_branca.posicao))

                    # atualiza o jogo
                    opcoes_negras = jogo.verifica_movimentos('negras')
                    opcoes_brancas = jogo.verifica_movimentos('brancas')
                    jogo.turno = 0
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

        # verifica se o jogo irá reiniciar
        if evento.type == pygame.KEYDOWN and jogo.fim:
            if evento.key == pygame.K_RETURN:
                jogo.fim = False
                jogo.vencedor = ''

                jogo.brancas = Conjuntos("brancas")
                jogo.negras = Conjuntos("negras")

                jogo.turno = 0
                jogo.selecao = 100
                jogo.movimentos_validos = []
                opcoes_negras = jogo.verifica_movimentos('negras')
                opcoes_brancas = jogo.verifica_movimentos('brancas')

    # verifica se houve um vencedor
    if jogo.vencedor != '':
        jogo.fim = True
        Xadrez.mostra_final(jogo)

    pygame.display.flip()

Xadrez.fim_jogo()

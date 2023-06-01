import pygame
from Xadrez import Xadrez
from Conjuntos import Conjuntos


jogo = Xadrez.inicio_jogo()
conjuntos = Conjuntos()

opcoes_negras = conjuntos.verifica_movimentos('negras')
opcoes_brancas = conjuntos.verifica_movimentos('brancas')
rodando = True

while rodando:
    jogo.tempo.tick(jogo.fps)
    if jogo.contador < 30:
        jogo.contador += 1
    else:
        jogo.contador = 0
    jogo.tela.fill('dark grey')

    Xadrez.mostra_tabuleiro(jogo)
    Xadrez.mostra_pecas(jogo, conjuntos)
    Xadrez.mostra_cheque(jogo, conjuntos, opcoes_negras, opcoes_brancas)

    if jogo.selecao != 100:
        conjuntos.movimentos_validos = Xadrez.verificar_mov_possiveis(
            opcoes_negras, opcoes_brancas, jogo)
        Xadrez.mostra_mov_possiveis(conjuntos.movimentos_validos, jogo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not jogo.fim:

            x_coord = evento.pos[0] // 60
            y_coord = evento.pos[1] // 60

            clicou = (x_coord, y_coord)

            jogo.som_fim.stop()
            jogo.som_inicio.stop()

            if jogo.turno <= 1:

                if clicou in conjuntos.loc_brancas:
                    jogo.selecao = conjuntos.loc_brancas.index(clicou)
                    if jogo.turno == 0:
                        jogo.turno = 1

                if clicou in conjuntos.movimentos_validos and jogo.selecao != 100:
                    conjuntos.loc_brancas[jogo.selecao] = clicou
                    jogo.som_mov.play()

                    if clicou in conjuntos.loc_negras:
                        peca_negra = conjuntos.loc_negras.index(clicou)
                        conjuntos.cap_brancas.append(
                            conjuntos.negras[peca_negra])

                        if conjuntos.negras[peca_negra] == 'rei':
                            jogo.vencedor = 'brancas'

                        conjuntos.negras.pop(peca_negra)
                        conjuntos.loc_negras.pop(peca_negra)

                    opcoes_negras = conjuntos.verifica_movimentos('negras')

                    opcoes_brancas = conjuntos.verifica_movimentos('brancas')
                    jogo.turno = 2
                    jogo.selecao = 100
                    conjuntos.movimentos_validos = []

            if jogo.turno > 1:

                if clicou in conjuntos.loc_negras:
                    jogo.selecao = conjuntos.loc_negras.index(clicou)
                    if jogo.turno == 2:
                        jogo.turno = 3
                if clicou in conjuntos.movimentos_validos and jogo.selecao != 100:
                    conjuntos.loc_negras[jogo.selecao] = clicou
                    jogo.som_mov.play()

                    if clicou in conjuntos.loc_brancas:
                        white_piece = conjuntos.loc_brancas.index(clicou)
                        conjuntos.cap_negras.append(
                            conjuntos.brancas[white_piece])
                        if conjuntos.brancas[white_piece] == 'rei':
                            jogo.vencedor = 'negras'
                        conjuntos.brancas.pop(white_piece)
                        conjuntos.loc_brancas.pop(white_piece)
                    opcoes_negras = conjuntos.verifica_movimentos('negras')
                    opcoes_brancas = conjuntos.verifica_movimentos('brancas')
                    jogo.turno = 0
                    jogo.selecao = 100
                    conjuntos.movimentos_validos = []

        if evento.type == pygame.KEYDOWN and jogo.fim:
            if evento.key == pygame.K_RETURN:
                jogo.fim = False
                jogo.vencedor = ''
                conjuntos.brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                                     'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
                conjuntos.loc_brancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                conjuntos.negras = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                                    'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
                conjuntos.loc_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                        (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                conjuntos.cap_brancas = []
                conjuntos.cap_negras = []
                jogo.turno = 0
                jogo.selecao = 100
                conjuntos.movimentos_validos = []
                opcoes_negras = conjuntos.verifica_movimentos('negras')
                opcoes_brancas = conjuntos.verifica_movimentos('brancas')

    if jogo.vencedor != '':
        jogo.fim = True
        Xadrez.mostra_final(jogo)

    pygame.display.flip()

Xadrez.fim_jogo()

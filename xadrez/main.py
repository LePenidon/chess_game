from functions import *

jogo = inicio_jogo()

opcoes_negras = verifica_movimentos(
    jogo.negras, jogo.loc_negras, jogo, 'negras')
opcoes_brancas = verifica_movimentos(
    jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
rodando = True

while rodando:
    jogo.tempo.tick(jogo.fps)
    if jogo.contador < 30:
        jogo.contador += 1
    else:
        jogo.contador = 0
    jogo.tela.fill('dark gray')

    mostra_tabuleiro(jogo)
    mostra_pecas(jogo)
    mostra_capturadas(jogo)
    mostra_cheque(jogo, opcoes_negras, opcoes_brancas)

    if jogo.selecao != 100:
        jogo.movimentos_validos = verificar_mov_possiveis(
            opcoes_negras, opcoes_brancas, jogo)
        mostra_mov_possiveis(jogo.movimentos_validos, jogo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not jogo.fim:

            x_coord = evento.pos[0] // 60
            y_coord = evento.pos[1] // 60

            clicou = (x_coord, y_coord)
            # print(clicou)

            if jogo.turno <= 1:
                if clicou == (11, 9) or clicou == (12, 9) or clicou == (13, 9) or clicou == (14, 9):
                    jogo.vencedor = 'negras'

                if clicou in jogo.loc_brancas:
                    jogo.selecao = jogo.loc_brancas.index(clicou)
                    if jogo.turno == 0:
                        jogo.turno = 1

                if clicou in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.loc_brancas[jogo.selecao] = clicou

                    if clicou in jogo.loc_negras:
                        peca_negra = jogo.loc_negras.index(clicou)
                        jogo.cap_brancas.append(jogo.negras[peca_negra])

                        if jogo.negras[peca_negra] == 'rei':
                            jogo.vencedor = 'brancas'

                        jogo.negras.pop(peca_negra)
                        jogo.loc_negras.pop(peca_negra)

                    opcoes_negras = verifica_movimentos(
                        jogo.negras, jogo.loc_negras, jogo, 'negras')

                    opcoes_brancas = verifica_movimentos(
                        jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
                    jogo.turno = 2
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

            if jogo.turno > 1:
                if clicou == (11, 9) or clicou == (12, 9) or clicou == (13, 9) or clicou == (14, 9):
                    jogo.vencedor = 'brancas'
                if clicou in jogo.loc_negras:
                    jogo.selecao = jogo.loc_negras.index(clicou)
                    if jogo.turno == 2:
                        jogo.turno = 3
                if clicou in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.loc_negras[jogo.selecao] = clicou
                    if clicou in jogo.loc_brancas:
                        white_piece = jogo.loc_brancas.index(clicou)
                        jogo.cap_negras.append(jogo.brancas[white_piece])
                        if jogo.brancas[white_piece] == 'rei':
                            jogo.vencedor = 'negras'
                        jogo.brancas.pop(white_piece)
                        jogo.loc_brancas.pop(white_piece)
                    opcoes_negras = verifica_movimentos(
                        jogo.negras, jogo.loc_negras, jogo, 'negras')
                    opcoes_brancas = verifica_movimentos(
                        jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
                    jogo.turno = 0
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

        if evento.type == pygame.KEYDOWN and jogo.fim:
            if evento.key == pygame.K_RETURN:
                jogo.fim = False
                jogo.vencedor = ''
                jogo.brancas = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                                'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
                jogo.loc_brancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                jogo.negras = ['torre', 'cavalo', 'bispo', 'rei', 'rainha', 'bispo', 'cavalo', 'torre',
                               'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao', 'peao']
                jogo.loc_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                jogo.cap_brancas = []
                jogo.cap_negras = []
                jogo.turno = 0
                jogo.selecao = 100
                jogo.movimentos_validos = []
                opcoes_negras = verifica_movimentos(
                    jogo.negras, jogo.loc_negras, jogo, 'negras')
                opcoes_brancas = verifica_movimentos(
                    jogo.brancas, jogo.loc_brancas, jogo, 'brancas')

    if jogo.vencedor != '':
        jogo.fim = True
        mostra_final(jogo)

    pygame.display.flip()

fim_jogo()

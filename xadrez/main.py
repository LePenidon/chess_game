from functions import *

jogo = inicio_jogo()

opcoes_negras = check_options(jogo.negras, jogo.loc_negras, jogo, 'negras')
opcoes_brancas = check_options(jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
run = True

while run:
    jogo.tempo.tick(jogo.fps)
    if jogo.contador < 30:
        jogo.contador += 1
    else:
        jogo.contador = 0
    jogo.tela.fill('dark gray')

    draw_board(jogo)
    draw_pieces(jogo)
    # draw_captured(jogo)
    # draw_check(jogo, opcoes_negras, opcoes_brancas)

    if jogo.selecao != 100:
        jogo.movimentos_validos = check_valid_moves(
            opcoes_negras, opcoes_brancas, jogo)
        draw_valid(jogo.movimentos_validos, jogo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not jogo.fim:

            x_coord = event.pos[0] // 60
            y_coord = event.pos[1] // 60

            click_coords = (x_coord, y_coord)
            # print(click_coords)

            if jogo.turno <= 1:
                if click_coords == (10, 9) or click_coords == (11, 9) or click_coords == (12, 9) or click_coords == (13, 9):
                    jogo.vencedor = 'negras'

                if click_coords in jogo.loc_brancas:
                    jogo.selecao = jogo.loc_brancas.index(click_coords)
                    if jogo.turno == 0:
                        jogo.turno = 1

                if click_coords in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.loc_brancas[jogo.selecao] = click_coords

                    if click_coords in jogo.loc_negras:
                        black_piece = jogo.loc_negras.index(click_coords)
                        jogo.cap_brancas.append(jogo.negras[black_piece])

                        if jogo.negras[black_piece] == 'rei':
                            jogo.vencedor = 'brancas'

                        jogo.negras.pop(black_piece)
                        jogo.loc_negras.pop(black_piece)

                    opcoes_negras = check_options(
                        jogo.negras, jogo.loc_negras, jogo, 'negras')

                    opcoes_brancas = check_options(
                        jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
                    jogo.turno = 2
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

            if jogo.turno > 1:
                if click_coords == (10, 9) or click_coords == (11, 9) or click_coords == (12, 9) or click_coords == (13, 9):
                    jogo.vencedor = 'brancas'
                if click_coords in jogo.loc_negras:
                    jogo.selecao = jogo.loc_negras.index(click_coords)
                    if jogo.turno == 2:
                        jogo.turno = 3
                if click_coords in jogo.movimentos_validos and jogo.selecao != 100:
                    jogo.loc_negras[jogo.selecao] = click_coords
                    if click_coords in jogo.loc_brancas:
                        white_piece = jogo.loc_brancas.index(click_coords)
                        jogo.cap_negras.append(jogo.brancas[white_piece])
                        if jogo.brancas[white_piece] == 'rei':
                            jogo.vencedor = 'negras'
                        jogo.brancas.pop(white_piece)
                        jogo.loc_brancas.pop(white_piece)
                    opcoes_negras = check_options(
                        jogo.negras, jogo.loc_negras, jogo, 'negras')
                    opcoes_brancas = check_options(
                        jogo.brancas, jogo.loc_brancas, jogo, 'brancas')
                    jogo.turno = 0
                    jogo.selecao = 100
                    jogo.movimentos_validos = []

        if event.type == pygame.KEYDOWN and jogo.fim:
            if event.key == pygame.K_RETURN:
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
                opcoes_negras = check_options(
                    jogo.negras, jogo.loc_negras, jogo, 'negras')
                opcoes_brancas = check_options(
                    jogo.brancas, jogo.loc_brancas, jogo, 'brancas')

    if jogo.vencedor != '':
        jogo.fim = True
        draw_game_over(jogo)

    pygame.display.flip()


fim_jogo()

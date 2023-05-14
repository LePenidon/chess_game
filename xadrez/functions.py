import pygame
import Xadrez as xd


def inicio_jogo():
    pygame.init()
    pygame.font.init()
    jogo = xd.Xadrez()

    return jogo


def mostra_tabuleiro(jogo: xd.Xadrez):
    for i in range(32):
        coluna = i % 4
        linha = i // 4
        if linha % 2 == 0:
            pygame.draw.rect(jogo.tela, 'light gray', [
                             (coluna * 120), linha * 60, 60, 60])
        else:
            pygame.draw.rect(jogo.tela, 'light gray', [
                             60+(coluna * 120), linha * 60, 60, 60])

        texto = ['Brancas!', 'Brancas!',
                 'Negras!', 'Negras!']

        jogo.tela.blit(jogo.fonte_media.render(
            texto[jogo.turno], True, 'black'), (20, 550))

        for i in range(9):
            pygame.draw.line(jogo.tela, 'black',
                             (0, 60 * i), (480, 60 * i), 2)
            pygame.draw.line(jogo.tela, 'black',
                             (60 * i, 0), (60 * i, 480), 2)

        jogo.tela.blit(jogo.fonte_media.render(
            'Abandonar', True, 'black'), (670, 550))


def mostra_pecas(jogo: xd.Xadrez):
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
                pygame.draw.rect(jogo.tela, 'red', [
                                 (jogo.loc_brancas[i][0] * 60)+2, (jogo.loc_brancas[i][1] * 60)+2, 60, 60], 2)

    for i in range(len(jogo.negras)):
        index = jogo.pecas.index(jogo.negras[i])
        if jogo.negras[i] == 'peao':
            jogo.tela.blit(
                jogo.imagens_negras[0], ((jogo.loc_negras[i][0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
        else:
            jogo.tela.blit(jogo.imagens_negras[index], ((jogo.loc_negras[i]
                                                        [0] * 60)+10, (jogo.loc_negras[i][1] * 60)+5))
        if jogo.turno >= 2:
            if jogo.selecao == i:
                pygame.draw.rect(jogo.tela, 'blue', [
                                 (jogo.loc_negras[i][0] * 60)+2, (jogo.loc_negras[i][1] * 60)+2, 60, 60], 2)


def verifica_movimentos(pecas, localizacoes, jogo: xd.Xadrez, turno):
    movimentos = []
    todos_movimentos = []
    for i in range((len(pecas))):
        loc = localizacoes[i]
        peca = pecas[i]
        if peca == 'peao':
            movimentos = verifica_peao(loc, turno, jogo)
        elif peca == 'torre':
            movimentos = verifica_torre(loc, turno, jogo)
        elif peca == 'cavalo':
            movimentos = verifica_cavalo(loc, turno, jogo)
        elif peca == 'bispo':
            movimentos = verifica_bispo(loc, turno, jogo)
        elif peca == 'rainha':
            movimentos = verifica_rainha(loc, turno, jogo)
        elif peca == 'rei':
            movimentos = verifica_rei(loc, turno, jogo)

        todos_movimentos.append(movimentos)

    return todos_movimentos


def verifica_rei(posicao, turno, jogo: xd.Xadrez):
    movimentos = []
    if turno == 'brancas':
        pecas_da_cor = jogo.loc_brancas
    else:
        pecas_da_cor = jogo.loc_negras

    anda = [(1, 0), (1, 1), (1, -1), (-1, 0),
            (-1, 1), (-1, -1), (0, 1), (0, -1)]

    for i in range(8):
        mov_possivel = (posicao[0] + anda[i][0], posicao[1] + anda[i][1])

        if mov_possivel not in pecas_da_cor and 0 <= mov_possivel[0] <= 7 and 0 <= mov_possivel[1] <= 7:

            movimentos.append(mov_possivel)

    return movimentos


def verifica_rainha(posicao, turno, jogo: xd.Xadrez):
    movimentos_bispo = verifica_bispo(posicao, turno, jogo)
    movimentos_torre = verifica_torre(posicao, turno, jogo)

    for i in range(len(movimentos_torre)):
        movimentos_bispo.append(movimentos_torre[i])

    return movimentos_bispo


def verifica_bispo(posicao, turno, jogo: xd.Xadrez):
    movimentos = []
    if turno == 'brancas':
        pecas_outra_cor = jogo.loc_negras
        pecas_da_cor = jogo.loc_brancas
    else:
        pecas_da_cor = jogo.loc_negras
        pecas_outra_cor = jogo.loc_brancas

    # up-right, up-left, down-right, down-left
    for i in range(4):
        passa = True
        sequencia = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1

        while passa:
            if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) not in pecas_da_cor and \
                    0 <= posicao[0] + (sequencia * x) <= 7 and 0 <= posicao[1] + (sequencia * y) <= 7:
                movimentos.append(
                    (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)))

                if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) in pecas_outra_cor:
                    passa = False
                sequencia += 1
            else:
                passa = False

    return movimentos


def verifica_torre(posicao, turno, jogo: xd.Xadrez):
    movimentos = []
    if turno == 'brancas':
        pecas_outra_cor = jogo.loc_negras
        pecas_da_cor = jogo.loc_brancas
    else:
        pecas_da_cor = jogo.loc_negras
        pecas_outra_cor = jogo.loc_brancas
    for i in range(4):  # down, up, right, left
        passa = True
        sequencia = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while passa:
            if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) not in pecas_da_cor and \
                    0 <= posicao[0] + (sequencia * x) <= 7 and 0 <= posicao[1] + (sequencia * y) <= 7:
                movimentos.append(
                    (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)))
                if (posicao[0] + (sequencia * x), posicao[1] + (sequencia * y)) in pecas_outra_cor:
                    passa = False
                sequencia += 1
            else:
                passa = False
    return movimentos


def verifica_peao(posicao, turno, jogo: xd.Xadrez):
    movimentos = []
    if turno == 'brancas':
        if (posicao[0], posicao[1] + 1) not in jogo.loc_brancas and \
                (posicao[0], posicao[1] + 1) not in jogo.loc_negras and posicao[1] < 7:
            movimentos.append((posicao[0], posicao[1] + 1))
        if (posicao[0], posicao[1] + 2) not in jogo.loc_brancas and \
                (posicao[0], posicao[1] + 2) not in jogo.loc_negras and posicao[1] == 1:
            movimentos.append((posicao[0], posicao[1] + 2))
        if (posicao[0] + 1, posicao[1] + 1) in jogo.loc_negras:
            movimentos.append((posicao[0] + 1, posicao[1] + 1))
        if (posicao[0] - 1, posicao[1] + 1) in jogo.loc_negras:
            movimentos.append((posicao[0] - 1, posicao[1] + 1))
    else:
        if (posicao[0], posicao[1] - 1) not in jogo.loc_brancas and \
                (posicao[0], posicao[1] - 1) not in jogo.loc_negras and posicao[1] > 0:
            movimentos.append((posicao[0], posicao[1] - 1))
        if (posicao[0], posicao[1] - 2) not in jogo.loc_brancas and \
                (posicao[0], posicao[1] - 2) not in jogo.loc_negras and posicao[1] == 6:
            movimentos.append((posicao[0], posicao[1] - 2))
        if (posicao[0] + 1, posicao[1] - 1) in jogo.loc_brancas:
            movimentos.append((posicao[0] + 1, posicao[1] - 1))
        if (posicao[0] - 1, posicao[1] - 1) in jogo.loc_brancas:
            movimentos.append((posicao[0] - 1, posicao[1] - 1))

    return movimentos


def verifica_cavalo(posicao, turno, jogo: xd.Xadrez):
    movimentos = []
    if turno == 'brancas':
        pecas_da_cor = jogo.loc_brancas
    else:
        pecas_da_cor = jogo.loc_negras

    # 8 squares to check for knights, they can go two squares in one direction and one in another
    anda = [(1, 2), (1, -2), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        mov_possivel = (posicao[0] + anda[i][0], posicao[1] + anda[i][1])
        if mov_possivel not in pecas_da_cor and 0 <= mov_possivel[0] <= 7 and 0 <= mov_possivel[1] <= 7:
            movimentos.append(mov_possivel)
    return movimentos


def verificar_mov_possiveis(opcoes_negras, opcoes_brancas, jogo: xd.Xadrez):
    if jogo.turno < 2:
        opcoes = opcoes_brancas
    else:
        opcoes = opcoes_negras

    opcoes_validas = opcoes[jogo.selecao]

    return opcoes_validas


def mostra_mov_possiveis(moves, jogo: xd.Xadrez):
    if jogo.turno < 2:
        turno = 'red'
    else:
        turno = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            jogo.tela, turno, (moves[i][0] * 60+30, moves[i][1] * 60+30), 5)


def mostra_capturadas(jogo: xd.Xadrez):
    for i in range(len(jogo.cap_brancas)):
        peca_capturada = jogo.cap_brancas[i]
        index = jogo.pecas.index(peca_capturada)
        jogo.tela.blit(jogo.imagens_negras_p[index], (600, 30 * i + 10))
    for i in range(len(jogo.cap_negras)):
        peca_capturada = jogo.cap_negras[i]
        index = jogo.pecas.index(peca_capturada)
        jogo.tela.blit(jogo.imagens_brancas_p[index], (500, 30 * i+10))


def mostra_cheque(jogo: xd.Xadrez, opcoes_negras, opcoes_brancas):
    if jogo.turno < 2:
        if 'rei' in jogo.brancas:
            index_rei = jogo.brancas.index('rei')
            loc_rei = jogo.loc_brancas[index_rei]
            for i in range(len(opcoes_negras)):
                if loc_rei in opcoes_negras[i]:
                    if jogo.contador < 15:
                        pygame.draw.rect(jogo.tela, 'dark red', [jogo.loc_brancas[index_rei][0] * 60 + 1,
                                                                 jogo.loc_brancas[index_rei][1] * 60 + 1, 60, 60], 5)
    else:
        if 'rei' in jogo.negras:
            index_rei = jogo.negras.index('rei')
            loc_rei = jogo.loc_negras[index_rei]
            for i in range(len(opcoes_brancas)):
                if loc_rei in opcoes_brancas[i]:
                    if jogo.contador < 15:
                        pygame.draw.rect(jogo.tela, 'dark blue', [jogo.loc_negras[index_rei][0] * 60 + 1,
                                                                  jogo.loc_negras[index_rei][1] * 60 + 1, 60, 60], 5)


def mostra_final(jogo: xd.Xadrez):
    pygame.draw.rect(jogo.tela, 'black', [200, 200, 400, 70])
    jogo.tela.blit(jogo.fonte.render(
        f'{jogo.vencedor} venceu!', True, 'white'), (210, 210))
    jogo.tela.blit(jogo.fonte.render(f'Aperte ENTER para recomeçar!',
                                     True, 'white'), (210, 240))


def fim_jogo():
    pygame.quit()

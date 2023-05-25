import pygame
import classes.Xadrez as xd
from classes.Rainha import Rainha
from classes.Rei import Rei
from classes.Torre import Torre
from classes.Bispo import Bispo
from classes.Cavalo import Cavalo
from classes.Peao import Peao


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
                pygame.draw.rect(jogo.tela, 'blue', [
                                 (jogo.loc_brancas[i][0] * 60)+2, (jogo.loc_brancas[i][1] * 60)+2, 60, 60], 2)

    for i in range(len(jogo.negras)):
        index = jogo.pecas.index(jogo.negras[i])
        if jogo.negras[i] == 'peao':
            jogo.tela.blit(
                jogo.imagens_negras[0], ((jogo.loc_negras[i][0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
        else:
            jogo.tela.blit(jogo.imagens_negras[index], ((jogo.loc_negras[i]
                                                        [0] * 60)+10, (jogo.loc_negras[i][1] * 60)+10))
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


def verificar_mov_possiveis(opcoes_negras, opcoes_brancas, jogo: xd.Xadrez):
    if jogo.turno < 2:
        opcoes = opcoes_brancas
    else:
        opcoes = opcoes_negras

    opcoes_validas = opcoes[jogo.selecao]

    return opcoes_validas


def mostra_mov_possiveis(moves, jogo: xd.Xadrez):
    if jogo.turno < 2:
        turno = 'blue'
    else:
        turno = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            jogo.tela, turno, (moves[i][0] * 60+30, moves[i][1] * 60+30), 5)


def mostra_cheque(jogo: xd.Xadrez, opcoes_negras, opcoes_brancas):
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


def mostra_final(jogo: xd.Xadrez):
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

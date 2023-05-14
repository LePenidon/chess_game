import pygame
import Xadrez as xd


def inicio_jogo():
    pygame.init()
    pygame.font.init()
    jogo = xd.Xadrez()

    return jogo


def draw_board(jogo: xd.Xadrez):
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(jogo.tela, 'light gray', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(jogo.tela, 'light gray', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(jogo.tela, 'gray', [0, 800, jogo.comprimento, 100])
        pygame.draw.rect(jogo.tela, 'gold', [0, 800, jogo.comprimento, 100], 5)
        pygame.draw.rect(jogo.tela, 'gold', [800, 0, 200, jogo.altura], 5)
        status_text = ['Brancas!', 'Brancas!',
                       'Negras!', 'Negras!']
        jogo.tela.blit(jogo.fonte_grande.render(
            status_text[jogo.turno], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(jogo.tela, 'black',
                             (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(jogo.tela, 'black',
                             (100 * i, 0), (100 * i, 800), 2)
        jogo.tela.blit(jogo.fonte_media.render(
            'FORFEIT', True, 'black'), (810, 830))


# draw pieces onto board
def draw_pieces(jogo: xd.Xadrez):
    for i in range(len(jogo.brancas)):
        index = jogo.pecas.index(jogo.brancas[i])
        if jogo.brancas[i] == 'peao':
            jogo.tela.blit(
                jogo.imagens_brancas[0], (jogo.loc_brancas[i][0] * 100 + 22, jogo.loc_brancas[i][1] * 100 + 30))
        else:
            jogo.tela.blit(jogo.imagens_brancas[index], (jogo.loc_brancas[i]
                                                         [0] * 100 + 10, jogo.loc_brancas[i][1] * 100 + 10))
        if jogo.turno < 2:
            if jogo.selecao == i:
                pygame.draw.rect(jogo.tela, 'red', [jogo.loc_brancas[i][0] * 100 + 1, jogo.loc_brancas[i][1] * 100 + 1,
                                                    100, 100], 2)

    for i in range(len(jogo.negras)):
        index = jogo.pecas.index(jogo.negras[i])
        if jogo.negras[i] == 'peao':
            jogo.tela.blit(
                jogo.imagens_negras[0], (jogo.loc_negras[i][0] * 100 + 22, jogo.loc_negras[i][1] * 100 + 30))
        else:
            jogo.tela.blit(jogo.imagens_negras[index], (jogo.loc_negras[i]
                                                        [0] * 100 + 10, jogo.loc_negras[i][1] * 100 + 10))
        if jogo.turno >= 2:
            if jogo.selecao == i:
                pygame.draw.rect(jogo.tela, 'blue', [jogo.loc_negras[i][0] * 100 + 1, jogo.loc_negras[i][1] * 100 + 1,
                                                     100, 100], 2)


# function to check all pieces valid options on board
def check_options(pecas, loc, jogo: xd.Xadrez, turno):
    moves_list = []
    all_moves_list = []
    for i in range((len(pecas))):
        location = loc[i]
        piece = pecas[i]
        if piece == 'peao':
            moves_list = check_pawn(location, turno, jogo)
        elif piece == 'torre':
            moves_list = check_rook(location, turno, jogo)
        elif piece == 'cavalo':
            moves_list = check_knight(location, turno, jogo)
        elif piece == 'bispo':
            moves_list = check_bishop(location, turno, jogo)
        elif piece == 'rainha':
            moves_list = check_queen(location, turno, jogo)
        elif piece == 'rei':
            moves_list = check_king(location, turno, jogo)
        all_moves_list.append(moves_list)

    return all_moves_list


# check king valid moves
def check_king(position, color, jogo: xd.Xadrez):
    moves_list = []
    if color == 'brancas':
        enemies_list = jogo.loc_negras
        friends_list = jogo.loc_brancas
    else:
        friends_list = jogo.loc_negras
        enemies_list = jogo.loc_brancas
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color, jogo: xd.Xadrez):
    moves_list = check_bishop(position, color, jogo)
    second_list = check_rook(position, color, jogo)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color, jogo: xd.Xadrez):
    moves_list = []
    if color == 'white':
        enemies_list = jogo.loc_negras
        friends_list = jogo.loc_brancas
    else:
        friends_list = jogo.loc_negras
        enemies_list = jogo.loc_brancas
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
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
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color, jogo: xd.Xadrez):
    moves_list = []
    if color == 'white':
        enemies_list = jogo.loc_negras
        friends_list = jogo.loc_brancas
    else:
        friends_list = jogo.loc_negras
        enemies_list = jogo.loc_brancas
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
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
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color, jogo: xd.Xadrez):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in jogo.loc_brancas and \
                (position[0], position[1] + 1) not in jogo.loc_negras and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in jogo.loc_brancas and \
                (position[0], position[1] + 2) not in jogo.loc_negras and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in jogo.loc_negras:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in jogo.loc_negras:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in jogo.loc_brancas and \
                (position[0], position[1] - 1) not in jogo.loc_negras and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in jogo.loc_brancas and \
                (position[0], position[1] - 2) not in jogo.loc_negras and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in jogo.loc_brancas:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in jogo.loc_brancas:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# check valid knight moves
def check_knight(position, color, jogo: xd.Xadrez):
    moves_list = []
    if color == 'white':
        enemies_list = jogo.loc_negras
        friends_list = jogo.loc_brancas
    else:
        friends_list = jogo.loc_negras
        enemies_list = jogo.loc_brancas
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves(opcoes_negras, opcoes_brancas, jogo: xd.Xadrez):
    if jogo.turno < 2:
        options_list = opcoes_brancas
    else:
        options_list = opcoes_negras
    valid_options = options_list[jogo.selecao]
    return valid_options


def draw_valid(moves, jogo: xd.Xadrez):
    if jogo.turno < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            jogo.tela, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw captured pieces on side of jogo.tela
def draw_captured(jogo: xd.Xadrez):
    for i in range(len(jogo.cap_brancas)):
        captured_piece = jogo.cap_brancas[i]
        index = jogo.pecas.index(captured_piece)
        jogo.tela.blit(jogo.imagens_negras_p[index], (825, 5 + 50 * i))
    for i in range(len(jogo.cap_negras)):
        captured_piece = jogo.cap_negras[i]
        index = jogo.pecas.index(captured_piece)
        jogo.tela.blit(jogo.imagens_brancas_p[index], (925, 5 + 50 * i))


# draw a flashing square around king if in check
def draw_check(jogo: xd.Xadrez, opcoes_negras, opcoes_brancas):
    if jogo.turno < 2:
        if 'king' in jogo.brancas:
            king_index = jogo.brancas.index('king')
            king_location = jogo.loc_brancas[king_index]
            for i in range(len(opcoes_negras)):
                if king_location in opcoes_negras[i]:
                    if jogo.contador < 15:
                        pygame.draw.rect(jogo.tela, 'dark red', [jogo.loc_brancas[king_index][0] * 100 + 1,
                                                                 jogo.loc_brancas[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in jogo.negras:
            king_index = jogo.negras.index('king')
            king_location = jogo.loc_negras[king_index]
            for i in range(len(opcoes_brancas)):
                if king_location in opcoes_brancas[i]:
                    if jogo.contador < 15:
                        pygame.draw.rect(jogo.tela, 'dark blue', [jogo.loc_negras[king_index][0] * 100 + 1,
                                                                  jogo.loc_negras[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over(jogo: xd.Xadrez):
    pygame.draw.rect(jogo.tela, 'negras', [200, 200, 400, 70])
    jogo.tela.blit(jogo.fonte.render(
        f'{jogo.vencedor} won the game!', True, 'white'), (210, 210))
    jogo.tela.blit(jogo.fonte.render(f'Press ENTER to Restart!',
                                     True, 'white'), (210, 240))


def fim_jogo():
    pygame.quit()

import pygame
from Xadrez import Xadrez
from Conjuntos import Conjuntos


jogo = Xadrez.inicio_jogo()

opcoes_negras = jogo.verifica_movimentos('negras')
opcoes_brancas = jogo.verifica_movimentos('brancas')

print(opcoes_brancas)

# while rodando:
#     jogo.tempo.tick(jogo.fps)
#     if jogo.contador < 30:
#         jogo.contador += 1
#     else:
#         jogo.contador = 0
#     jogo.tela.fill('dark grey')
#     Xadrez.mostra_tabuleiro(jogo)
#     Xadrez.mostra_pecas(jogo)

#     pygame.display.flip()

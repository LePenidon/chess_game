from abc import ABC, abstractmethod
import pygame


class Peca(ABC):
    cor = None
    imagem = None
    nome = None
    posicao = None

    def __init__(self, uma_cor, um_nome, uma_imagem, uma_posicao):
        caminho_img = 'imgs/'
        extensao_img = '.png'
        self.cor = uma_cor
        self.nome = um_nome
        self.imagem = pygame.image.load(
            caminho_img+uma_imagem+extensao_img)
        self.imagem = pygame.transform.scale(
            self.imagem, (40, 40))
        self.posicao = uma_posicao

        return

    @abstractmethod
    def movimentos(self, posicao, turno):
        return []

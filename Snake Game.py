import pygame
from pygame.locals import *
from sys import exit
from random import randint

def jogo():
    pygame.init()
    barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
    largura = 640
    altura = 480

    x_cobra = int((largura / 2))
    y_cobra = int((altura / 2))
    velocidade = 10
    x_controle = velocidade
    y_controle = 0

    x_maca = randint(40,600)
    y_maca= randint(50,430)

    fonte = pygame.font.SysFont('Consolas',30,True,True)
    pontos = 0

    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('Jogo')
    relogio = pygame.time.Clock()
    lista_cobra = []
    comprimento_inicial = 5
    def aumenta_cobra(lista_cobra): 
        for XeY in lista_cobra:
            pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))

    while True:
        relogio.tick(30)
        tela.fill((0,0,0))
        mensagem = f'Pontos: {pontos}'
        texto_formatado = fonte.render(mensagem,True,(255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_a:
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                if event.key == K_d:
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                if event.key == K_w:
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                if event.key == K_s:
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

        x_cobra = x_cobra + x_controle
        y_cobra = y_cobra + y_controle

        cobra = pygame.draw.rect(tela,(0,0,255),(x_cobra,y_cobra,20,20))
        maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))
        if cobra.colliderect(maca):
            x_maca = randint(40,600)
            y_maca= randint(50,430)
            pontos += 1
            barulho_colisao.play()
            comprimento_inicial += 1

        lista_cabeca = []
        lista_cabeca.append(x_cobra)
        lista_cabeca.append(y_cobra)

        lista_cobra.append(lista_cabeca)

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        aumenta_cobra(lista_cobra)

        def exibir_mensagem(mensagem):
            texto = fonte.render(mensagem, True, (255, 255, 255))
            rect_texto = texto.get_rect()
            rect_texto.center = (largura / 2, altura / 2)
            tela.blit(texto, rect_texto)
            pygame.display.update()
            pygame.time.wait(2000)

        if any(bloco == lista_cabeca for bloco in lista_cobra[:-1]):
            exibir_mensagem("Você perdeu!.")
            jogo()

        if x_cobra < 0 or y_cobra < 0 or x_cobra > largura-20 or y_cobra > altura-20:
            exibir_mensagem("Você perdeu!.")
            jogo()

        tela.blit(texto_formatado,(450,50))
        pygame.display.update()

jogo()

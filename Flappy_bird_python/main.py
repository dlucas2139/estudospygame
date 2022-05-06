from turtle import bgcolor
import pygame, sys,time,random
def desenhar_chao():
    janela.blit(floor_surface,(floor_x_position,900))
    janela.blit(floor_surface,(floor_x_position + 576,900))
def criar_cano():
    cano_aleatorio = random.choice(cano_cima)
    cano_baixo = pipe_surface.get_rect(midtop = (700,cano_aleatorio))    
    cano_top = pipe_surface.get_rect(midbottom = (700,cano_aleatorio -300))    
    return cano_baixo, cano_top
def move_cano(canos):
    for cano in canos:
        cano.centerx -= 5
    return canos
def desenhar_canos(canos):
    for pipe in canos:
        if pipe.bottom >= 1024:
            janela.blit(pipe_surface,pipe)
        else:
            flip_cano = pygame.transform.flip(pipe_surface,False,True)
            janela.blit(flip_cano,pipe)
        pass
def colisoes(canos):
    for pipe in canos:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True
def virar_p(passaro):
    novo_passaro = pygame.transform.rotozoom(passaro,-move_bird * 3,1)
    return novo_passaro
pygame.init()
janela = pygame.display.set_mode((576,1024))
relogio = pygame.time.Clock()
gravidade = 0.40
move_bird = 0

bg_surface = pygame.image.load("sprites/background-day.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("sprites/base.png").convert()
floor_surface = pygame.transform.scale2x(floor_surface)

bird_surface = pygame.image.load("sprites/bluebird-midflap.png").convert_alpha()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load("sprites/pipe-green.png")
pipe_surface= pygame.transform.scale2x(pipe_surface)
cano_cima = [400,600,800]
cano_lista = []
spaw_cano = pygame.USEREVENT
pygame.time.set_timer(spaw_cano,1200)
font = pygame.font.Font('GAME_glm.ttf', 32)
text = font.render('BRUNO LUCAS', True, (255,0,0), (0,255,0))

floor_x_position = 0
jogando = True
while True:
    relogio.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jogando == True:
                move_bird = 0
                move_bird -= 12
            if event.key == pygame.K_SPACE and jogando == False:
                jogando = True
                cano_lista.clear()
                bird_rect.center = (100,512)
                move_bird = 0
                
        if event.type == spaw_cano:
            cano_lista.extend(criar_cano())
            print(cano_lista)
    janela.blit(bg_surface,(0,0))
    if not jogando:
        janela.blit(text,(200,10))

        cano_lista.clear()
    if jogando:
        jogando = colisoes(cano_lista)
        move_bird += gravidade
        virar_passaro = virar_p(bird_surface)
        bird_rect.centery += move_bird
        
        janela.blit(virar_passaro,bird_rect)

        cano_lista = move_cano(cano_lista)
        desenhar_canos(cano_lista)

    desenhar_chao()
    floor_x_position -=1
    if floor_x_position <= -576:
        floor_x_position = 0
    pygame.display.update()
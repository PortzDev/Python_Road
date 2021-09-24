import pygame
from random import randint

pygame.init()

janela = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption('Python Road')

x = 590  # pos inic carro jogador  max 900 / min 260
y = 320  # pos inic carro jogador  max 744 / min 0

pos_x = 280  # posição inicial dos outros carros
pos_y = randint(1280, 1530)  # taxi no eixo y
pos_y2 = randint(1850, 2550)  # policia no eixo y
pos_y3 = randint(2900, 3700)  # ambulância no eixo y
timer = 0
segundos = 0

velocidade = 40  # velocidade do carro do jogador
velocidade_outros = 42

fundo = pygame.image.load('asphalt_road.png')
fundo = pygame.transform.scale(fundo, (1280, 1024))  # estica fundo
carro = pygame.image.load('black_mustang.png')
carro = pygame.transform.scale(carro, (150, 310))  # formata carro
police = pygame.image.load('police.png')
police = pygame.transform.scale(police, (210, 360))
cab = pygame.image.load('cab.png')
cab = pygame.transform.scale(cab, (150, 310))
ambulance = pygame.image.load('ambulance.png')
ambulance = pygame.transform.scale(ambulance, (150, 310))

font = pygame.font.SysFont('arial black', 30)  # Placar Temporizador
# Abaixo define a cor da fonte e do fundo
texto = font.render('Time: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()  # define um retângulo atrás do texto
pos_texto.center = (65, 50)  # posiciona o retângulo em x e y

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)  # atualiza a tela a cada 50 milissegundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y >= 0:
        y -= velocidade
    if comandos[pygame.K_DOWN] and y <= 744:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 875:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 245:
        x -= velocidade

    if (pos_y <= -180):  # para o taxi voltar a tela
        pos_y = randint(1280, 1500)
    if (pos_y2 <= -180):  # para a polícia voltar a tela
        pos_y2 = randint(1850, 2550)
    if (pos_y3 <= -180):  # para a ambulância voltar a tela
        pos_y3 = randint(2900, 3700)

    if (timer < 20):  # 20 * 50 milissegundos (do while) = 1 segundo
        timer += 1
    else:  # a cada 20 voltas no while dá um segundo e cai no else
        segundos += 1
        texto = font.render(f'Time: {str(segundos/10)}', True,
                            (255, 255, 255), (0, 0, 0))

    pos_y -= velocidade_outros + randint(0, 2)  # táxi
    pos_y2 -= velocidade_outros + randint(4, 7)  # polícia
    pos_y3 -= velocidade_outros + randint(10, 12)  # ambulância

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(cab, (pos_x, pos_y))
    janela.blit(police, (pos_x + 250, pos_y2))
    janela.blit(ambulance, (pos_x + 540, pos_y3))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()

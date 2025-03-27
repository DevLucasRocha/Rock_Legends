import pygame

# Inicializa o Pygame
pygame.init()

# Configuração da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Luta 2D")

# Carregar spritesheet
spritesheet = pygame.image.load("/GameTest/imagens/mini-riu.png")

# Configuração dos quadros de animação
frame_largura = spritesheet.get_width() // 4  # Divide a largura total pelo número de quadros
frame_altura = spritesheet.get_height()
num_quadros = 4  # Quantidade de quadros na spritesheet

# Lista para armazenar os quadros da animação
frames = []
for i in range(num_quadros):
    frame = spritesheet.subsurface((i * frame_largura, 0, frame_largura, frame_altura))
    frames.append(frame)

# Posição inicial do personagem
x, y = 200, 400
velocidade = 5

# Controle de animação
indice_frame = 0
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    clock.tick(10)  # Controla a velocidade da animação
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()
    movendo = False

    # Movimentação do personagem e troca de animação
    if teclas[pygame.K_a] and x > 0:
        x -= velocidade
        movendo = True
    if teclas[pygame.K_d] and x < LARGURA - frame_largura:
        x += velocidade
        movendo = True
    if teclas[pygame.K_w] and y > 0:
        y -= velocidade
        movendo = True
    if teclas[pygame.K_s] and y < ALTURA - frame_altura:
        y += velocidade
        movendo = True

    # Atualizar quadro da animação
    if movendo:
        indice_frame = (indice_frame + 1) % num_quadros
    else:
        indice_frame = 0  # Quadro parado

    # Atualiza a tela
    tela.fill((0, 0, 0))  # Fundo preto
    tela.blit(frames[indice_frame], (x, y))
    pygame.display.update()

pygame.quit()

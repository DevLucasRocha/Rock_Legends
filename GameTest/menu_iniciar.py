import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Luta 2D")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Carregar fontes
font = pygame.font.Font(None, 36)

# Carregar imagens de fundo
background_menu = pygame.image.load("sprites/menu_background.png")
background_selection = pygame.image.load("sprites/selection_background.png")
background_fight = pygame.image.load("sprites/fight_background.png")

# Carregar sprites dos personagens
player1_sprite = pygame.image.load("sprites/player1.png")
player2_sprite = pygame.image.load("sprites/player2.png")

# Carregar sons
effect_punch = pygame.mixer.Sound("sounds/punch.wav")
effect_kick = pygame.mixer.Sound("sounds/kick.wav")
effect_special = pygame.mixer.Sound("sounds/special.wav")
menu_music = "sounds/menu_music.mp3"
pygame.mixer.music.load(menu_music)
if options["music"]:
    pygame.mixer.music.play(-1)

# Lista de personagens e golpes especiais
characters = {
    "Ryu": {"special": "Hadouken"},
    "Ken": {"special": "Shoryuken"},
    "Chun-Li": {"special": "Kikoken"},
    "Guile": {"special": "Sonic Boom"},
    "Zangief": {"special": "Spinning Piledriver"},
    "Blanka": {"special": "Electric Thunder"},
    "Dhalsim": {"special": "Yoga Fire"},
    "Bison": {"special": "Psycho Crusher"}
}

# Níveis de dificuldade
difficulty_levels = {"Fácil": (1, [0, 2, 5]), "Comum": (2, [5, 5, 10]), "Difícil": (3, [5, 10, 15]), "Kratos": (4, [10, 15, 20])}
difficulty = None

# Estado do jogo
game_state = "menu"
selected_character_p1 = None
selected_character_p2 = None

# Configuração dos jogadores
player1 = {"x": 200, "y": 400, "health": 100}
player2 = {"x": 600, "y": 400, "health": 100}

# Opções do jogo
options = {"music": True, "controls": {"attack_weak": pygame.K_j, "attack_strong": pygame.K_k, "special": pygame.K_l, "kick_weak": pygame.K_u, "kick_strong": pygame.K_i, "jump": pygame.K_SPACE}}

# Função para desenhar o menu inicial
def draw_menu():
    screen.blit(background_menu, (0, 0))
    text = font.render("Pressione ENTER para iniciar | Configurações: C", True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))

# Função para desenhar configurações
def draw_settings():
    screen.blit(background_menu, (0, 0))
    text = font.render("Configurações: (M) Música: {}".format("ON" if options["music"] else "OFF"), True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, 100))
    
# Loop principal
def main():
    global game_state, selected_character_p1, selected_character_p2, difficulty
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(WHITE)
        
        if game_state == "menu":
            draw_menu()
        elif game_state == "settings":
            draw_settings()
        elif game_state == "selection":
            draw_character_selection()
        elif game_state == "difficulty":
            draw_difficulty_selection()
        elif game_state == "fight":
            draw_fight_scene()
            handle_fight()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == "menu":
                    if event.key == pygame.K_RETURN:
                        game_state = "selection"
                    elif event.key == pygame.K_c:
                        game_state = "settings"
                elif game_state == "settings":
                    if event.key == pygame.K_m:
                        options["music"] = not options["music"]
                        if options["music"]:
                            pygame.mixer.music.play(-1)
                        else:
                            pygame.mixer.music.stop()
                        game_state = "menu"
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

# Inicia o jogo
if __name__ == "__main__":
    main()

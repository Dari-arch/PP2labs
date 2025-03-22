import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("red.png")
        # Resize the enemy image to match the player's car size
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gonka.png")
        # Resize the player image to a larger size
        self.image = pygame.transform.scale(self.image, (60, 120))  # Enlarged size
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        # Move the player left and right (no vertical movement)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coinn.png")  # Replace with your coin image
        # Resize the coin image to a reasonable size
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Function to restart the game
def restart_game():
    global score
    global player_group
    global enemy_group
    global coin_group
    global P1, E1, coin

    score = 0
    P1 = Player()
    E1 = Enemy()
    coin = Coin()

    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()

    player_group.add(P1)
    enemy_group.add(E1)
    coin_group.add(coin)


def game_over_screen():
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("Game Over", True, BLACK)
    restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)
    
    # Proper positioning of the texts
    game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    DISPLAYSURF.blit(game_over_text, game_over_text_rect)
    DISPLAYSURF.blit(restart_text, restart_text_rect)

    pygame.display.update()


# Initialize game elements
P1 = Player()
E1 = Enemy()
coin = Coin()

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

player_group.add(P1)
enemy_group.add(E1)
coin_group.add(coin)

score = 0
font = pygame.font.SysFont(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    coin.move()

    # Check for collision with coin
    if pygame.sprite.collide_rect(P1, coin):
        score += 1
        coin = Coin()  # Create new coin
        coin_group.empty()  # Remove the old coin from the group
        coin_group.add(coin)

    # Check for collision with enemy (game over condition)
    if pygame.sprite.collide_rect(P1, E1):
        for i in range(60):  # Animation to make the car fly out of the screen
            DISPLAYSURF.fill(WHITE)
            P1.rect.move_ip(0, -10)  # Move upwards (flying out)
            P1.draw(DISPLAYSURF)
            E1.draw(DISPLAYSURF)
            coin.draw(DISPLAYSURF)
            pygame.display.update()
            FramePerSec.tick(FPS)
        game_over_screen()
        while True:  # Wait for user input to restart or quit
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[K_r]:
                restart_game()
                break
            if keys[K_q]:
                pygame.quit()
                sys.exit()

    # Drawing everything
    DISPLAYSURF.fill(WHITE)

    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    coin.draw(DISPLAYSURF)

    # Display score
    score_text = font.render(f"Coins: {score}", True, BLACK)
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH - 120, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)

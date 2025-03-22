import pygame
import random

# Константы игры
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Функция для генерации еды вне змейки и стен
def generate_food(snake):
    while True:
        x, y = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            return x, y

# Основной цикл игры
def game():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)
    food = generate_food(snake)
    running = True
    score = 0
    level = 1
    speed = 10

    while running:
        screen.fill(BLACK)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        # Движение змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        # Проверка на столкновение с границами
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            running = False
        
        # Проверка на столкновение с собой
        if new_head in snake:
            running = False
        
        # Добавляем новую голову
        snake.insert(0, new_head)
        
        # Проверка, съедена ли еда
        if new_head == food:
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 2
            food = generate_food(snake)
        else:
            snake.pop()
        
        # Отрисовка змейки и еды
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        
        # Отображение счета и уровня
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()

if __name__ == "__main__":
    game()


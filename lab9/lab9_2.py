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

# Функция для генерации еды с случайным весом и временем исчезновения
def generate_food(snake):
    while True:
        # Генерация случайной позиции для еды
        x, y = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            # Вес еды случайным образом от 1 до 5
            weight = random.randint(1, 5)
            # Время жизни еды (таймер) от 5 до 15 секунд
            timer = random.randint(5, 15)
            return x, y, weight, timer

# Основной цикл игры
def game():
    snake = [(100, 100), (80, 100), (60, 100)]  # Начальное положение змейки
    direction = (GRID_SIZE, 0)  # Начальное направление движения
    food_x, food_y, food_weight, food_timer = generate_food(snake)  # Генерация еды
    food_time_remaining = food_timer  # Время жизни еды
    running = True
    score = 0
    level = 1
    speed = 10

    while running:
        screen.fill(BLACK)

        # Обработка событий (управление и выход)
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
        if new_head == (food_x, food_y):
            score += food_weight  # Добавляем вес еды к счёту
            if score % 3 == 0:
                level += 1
                speed += 2  # Увеличиваем скорость с каждым уровнем
            food_x, food_y, food_weight, food_timer = generate_food(snake)  # Генерация новой еды
            food_time_remaining = food_timer  # Сброс времени жизни новой еды
        else:
            snake.pop()

        # Таймер для еды (если еда исчезает через время)
        if food_time_remaining > 0:
            food_time_remaining -= 1  # Уменьшаем время жизни
        else:
            # Если еда исчезла, генерируем новую
            food_x, food_y, food_weight, food_timer = generate_food(snake)
            food_time_remaining = food_timer

        # Отрисовка змейки
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        # Отрисовка еды с отображением веса
        pygame.draw.rect(screen, RED, (food_x, food_y, GRID_SIZE, GRID_SIZE))
        # Отображаем вес еды
        weight_text = font.render(str(food_weight), True, WHITE)
        screen.blit(weight_text, (food_x + GRID_SIZE // 4, food_y + GRID_SIZE // 4))

        # Отображение счёта и уровня
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(speed)  # Управление скоростью игры
    
    pygame.quit()

if __name__ == "__main__":
    game()

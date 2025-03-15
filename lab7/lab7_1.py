import pygame


pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")


BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
MOVE_DISTANCE = 20


running = True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and ball_x - BALL_RADIUS - MOVE_DISTANCE >= 0:
        ball_x -= MOVE_DISTANCE
    if keys[pygame.K_RIGHT] and ball_x + BALL_RADIUS + MOVE_DISTANCE <= WIDTH:
        ball_x += MOVE_DISTANCE
    if keys[pygame.K_UP] and ball_y - BALL_RADIUS - MOVE_DISTANCE >= 0:
        ball_y -= MOVE_DISTANCE
    if keys[pygame.K_DOWN] and ball_y + BALL_RADIUS + MOVE_DISTANCE <= HEIGHT:
        ball_y += MOVE_DISTANCE
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.update()

pygame.quit()


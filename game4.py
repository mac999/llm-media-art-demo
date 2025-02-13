import pygame
pygame.init()
screen = pygame.display.set_mode((600,400))
surface = pygame.Surface((600,400), pygame.SRCALPHA)
opacity = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255,255,255))
    surface.fill((255,0,0,opacity))
    screen.blit(surface, (0,0))
    pygame.display.flip()
    clock.tick(60)
    if opacity < 255:
        opacity += 1
import pygame
pygame.init()
tela = pygame.display.set_mode([500, 500])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (250, 250, 250), (250, 250), 75)
    pygame.display.flip()
pygame.quit()
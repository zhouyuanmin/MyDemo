import pygame
import inspect

pygame.init()
screen = pygame.display.set_mode((600, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(inspect.getdoc('pygame.mouse.get_pos'))
            # print(inspect.getmodulename('pygame.mouse.get_pos'))
            print('pygame.mouse.get_pos()', pygame.mouse.get_pos())
    pygame.draw.rect(screen, (99, 0, 0), (100, 100, 100, 100))
    pygame.display.update()

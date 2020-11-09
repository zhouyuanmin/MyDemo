import pygame

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((600, 500))  # 创建窗口
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            running = False
        elif event.type == pygame.KEYDOWN:
            print(event.key)

    pygame.draw.rect(screen, (255, 255, 0), (300, 200, 100, 100))
    pygame.display.update()  # 刷新窗口
pygame.quit()
print('测试能否执行')

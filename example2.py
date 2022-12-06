import pygame
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

my_image = pygame.image.load("test_mask_lv2.jpg").convert_alpha()

# уменьшил до размера (100, 100)
scaled_image = pygame.transform.scale(my_image, (100, 100))

angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
                # пишем свой код
    # обновляем значения
    angle += 1
    # рисуем
    screen.fill((200, 100, 0))
    screen.blit(my_image, (0, 0))

    # исходное изображение поворачивается на значение переменной angle
    # и записывается в перменную rotated_image


    pygame.display.flip()
    clock.tick(10)
pygame.quit()
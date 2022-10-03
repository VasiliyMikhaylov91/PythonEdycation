import pygame
import random
import os

# настройка папки ассетов

WIDTH = 660  # ширина игрового окна
HEIGHT = 880 # высота игрового окна
FPS = 30 # частота кадров в секунду

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    
    def update(self):
        global flag_move
        match flag_move:
            case 'left':
                self.rect.x -= 5
            case 'right':
                self.rect.x += 5
            case 'up':
                self.rect.y -= 5
            case 'down':
                self.rect.y += 5
        if self.rect.right == WIDTH:
            flag_move = 'up'
        if self.rect.top == 0:
            flag_move = 'left'
        if self.rect.left == 0:
            flag_move = 'down'
        if self.rect.bottom == HEIGHT and self.rect.right != WIDTH:
            flag_move = 'right'
        

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

game_folder = os.path.dirname('G:\GeekBrains\PythonEdycation\homeworks\Lesson9a\game\my_game.py')
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()


player = Player()
all_sprites.add(player)

# Цикл игры
running = True
flag_move = 'right'
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Отрисовка
    screen.fill(BLUE)
    all_sprites.draw(screen)
    
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
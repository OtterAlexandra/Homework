import pygame
import sys
from itertools import product


def start_screen():
    background_image = pygame.image.load('data/fon.jpg')
    background_image = pygame.transform.scale(background_image, size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return

        screen.fill('black')
        screen.blit(background_image, (0, 0))
        pygame.display.flip()


Tile_size = 50
file = list(map(str.strip, sys.stdin.readlines()))


class Tile(pygame.sprite.Sprite):
    type2image = {'.': pygame.transform.scale(pygame.image.load('data/grass.png'), (Tile_size, Tile_size)),
                  '#': pygame.transform.scale(pygame.image.load('data/box.png'), (Tile_size, Tile_size))}

    def __init__(self, pos, type, *groups):
        super().__init__(*groups)
        self.image = Tile.type2image[type]
        self.rect = self.image.get_rect().move(pos)
        self.type = type


class Hero(pygame.sprite.Sprite):
    image = pygame.transform.scale(pygame.image.load('data/mar.png'), (Tile_size, Tile_size))

    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = Hero.image
        self.rect = Hero.image.get_rect().move(pos)


def load_map(path):
    with open(path, mode='r') as file:
        return [list(row.rstrip('\n')) for row in file]


def generate(map):
    tile_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    player = None
    for i, j in product(range(len(map)), range(len(map[0]))):
        if map[i][j] == '@':
            Tile((j * Tile_size, i * Tile_size), '.', tile_group)
            player = Hero((j * Tile_size, i * Tile_size), player_group)
        else:
            Tile((j * Tile_size, i * Tile_size), map[i][j], tile_group)
    return player, tile_group, player_group


player, text_level, player_group = generate(load_map('data/map_1.txt'))

pygame.init()
size = (800, 600)
running = True
screen = pygame.display.set_mode(size)

start_screen()

try:
    a = 'data/' + file[0]
    player, test_level, play = generate(load_map(a))
except Exception:
    print('Error')
    exit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            last_pos = player.rect.x, player.rect.y
            if event.key == pygame.K_UP:
                player.rect.move_ip((0, -Tile_size))
            elif event.key == pygame.K_DOWN:
                player.rect.move_ip((0, Tile_size))
            if event.key == pygame.K_RIGHT:
                player.rect.move_ip((Tile_size, 0))
            elif event.key == pygame.K_LEFT:
                player.rect.move_ip((-Tile_size, 0))

            collid = pygame.sprite.spritecollide(player, text_level, dokill=False)
            for col in collid:
                if col.type == '#':
                    player.rect.x, player.rect.y = last_pos
                    break

    screen.fill('black')
    text_level.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()

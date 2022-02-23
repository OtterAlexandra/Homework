import random

import pygame as pg

pg.init()
size = width, height = 500, 500
screen = pg.display.set_mode(size)


class Bomb(pg.sprite.Sprite):
    image = pg.image.load("data/bomb.png")
    image_boom = pg.image.load("data/boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 450)
        self.rect.y = random.randint(0, 449)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


bomb_group = pg.sprite.Group(Bomb())
for _ in range(20):
    Bomb(bomb_group)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black')
    bomb_group.update(event)
    bomb_group.draw(screen)
    pg.display.flip()

pg.quit()

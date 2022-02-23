import random

import pygame as pg

pg.init()
size = width, height = 600, 300
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 200


class GO(pg.sprite.Sprite):
    image = pg.image.load("data/gameover.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GO.image
        self.rect = self.image.get_rect()
        self.rect.x = -600

    def update(self, *args):
        if self.rect.x != 0:
            self.rect.x += 1


go_group = pg.sprite.Group(GO())

running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('blue')
    go_group.update()
    go_group.draw(screen)
    pg.display.flip()

pg.quit()

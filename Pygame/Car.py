import pygame as pg

pg.init()
pg.display.set_caption('Машинка')
size = width, height = 600, 95
screen = pg.display.set_mode(size)

clock = pg.time.Clock()
fps = 30


class Car(pg.sprite.Sprite):
    image = pg.image.load('data/car.png')

    def __init__(self):
        super().__init__()
        self.pos = (0, 0)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(0, 0)
        self.rect.center = 75, 48
        self.t = True

    def update(self):
        if self.t:
            self.rect.x += 10
        else:
            self.rect.x -= 10

        if self.rect.left > width - 150:
            self.t = False
            self.image = pg.transform.flip(self.image, True, False)
        elif self.rect.right < 150:
            self.t = True
            self.image = pg.transform.flip(self.image, True, False)


running = True
car_group = pg.sprite.Group(Car())

while running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    dt = clock.tick() / 1000

    screen.fill('white')
    car_group.update()
    car_group.draw(screen)
    pg.display.flip()
pg.quit()

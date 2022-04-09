import pygame as pg
from itertools import product


class CellMatrix:

    def __init__(self, width, height, position=(50, 50), cell_size=50):
        self._width = width
        self._height = height
        self._pos = position
        self._cs = cell_size
        self._state = [[0] * height for _ in range(width)]
        self._counter = 0  # 0 - синий, 1 - красный
        self._track = [[0] * height for _ in range(width)]

    def get_cell(self, mouse_pos):  # work all
        result_x = (mouse_pos[0] - self._pos[0]) // self._cs
        result_y = (mouse_pos[1] - self._pos[1]) // self._cs
        if result_x > self._width or result_x < 0 or result_y > self._width or result_y < 0:
            return None
        return result_x, result_y

    def on_click(self, cell):  # work all
        if self._state[cell[0]][cell[1]] == 0:
            self._state[cell[0]][cell[1]] = 1
            self._track[cell[0]][cell[1]] = self._counter
        self._counter = 1 - self._counter

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)

    def draw(self, surface):
        for x, y in product(range(self._width), range(self._height)):
            pg.draw.rect(surface, (255, 255, 255),
                         (x * self._cs + self._pos[0],
                          y * self._cs + self._pos[0],
                          self._cs, self._cs), width=1)

            if self._state[x][y] > 0:
                if self._track[x][y] == 0:
                    pg.draw.circle(surface, (0, 0, 255),
                                   ((x + 0.5) * self._cs + self._pos[0], (y + 0.5) * self._cs + self._pos[0]),
                                   self._cs / 2 - 2)
                elif self._track[x][y] == 1:
                    pg.draw.circle(surface, (255, 0, 0),
                                   ((x + 0.5) * self._cs + self._pos[0], (y + 0.5) * self._cs + self._pos[0]),
                                   self._cs / 2 - 2)


size = (640, 480)
pg.init()
screen = pg.display.set_mode(size)
board = CellMatrix(7, 7)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            board.process_click(event.pos)
    screen.fill((0, 0, 0))
    board.draw(screen)
    pg.display.flip()

pg.quit()

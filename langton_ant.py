from langton_grid import Grid
from langton_window import Window


class Ant:
    """
    Klasa reprezentujaca
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lastX = x
        self.lastY = y
        self.dir = (1, 0)

    def rotate_left(self):
        self.dir = (-self.dir[1], self.dir[0])

    def rotate_right(self):
        self.dir = (self.dir[1], -self.dir[0])

    def forward(self):
        self.lastX = self.x
        self.lastY = self.y
        self.x += self.dir[0]
        self.y += self.dir[1]

    def left(self):
        self.rotate_left()
        self.forward()

    def right(self):
        self.rotate_right()
        self.forward()

    def draw(self, window: Window, grid: Grid):
        window.draw_rect(
            (0, 0, 0) if grid.g[self.lastX][self.lastY] == 0 else
            (255, 255, 255), self.lastX * grid.cellW, self.lastY * grid.cellH,
            grid.cellW, grid.cellH)
        window.draw_rect(
            (255, 0, 0), self.x * grid.cellW, self.y * grid.cellH, grid.cellW,
            grid.cellH)

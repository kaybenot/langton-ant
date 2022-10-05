from langton_window import Window


class Grid:
    """
    Klasa reprezentujaca plansze, po ktorej porusza sie mrowka.
    """
    def __init__(self, w, h, windowW, windowH):
        '''
        Inicjalizacja planszy
        '''
        self.w = w
        self.h = h
        self.g = [[0 for y in range(h)] for x in range(w)]
        self.cellW = windowW / w
        self.cellH = windowH / h

    def step(self, x, y, window: Window):
        '''
        Funkcja wykonuje krok mrowki na planszy we wskazanym miejscu.
        '''
        if x >= self.w or y >= self.h or x < 0 or y < 0:
            return -1
        else:
            retVal = self.g[x][y]
            self.g[x][y] = 1 if self.g[x][y] == 0 else 0
            color = (255, 255, 255) if self.g[x][y] == 1 else (0, 0, 0)
            window.draw_rect(
                color, x * self.cellW, y * self.cellH, self.cellW, self.cellH)
            return retVal

    def draw(self, x, y, window: Window):
        '''
        Funkcja wykonuje rysowanie kwadratu na planszy we wskazanym miejscu.
        '''
        x = int(x // self.cellW)
        y = int(y // self.cellH)
        if x >= self.w or y >= self.h or x < 0 or y < 0:
            return -1
        else:
            retVal = self.g[x][y]
            self.g[x][y] = 1 if self.g[x][y] == 0 else 0
            color = (255, 255, 255) if self.g[x][y] == 1 else (0, 0, 0)
            window.draw_rect(
                color, x * self.cellW, y * self.cellH, self.cellW, self.cellH)
            return retVal

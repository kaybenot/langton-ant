from langton_ant import *
from langton_grid import *


class Mechanic:
    """
    Klasa zajmujaca sie plansza i mrowka Langtona.
    """
    def __init__(self, gridW, gridH, windowW, windowH):
        '''
        Inicjalizacja planszy i mrowki Langtona.
        '''
        self.ant = Ant(gridW // 2, gridH // 2)
        self.grid = Grid(gridW, gridH, windowW, windowH)

    def mechanic_step(self, window):
        '''
        Funkcja wykonuje krok mrowki i aktualiazuje plansze.
        '''
        gridVal = self.grid.step(self.ant.x, self.ant.y, window)
        self.ant.draw(window, self.grid)
        if gridVal == -1:
            return False
        elif gridVal == 0:
            self.ant.right()
        else:
            self.ant.left()
        return True

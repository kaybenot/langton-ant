from pygame import draw
from langton_mechanic import *
from langton_window import *
import time


class Langton:
    """
    Klasa laczaca wszystkie moduly, prowadzi glowna petle programu.
    """
    def __init__(self, windowW, windowH, w, h, fps, drawing):
        '''
        Funkcja inicjalizuje moduly i ustawia licznik czasu klatek.
        '''
        self.window = Window(windowW, windowH)
        self.mechanic = Mechanic(w, h, windowW, windowH)
        self.running = True
        self.frame_time = 1 / fps
        self.drawing = drawing

    def draw_grid(self):
        '''
        Funkcja zajmujaca sie rysowaniem planszy przed gra.
        '''
        draw_running = True
        while draw_running:
            draw_running = self.window.poll_events_draw(self.mechanic.grid)
            self.window.swap_frame()

    def run(self):
        '''
        Funkcja zawiera glowna petle programu, wykonuje mechanike dzialania
        mrowki Langtona co klatke. Klatka wykonywana jest co okreslony czas.
        Po wyjsciu za ekran lub po pierwszej probie zamkniecia okna, program
        sie pauzuje.
        '''
        if self.drawing:
            self.draw_grid()
        start = time.time()
        while self.running:
            now = time.time()
            self.running = self.window.poll_events()
            if now - start >= self.frame_time:
                inBounds = self.mechanic.mechanic_step(self.window)
                self.window.swap_frame()
                start += self.frame_time
                if not inBounds:
                    self.running = False
        while True:
            if not self.window.poll_events():
                break

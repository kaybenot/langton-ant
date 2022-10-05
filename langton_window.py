import pygame


class Window:
    """
    Klasa zajmujaca sie wyswietlaniem okna, odswierzaniem go
    i wychwytywaniem eventow
    """
    def __init__(self, w, h):
        '''
        Inicjalizacja okna.
        '''
        self.surface = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Mrowka Langtona")
        self.surface.fill((0, 0, 0))

    def poll_events(self):
        '''
        Funkcja wychwytujaca eventy okna.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def poll_events_draw(self, grid):
        '''
        Funkcja wychwytuje eventy okna oraz lewego przycisku myszy.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                grid.draw(pos[0], pos[1], self)
        return True

    def swap_frame(self):
        '''
        Funkcja aktualizuje klatke.
        '''
        pygame.display.flip()

    def draw_rect(self, color, x, y, w, h):
        '''
        Funkcja rysuje kwadrat we wskazanych koordynatach,
        o określonych rozmiarach i w określonym kolorze.
        '''
        pygame.draw.rect(self.surface, color, pygame.Rect(x, y, w, h))

import pygame
class ChessBoard:
    def __init__(self):
        self.size = 8
        self.square_size = 60
        self.colors = [(245, 222, 179), (139, 69, 19)]  # Белые/коричневые поля
        
    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(screen, color, 
                               (col * self.square_size, row * self.square_size, 
                                self.square_size, self.square_size))
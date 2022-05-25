import pygame

# windows and box size 
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS 

# rgb colors 
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0 )
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# assets as constants
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (20, 20))

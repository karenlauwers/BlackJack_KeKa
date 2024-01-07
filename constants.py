import pygame 
import sys

pygame.init()

#settings for frame per second 
fps = 60
clock = pygame.time.Clock()

#window settings 
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

#playing with colors 
black = (0, 0, 0)
white = (255, 255, 255)
casino_green1 = (39, 139, 34)
casino_green2 = (30, 92, 58)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (220, 220, 220)
dark_grey = (90, 90, 90)
dark_red = (139, 0, 0)
yellow_gold = (255, 223, 0)

#playing with font sizes
font_size1 = pygame.font.SysFont('Agency FB', 22)
font_size2 = pygame.font.SysFont('Agency FB', 30)
font_size3 = pygame.font.SysFont('Agency FB', 50)
font_size4 = pygame.font.SysFont('Agency FB', 70)
font_size5 = pygame.font.SysFont('Agency FB', 100)

ranks = ['A', '2', '3', '4', '5', '6',  '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'S', 'H', 'D']
deck_count = 3 # only works with deck_count < 10
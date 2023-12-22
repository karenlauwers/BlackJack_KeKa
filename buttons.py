import pygame
from constants import *

pygame.init() 

#create a class for the Buttons
#by creating a class, we can create different buttons in the game, without having to define the variables over and over again
#every button in the game will have text, a position on the screen, will be enabled or disabled (can click on it or not) and a size (width, height)
class Button: 
  def __init__(self, text, x_pos, y_pos, enabled, button_width, button_height): 
    self.text = text 
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.enabled = enabled
    self.button_width = button_width
    self.button_height = button_height
    self.draw()

#We must place the text in a rectangle to put it in a certain position and with a certain shape on the screen. 
#We call the function 'draw' every time we create a button (see def __init__ of the class)
  def draw(self): 
    button_text = font_size1.render(self.text, True, white)
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))
    if self.enabled: 
      if self.check_click():
        pygame.draw.rect(window, dark_grey, button_rect, 0, 5)
      else: 
        pygame.draw.rect(window, dark_red, button_rect, 0, 5)
    else: 
        pygame.draw.rect(window, casino_green1, button_rect, 0, 5)
    pygame.draw.rect(window, black, button_rect, 2, 5)
    window.blit(button_text, (self.x_pos+35, self.y_pos+15))

#features: if the button is enabled and you click on it, then the colour changes. 
#If the button is disabled (so you won't be able to click on it), the button gets another colour.
  def check_click(self):
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))

    if left_click and button_rect.collidepoint(mouse_pos) and self.enabled: 
      return True 
    else: 
      return False 
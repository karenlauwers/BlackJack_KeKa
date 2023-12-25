import pygame
from constants import *

pygame.init() 

# CREATE BUTTON CLASS
#By creating a class, we can create different buttons in the game, without having to define the variables over and over again
#Every button in the game will have text, a position on the screen, will be enabled or disabled (can click on it or not) and a size (width, height)
class Button: 
  def __init__(self, text, x_pos, y_pos, enabled, button_width, button_height): 
    self.text = text 
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.enabled = enabled
    self.button_width = button_width
    self.button_height = button_height
    # self.draw() # If you enable this, function 'draw' is running every time you make an object of the class Button. 
                  # In our game, we want be able to prepare the buttons without drawing them. This is mainly because of the readibility of the code and the ability to keep blocks of code together. 
                  # If we do not call the function 'draw' every time we create a button, this means that we will have to call the function everytime we want to draw and blit the button on the screen.
  
# Function to draw the rectangle in which we put the text, put the text in the rectangle and blit on the screen 
  def draw_button(self): 
    button_text = font_size2.render(self.text, True, white)
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))
    if self.enabled: 
      if self.check_click():
        pygame.draw.rect(window, dark_grey, button_rect, 0, 5) 
      else: 
        pygame.draw.rect(window, dark_red, button_rect, 0, 5)
    else: 
        pygame.draw.rect(window, casino_green1, button_rect, 0, 5)
    pygame.draw.rect(window, dark_grey, button_rect, 2, 5) # kader om het vak heen 
    window.blit(button_text, (self.x_pos+10, self.y_pos+10))

# Function to check if the button is clicked 
# Features: if the button is enabled and you click on it, then the colour changes. 
# If the button is disabled (so you won't be able to click on it), the button gets another colour.
  def check_click(self):
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.button_width, self.button_height))

    if left_click and button_rect.collidepoint(mouse_pos) and self.enabled: 
      return True 
    else: 
      return False 

# BUTTONS 
button_1player = Button('1 player',320, 150, True, 130, 50)
button_2player = Button('2 players', 320, 220, True, 130, 50)   
bet_ok1 = Button('Ok', 300, 180, False, 70, 50) # button to click in betscreen by player 1, as well in 1- as 2playergame
bet_ok2 = Button('Ok', 300, 290, False, 70,50) # button to click in betscreen by player 2 in 2playergame
play = Button('Play', 630, 240, False, 70,50) 
hit1 = Button('Hit', 110, 50, True, 70, 40)
stand1 = Button('Stand', 190, 50, True, 70, 40)
split1 = Button('Split', 270, 50, True, 70, 40 )
hit2 = Button('Hit', 490, 50, True, 70, 40)
stand2 = Button('Stand', 570, 50, True, 70, 40)
split2 = Button('Split', 650, 50, True, 70, 40 )
# double1 = Button('Double', 190, True, 70, 50 )
# quit = Button('Quit', 190, True, 70, 50 ) 
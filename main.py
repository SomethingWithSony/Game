import pygame

class Game:

  def __init__(self):
    WIDTH = 640
    HEIGHT = 320
    # Initialize pygame
    pygame.init()
    
    pygame.display.set_caption("Game")
    
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.display = pygame.Surface((WIDTH // 2, HEIGHT // 2))
    
    self.screen = 'Game'
    self.game_state = '' # Running , Paused / InMenu
    
    self.clock = pygame.time.Clock()
    self.is_running = True
    
  def screen_manager(self):
    while self.is_running:
      match self.screen:
        case 'Main Menu':
          pass
        case 'Game':
          self.game_loop()
        case 'Game Over':
          pass
    
    pygame.quit()
  
  def grid(self):
    pass
  
  def game_loop(self):
    self.display.fill((0,0,0))
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.is_running = False
    
    self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()) , (0, 0)) # Scale up 
    pygame.display.update() 

    self.clock.tick(60) # Lock framerate at 60fps
      

  
Game().game_loop()
    
    
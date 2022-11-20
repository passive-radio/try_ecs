import pygame
from dataclasses import dataclass
from utils import font

class Level():
    
    def __init__(self, is_start_scene: bool, window: pygame.Surface, screen_size: tuple, clear_color: tuple = (0,0,0), fps: int = 60) -> None:
        self.ative_scene = 0
        self.is_start_scene = is_start_scene
        self.window = window
        self.screen_size = screen_size
        self.clock = pygame.time.Clock()
        self.clear_color = clear_color
        self.FPS = fps
        self.font = pygame.font.Font(None, 64)
    def start_menu(self):
        while self.is_start_scene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_start_scene = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_start_scene = False
                    if event.key == pygame.K_RETURN:
                        self.is_start_scene = False
            
            self._render_start_menu()
            self.clock.tick(30)
    
    def _render_start_menu(self):
        self.window.fill(self.clear_color, pygame.Rect(0,0,self.screen_size[0], self.screen_size[1]))
        text_start = self.font.render("Start", True, (224,224,224))
        self.window.blit(text_start, [self.screen_size[0]/2 - text_start.get_size()[0]/2, self.screen_size[1]/2 - text_start.get_size()[1]/2])
        
        text_notion = font.set_text("Please Enter to start!", 32, (224,224,224))
        self.window.blit(text_notion, [self.screen_size[0]/2 - text_notion.get_size()[0]/2, 60 + self.screen_size[1]/2 - text_notion.get_size()[1]/2])
        
        pygame.display.flip()
        
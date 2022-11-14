import pygame
from . import component

class System():
    priority: int = 0
    world = 'World'
    
    def process(self, *args, **kwargs):
        pass
    
class MovementSystem(System):
    
    def __init__(self, max: tuple, min: tuple = (0,0)) -> None:
        super().__init__()
        self.minx = min[0]
        self.miny = min[1]
        self.maxx = max[0]
        self.maxy = max[1]
        
    
    def process(self):
        for ent, (vel, rend) in self.world.get_components(component.VelocityComponent, component.RenderableComponent):
            rend.x += vel.x
            rend.y += vel.y
            rend.x = min(self.maxx-rend.w, max(self.minx, rend.x))
            rend.y = min(self.maxy-rend.h, max(self.miny, rend.y))
            

class RenderSystem(System):
    
    def __init__(self, window, clear_color: tuple=(0,0,0)) -> None:
        super().__init__()
        self.window = window
        self.clear_color = clear_color
        
    def process(self):
        self.window.fill(self.clear_color)
        
        for ent, rend in self.world.get_component(component.RenderableComponent):
            try: 
                self.window.blit(rend.rend_image, (rend.x, rend.y))
            except:
                self.window.blit(rend.image, (rend.x, rend.y))
        
        pygame.display.flip()
        

class KeyControlSystem(System):
    
    def __init__(self, move_speed: int = 1) -> None:
        super().__init__()
        self.dx = move_speed
        self.dy = move_speed
        
    def process(self):
        
        for ent, (playable_comp, vel, rend) in self.world.get_components(component.PlayableComponent, component.VelocityComponent, component.RenderableComponent):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.world.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.world.running = False
                    elif event.key == pygame.K_LEFT:
                        vel.x = -1*self.dx
                        rend.rend_image = rend.image.subsurface((0,rend.h,rend.w,rend.h))
                    elif event.key == pygame.K_RIGHT:
                        vel.x = self.dx
                        rend.rend_image = rend.image.subsurface((0,rend.h*2,rend.w,rend.h))
                    elif event.key == pygame.K_UP:
                        vel.y = -1*self.dy
                        rend.rend_image = rend.image.subsurface((0,rend.h*3,rend.w,rend.h))
                    elif event.key == pygame.K_DOWN:
                        vel.y = self.dy
                        rend.rend_image = rend.image.subsurface((0,0,rend.w,rend.h))
                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                        vel.x = 0
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        vel.y = 0
                        
class SoundMixerSystem(System):
    def __init__(self, sound, volume=0.1) -> None:
        super().__init__()
        self.bgm = sound
        self.bgm.set_volume(volume)
        
    def process(self):
        self.bgm.play()
        
class CollisionSystem(System):
    def __init__(self) -> None:
        super().__init__()
    
    def process(self, *args, **kwargs):
        
        for ent, (rend) in self.world.get_components(component.RenderableComponent):
            pass
    
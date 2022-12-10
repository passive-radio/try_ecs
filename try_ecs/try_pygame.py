import pygame

from ecs.world import World
from ecs.component import *
from ecs.system import *
import pytmx

from level import Level

import random

FPS = 60
SCREEN_SIZE = (960, 640)

def load_map(filepath: str) -> pytmx.TiledMap:
    from pytmx import load_pygame
    map_image = pytmx.load_pygame(filepath)
    for layer in map_image.layers:
        print("type: ", type(layer.id))
        print(layer.id == 1)
    return map_image

def init() -> tuple[World,pygame.Surface]:
    pygame.init()
    pygame.display.set_caption("猫をうごかそ")
    pygame.display.set_icon(pygame.image.load("material/img/cat_chip01.png").subsurface((2,2,32,32)))
    window = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    world = World()
    
    bgm = pygame.mixer.Sound("material/sound/maodamashi_piano30.mp3")
    
    player_entity = world.create_entity()
    enemy_entity = world.create_entity()
    player_image_chipset = pygame.image.load("material/img/cat_chip01.png")
    enemy_image_chipset = pygame.image.load("material/img/simple_enemy01.png")
    
    map_entity = world.create_entity()
    
    world.add_component_to_entity(player_entity, VelocityComponent(0.0, 0.0))
    world.add_component_to_entity(player_entity, RenderableComponent(100,100, 33, 32, player_image_chipset, player_image_chipset.subsurface((0,0,33,32))))
    world.add_component_to_entity(player_entity, PlayableComponent(playable=True))
    world.add_component_to_entity(player_entity, CollisionComponent())
    world.add_component_to_entity(player_entity, AnimationComponent(step=0))
    world.add_component_to_entity(player_entity, StatsComponent(hp=100))
    
    world.add_component_to_entity(enemy_entity, RenderableComponent(300, 100, 32, 32, enemy_image_chipset, enemy_image_chipset.subsurface((0,0,32,32))))
    world.add_component_to_entity(enemy_entity, CollisionComponent())
    world.add_component_to_entity(enemy_entity, StatsComponent(hp=50))
    
    
    world.add_component_to_entity(map_entity, MapComponent(load_map("material/my_first_map.tmx"), 0, 0))
    
    world.add_system(RenderSystem(window, (255,255,255)), 200)
    world.add_system(KeyControlSystem(move_speed=3), 100)
    world.add_system(MovementSystem(max=SCREEN_SIZE), 0)
    world.add_system(SoundMixerSystem(bgm), 50)
    world.add_system(CollisionSystem(), -1)
    world.add_system(StaticRenderSystem(window), 300)
    world.add_system(AnimationSystem(), 400)
    world.add_system(RandomMovementSystem(max=SCREEN_SIZE), 500)
    return world, window

def main():
    
    world, window = init()
    clock = pygame.time.Clock()
    
    level = Level(True, window, SCREEN_SIZE, (10,10,10), 60)
    level.start_menu()
    
    bombs = []
    bomb_image_chipset = pygame.image.load("material/img/bomb.png")
    
    for _ in range(4):
        bomb = world.create_entity()
        world.add_component_to_entity(bomb, RenderableComponent(100*random.randrange(1, 5,1),50*random.randrange(1,10,1),32,32,bomb_image_chipset, bomb_image_chipset.subsurface((0,0,32,32))))
        world.add_component_to_entity(bomb, CollisionComponent(False))
        world.add_component_to_entity(bomb, VelocityComponent())
        world.add_component_to_entity(bomb, RandomMovementComponent())
        bombs.append(bomb)
    
    while world.running:
            
        world.process()
        clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()
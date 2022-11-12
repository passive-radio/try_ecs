import pygame

from ecs.world import World
from ecs.component import VelocityComponent

if __name__ == "__main__":
    world = World()
    entity1 = world.create_entity()
    velocity_component = VelocityComponent(0.0,0.0)
    world.add_component_to_entity(entity1, velocity_component)
    print(entity1)
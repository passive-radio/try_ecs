from typing import Type
from typing import TypeVar
from dataclasses import dataclass

from .component import Component
from .entity import Entity

version = '0.1'

"""
This module uses dataclass decorator to define the base component class, thus Python 3.7+ is required.
Please change the Python version in your envinment to 3.7 or higher if you uses Python < 3.7.
"""

class World():
    
    def __init__(self) -> None:
        self.components = {}
        self.entities = {}
        self.next_entity_id = 0
        self.systems = []
        
    def create_entity(self,):
        entity = self.next_entity_id
        self.next_entity_id += 1
        return entity

    def add_component_to_entity(self, entity: int, component: Component) -> None:
        component_type = type(component)
        
        if component_type not in self.components:
            self.components[component_type] = set()
        
        if entity not in self.entities:
            self.entities[entity] = {}
        
        """
        Add entity id in the components[component_type] set where every entities which have the component: component_type is stored.
        Add component in the entities[entity] dict where every components which consists the entit stored.
        """
        self.components[component_type].add(entity)
        self.entities[entity].setdefault(component_type, component)
        
    def get_entity_object(self, entity: int):
        return self.entities[entity]
    
if __name__ == "__main__":
    import component as ecs_component
    world = World()
    entity1 = world.create_entity()     # -> 0
    entity2 = world.create_entity()     # -> 1
    print(f"entity1: {entity1}, entity2: {entity2}")
    
    vel_com = ecs_component.VelocityComponent(1.1,1.1)
    world.add_component_to_entity(entity1, vel_com)
    print(world.get_entity_object(entity1))
    
from typing import Type
from typing import TypeVar
from dataclasses import dataclass

version = '0.1'

"""
This module uses dataclass decorator to define the base component class, thus Python 3.7+ is required.
Please change the Python version in your envinment to 3.7 or higher if you uses Python < 3.7.
"""

@dataclass
class Entity:
    """
    The base entity class used in this ecs module
    """
    id: int
    
if __name__ == "__main__":
    import component
    
    vel_com = component.VelocityComponent(1.1,1.1)
    next_entity_id = 1
    entity = Entity(next_entity_id)
    print(entity, entity.id, type(entity))
    

from typing import Type
from typing import TypeVar
from dataclasses import dataclass

from pygame import image as pg_image
import pytmx
version = '0.1'

"""
This module uses dataclass decorator to define the base component class, thus Python 3.7+ is required.
Please change the Python version in your envinment to 3.7 or higher if you uses Python < 3.7.
"""



@dataclass
class Component():
    """
    The base component class used in this ecs module
    """

@dataclass
class VelocityComponent(Component):
    x: float = 0.0
    y: float = 0.0

@dataclass
class PositionComponent(Component):
    x: float = 0.0
    y: float = 0.0

@dataclass
class RenderableComponent(Component):
    x: float = 0.0
    y: float = 0.0
    w: float = 33
    h: float = 36
    image: pg_image = None
    rend_image: pg_image = None
    
@dataclass
class PlayableComponent(Component):
    playable: bool = True
    
@dataclass
class CollisionComponent(Component):
    isCollided: bool = False
    
@dataclass
class MapComponent(Component):
    image: pytmx.TiledMap
    x: int = 0
    y: int = 0
    layer: int = 1

if __name__ == "__main__":
    test_component = VelocityComponent(.1, .2)
    print(test_component)
    print(type(test_component))
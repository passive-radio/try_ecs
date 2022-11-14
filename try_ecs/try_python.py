from typing import Type
from typing import TypeVar

from ecs import component

class Test():
    def __init__(self) -> None:
        self.get_list: dict = {}
        
    def get_component(self):
        return self.get_list.setdefault((component.VelocityComponent, component.PositionComponent), [1,2])
if __name__ == "__main__":
    test_instance = Test()
    print(test_instance.get_component())
    for entity in test_instance.get_component():
        entity += 1
        print(entity)
    print(test_instance.get_component())
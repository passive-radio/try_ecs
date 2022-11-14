from ecs import processor

class MovementProcessor(processor.Processor):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def process(self, *args, **kwargs):
        
        for ent, vel, rend in self.world.get_components(Velocity, Renderable):
            rend.x += vel.x
            rend.y += vel.y
            
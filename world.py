import pybullet as p
class WORLD:
    def __init__(self):
        self.world = p.loadSDF("world.sdf")
        


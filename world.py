import pybullet as p
class WORLD:
    def __init__(self):
        #self.robotId = robotId
        #self.robotId = p.loadURDF(body)
        #self.robotId = p.loadURDF("body.urdf")
        #p.loadSDF("world.sdf")
        #self.world = p.loadSDF(world)
        self.world = p.loadSDF("world.sdf")
        #self.robotId = p.loadURDF("body.urdf")
        


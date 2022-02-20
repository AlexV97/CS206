from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.planeId = p.loadURDF("plane.urdf")
        #self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
        self.world = WORLD()
        self.robot = ROBOT()
        
    #def _init_(self, physicsclient, pybullet_data, setgravity):
        #self.world = WORLD()
        #self.robot = ROBOT()
        ##self.physicsClient = p.connect(p.GUI)
        ##self.physicsClient = p.connect(physicsclient)
        #self.physicsClient = p.connect(p.GUI)
        ##p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #self.setAdditionalSearchPath = setAdditionalSearchPath(pybullet_data.getDataPath())
        ##self.p.setGravity(0,0,-9.8)
        ##self.setGravity = setGravity(setgravity)
        #self.setGravity = setGravity(0,0,-9.8)
        ##pyrosim.Prepare_To_Simulate(robotId)
        #self.pyrosim.Prepare_To_Simulate(robotId)


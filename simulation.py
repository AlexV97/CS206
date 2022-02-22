from world import WORLD
from robot import ROBOT

import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        for i in range(c.indexRange):
           p.stepSimulation()
           self.robot.Sense(i)
           self.robot.Act(i)
           time.sleep(1/480);

            
    def __del__(self):
        p.disconnect()


from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR 

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
        
        #self.robot.Save_Values_Sensors()
            
    def __del__(self):
        p.disconnect()


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
        #print("simulation - constructor")
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        
    def Run(self):
        #print("simulation - Run()")
        for i in range(c.indexRange):
           #print("simulation - p.stepSimulation()")
           p.stepSimulation()
           #print("simulation - self.robot.Sense(i)")
           self.robot.Sense(i)
           #print("simulation - self.robot.Think()")
           self.robot.Think()
           #print("simulation - self.robot.Act()")
           self.robot.Act(i)
           time.sleep(1/480);
        
        self.robot.Save_Values_Sensors()
            
    def __del__(self):
        p.disconnect()


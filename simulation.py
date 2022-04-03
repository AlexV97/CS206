from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR 
from solution import SOLUTION

import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if ( self.directOrGUI == "DIRECT" ):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)
        
    def Run(self):
        print("simulation Run() - c.indexRange= ", c.indexRange, " - directOrGUI=", self.directOrGUI)
        for i in range(c.indexRange):
           #print("simulation Run() before p.stepSimulation() ")
           p.stepSimulation()
           #print("simulation Run() before self.robot.Sense(i) - i= ", i)
           self.robot.Sense(i)
           #print("simulation Run() before self.robot.Think() ")
           self.robot.Think()
           #print("simulation Run() before self.robot.Act(i) ")
           self.robot.Act(i)
           if ( self.directOrGUI == "GUI"):
                time.sleep(1/(2*480)); #time.sleep(1/480); #
  
        self.robot.Save_Values_Sensors()
        #print("simulation Run() robot.Save_Values_Sensors()")
    
    def Get_Fitness(self):
        print("simulation Get_Fitness() Starts - self.directOrGUI = ", self.directOrGUI , " - = self.solutionID", self.solutionID)
        self.robot.Get_Fitness()
        print("simulation Get_Fitness() Done")
            
    def __del__(self):
        p.disconnect()


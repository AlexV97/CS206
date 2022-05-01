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
        #print("simulation Run() Started - solutionID:", self.solutionID)
        for i in range(c.indexRange):
           p.stepSimulation()
           self.robot.Sense(i)
           self.robot.Think()
           self.robot.Act(i)
           
        self.robot.Save_Values_Sensors() # saving sensors in ../data for normal DIRECT operation
        if ( self.directOrGUI == "GUI"):
            self.robot.Save_Best_Values_Sensors() # saving best sensors results in ../data_quadruped for final GUI operation
        
        
    def Get_Fitness(self):
        self.robot.Get_Fitness()
            
    def __del__(self):
        p.disconnect()


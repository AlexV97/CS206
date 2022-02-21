import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #self.sensors = {
        #}
        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.motors = {
        }

        
    def Prepare_To_Sense(self):
        self.sensors = {
        }
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) # printing infinitely coordinates of BackLeg

    def Sense(self,i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)
            
    def Prepare_To_Act(self):
        self.motors = {
        }
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Act(self):
        for motor in self.motors.values():
            motor.Set_Value(i, self.robot)
            

      
        
        
    

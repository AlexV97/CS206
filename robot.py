import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.motors = {
        }
        amplitude=c.amplitude
        frequency = c.frequency
        phaseOffset = c.phaseOffset
        for motor in pyrosim.jointNamesToIndices:
            self.motors[motor] = MOTOR(motor)
            #motor.Prepare_To_Act(amplitude, frequency, phaseOffset) # motor.Prepare_To_Act(amplitude, frequency, phaseOffset) AttributeError: 'str' object has no attribute 'Prepare_To_Act'
            #self.motors[motor].Prepare_To_Act(amplitude, frequency, phaseOffset) # motor.Set_Value(i, self.robot) AttributeError: 'str' object has no attribute 'Set_Value'

        
    def Prepare_To_Sense(self):
        self.sensors = {
        }
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) # printing infinitely coordinates of BackLeg

    def Sense(self,i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Act(self,i):
        for motor in self.motors:
            print("robot - Act for loop ", i)
            #motor.Set_Value(i, self.robot) # motor.Set_Value(i, self.robot AttributeError: 'str' object has no attribute 'Set_Value'
            self.motors[motor].Set_Value(i, self)
        
            

      
        
        
    

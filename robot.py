import pybullet as p
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

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
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {
        }
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if (self.nn.Is_Motor_Neuron(neuronName)):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) #Step 67
                self.motors[jointName].Set_Value(desiredAngle, self)
        
    def Save_Values_Sensors(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0) # self.robot
        #print("Get_Fitness() -stateOfLinkZero =", stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print("Get_Fitness() -positionOfLinkZero =", positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print("Get_Fitness() -xCoordinateOfLinkZero =", xCoordinateOfLinkZero)
        f_write = open("fitness.txt", "w")
        f_write.write(str(xCoordinateOfLinkZero))
        f_write.close()
        exit()
        
        
    

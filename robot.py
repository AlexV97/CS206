import pybullet as p
import numpy
import constants as c
import os
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solution_ID):
        self.robotId = p.loadURDF("body.urdf")
        self.solutionId = solution_ID
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.motors = {
        }
        amplitude=c.amplitude
        frequency = c.frequency
        phaseOffset = c.phaseOffset
        for motor in pyrosim.jointNamesToIndices:
            self.motors[motor] = MOTOR(motor)
        brain_file = "brain"+str(self.solutionId)+".nndf"
        print("robot __init__() brain_file=", brain_file)
        self.nn = NEURAL_NETWORK(brain_file)
        #print("robot __init__() before delete")
        #os.system("ls brain*.nndf")
        os.system("rm "+brain_file)
        #print("robot __init__() after delete") ### delete is working fine on this specific file
        #os.system("ls brain*.nndf")

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
        print("robot Get_Fitness() - starts ")
        stateOfLinkZero = p.getLinkState(self.robotId,0) # self.robot
        #print("robot Get_Fitness() -stateOfLinkZero =", stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print("robot Get_Fitness() -positionOfLinkZero =", positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        #print("robot Get_Fitness() -xCoordinateOfLinkZero =", xCoordinateOfLinkZero)
        fitnessFileName = "fitness"+str(self.solutionId)+".txt"
        f_write = open(fitnessFileName, "w")
        f_write.write(str(xCoordinateOfLinkZero))
        f_write.close()
        print("robot Get_Fitness() - DONE - fitnessFileName= ", fitnessFileName, " - xCoordinateOfLinkZero=", xCoordinateOfLinkZero)
        exit()
        
        
    

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
        self.nn = NEURAL_NETWORK(brain_file)
        os.system("rm "+brain_file)

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
                self.motors[jointName].Set_Value((desiredAngle*c.motorJointRange), self)
        
    def Save_Values_Sensors(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
    def Get_Fitness(self):
        #print("robot Get_Fitness() - starts ")
        stateOfLinkZero = p.getLinkState(self.robotId,0) # self.robot
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = -1*(positionOfLinkZero[0]) 

        fitnessFileName = "tmp"+str(self.solutionId)+".txt"
        os_command_line = "mv " + "tmp"+str(self.solutionId)+".txt "
        os_command_line += " fitness"+str(self.solutionId)+".txt "
        os.system(os_command_line)

        f_write = open(fitnessFileName, "w")
        f_write.write(str(xCoordinateOfLinkZero))
        f_write.close()

        #print("robot Get_Fitness() - DONE - fitnessFileName= ", fitnessFileName, " - xCoordinateOfLinkZero=", xCoordinateOfLinkZero)
        #exit()
        
        
    

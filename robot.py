import pybullet as p
import numpy
import constants as c
import time
import os
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self, solution_ID):
        self.solutionId = solution_ID
        self.sensors = {}
        self.motors = {}
        brain_file = "brain"+str(self.solutionId)+".nndf"
        self.nn = NEURAL_NETWORK(brain_file)
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        os.system("rm "+brain_file)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}
        for joint_name in pyrosim.jointNamesToIndices:
            self.motors[joint_name] = MOTOR(joint_name,
                                            amplitude=c.amplitude,
                                            frequency=c.frequency,
                                            phaseOffset=c.phaseOffset)

    def Act(self,i):
        for neuronName in self.nn.Get_Neuron_Names():
            if (self.nn.Is_Motor_Neuron(neuronName)):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotId, (desiredAngle*c.motorJointRange))
        
    def Save_Values_Sensors(self):
        print("robot Save_Values_Sensors() - sensors.values()=", self.sensors.values())
        for sensor in self.sensors.values():
            sensor.Save_Values()
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()  # comment out when not in debug
        
    def Get_Fitness(self):
        print("robot Get_Fitness() - starts ")

        xCoordinateOfLinkZero = p.getLinkState(self.robotId, 0)[0][0]  # x_coord_of_link_0
        #print("robot Get_Fitness() - xCoordinateOfLinkZero= ", xCoordinateOfLinkZero)
        fitnessFileName = "tmp"+str(self.solutionId)+".txt"
        #os_command_line = "mv " + "tmp"+str(self.solutionId)+".txt "
        os_command_line = "cp " + "tmp"+str(self.solutionId)+".txt "
        os_command_line += " fitness"+str(self.solutionId)+".txt "
        os.system(os_command_line)

        f_write = open(fitnessFileName, "w")
        f_write.write(str(xCoordinateOfLinkZero))
        f_write.close()

        print("robot Get_Fitness() - DONE - xCoordinateOfLinkZero=", xCoordinateOfLinkZero)

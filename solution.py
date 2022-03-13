import math
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
class SOLUTION:
    def __init__(self):
        self.sensorNeurons=[0,1,2]
        self.motorNeurons=[3,4]
        self.weights = np.random.rand(3,2)
        self.weights = 2*(self.weights)-1
        self.l=1.0
        self.w=1.0
        self.h=1.0
        self.box1_x=0
        self.box1_y=0
        self.box1_z=(self.h)/2
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[(self.box1_x-2.0),(self.box1_y+2.0),self.box1_z] , size=[self.w,self.l,self.h])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[self.w,self.l,self.h])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
        type = "revolute", position = [1.0,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[self.w,self.l,self.h])
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
        type = "revolute", position = [2.0,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[self.w,self.l,self.h])

        pyrosim.End()

    def Generate_Brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

        for currentRow in self.sensorNeurons:
            for currentColumn in self.motorNeurons:  
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn , weight = self.weights[currentRow][currentColumn-3])
        
        pyrosim.End()
        
    def Evaluate(self):
        os.system("python3 simulate.py")
        
        f_read = open("fitness.txt", "r")
        self.fitness=float(f_read.read())
        print("solution - Evaluate() read fitness = ", self.fitness)
        f_read.close()

import math
import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
class SOLUTION:
    def __init__(self, myID_arg):
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
        self.myID = myID_arg

    def Create_World(self):
        print("solution - Create_World() Start ")
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[(self.box1_x-2.0),(self.box1_y+2.0),self.box1_z] , size=[self.w,self.l,self.h])
        pyrosim.End()

    def Generate_Body(self):
        print("solution - Generate_Body() Start ")
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[self.w,self.l,self.h])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
        type = "revolute", position = [1.0,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[self.w,self.l,self.h])
        
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
        type = "revolute", position = [2.0,0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[self.w,self.l,self.h])

        pyrosim.End()
        print("solution - Create_World() End ")

    def Generate_Brain(self): # Send_Brain() ?
        print("solution - Generate_Brain() Start ")
        brain_file_name = "brain"+str(self.myID)+".nndf"
        print("Generate_Brain brain_file_name=", brain_file_name)
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")

        for currentRow in self.sensorNeurons:
            for currentColumn in self.motorNeurons:
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn , weight = self.weights[currentRow][currentColumn-3]) #aligns weights with neuron values
        
        pyrosim.End()
        print("solution - Generate_Brain() End brain_file_name=", brain_file_name)
        
    def Evaluate(self, directOrGUI):
        print("solution - Evaluate() Start ")
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os_commandLine = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &"
        print("solution Evaluate() - os_commandLine= ", os_commandLine)
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        print("solution - Evaluate() fitnessFileName= ", fitnessFileName)
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        print("solution - Evaluate() DONE with while wait")
        f_read = open(fitnessFileName, "r")
        self.fitness=float(f_read.read())
        f_read.close()
        print("solution - Evaluate() DONE reading fitnessFileName= ", fitnessFileName)

    def Mutate(self):
        print("solution.py - Mutate()")
        randomRow=random.randint(0,2)       # 3 rows
        randomColumn=random.randint(0,1)    # 2 columns
        #print("solution.py - randomRow=", randomRow, " - randomColumn=", randomColumn)
        my_random=random.random()
        self.weights[randomRow,randomColumn] = (2*(my_random)-1)
    
    def Set_ID(self, myID_arg):
        self.myID = myID_arg

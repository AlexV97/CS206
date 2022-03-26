import math
import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import constants as c
class SOLUTION:
    def __init__(self, myID_arg):
        #self.sensorNeurons=[0,1,2]
        self.sensorNeurons=[0,1,c.numMotorNeurons]
        #self.motorNeurons=[3,4]
        self.motorNeurons=[c.numSensorNeurons,4]
        #self.weights = np.random.rand(3,2)
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = 2*(self.weights)-1
        self.l=1.0
        self.w=1.0
        self.h=1.0
        self.box1_x=0
        self.box1_y=0
        self.box1_z=(self.h)/2
        self.myID = myID_arg
        self.fitness = 0

    def Create_World(self):
        #print("solution - Create_World() Start ")
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[(self.box1_x-2.0),(self.box1_y+2.0),self.box1_z] , size=[self.w,self.l,self.h])
        pyrosim.End()

    def Generate_Body(self):
        #print("solution - Generate_Body() Start ")
        pyrosim.Start_URDF("body.urdf")
        #pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[self.w,self.l,self.h])
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[self.w,self.l,self.h])


        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
        #type = "revolute", position = [1.0,0,1.0])
        type = "revolute", position = [0,-0.5,1.0], jointAxis = "1 0 0")        ### position = [0,-0.5,1.0], jointAxis = "0 1 0")
        #pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[self.w,self.l,self.h])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
         
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
        #type = "revolute", position = [2.0,0,1.0])
        type = "revolute", position = [0,0.5,1.0], jointAxis = "1 0 0")         ### position = [0,0.5,1.0], jointAxis = "0 1 0"
        #pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[self.w,self.l,self.h])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])    ### pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" ,
        type = "revolute", position = [-0.5,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])    ### pos=[0,0.5,0] , size=[0.2,1,0.2])
        
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" ,
        type = "revolute", position = [0.5,0,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])    ### pos=[0,0.5,0] , size=[0.2,1,0.2])

        pyrosim.End()
        #print("solution - Create_World() End ")
        #exit()

    def Generate_Brain(self): # Send_Brain() ?
        #print("solution - Generate_Brain() Start ")
        brain_file_name = "brain"+str(self.myID)+".nndf"
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=c.numMotorNeurons, linkName="LeftLeg")
        #pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+1, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+2, jointName = "Torso_LeftLeg")

        for currentRow in self.sensorNeurons:
            for currentColumn in self.motorNeurons:
                #pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn , weight = self.weights[currentRow][currentColumn-3]) #aligns weights with neuron values
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn , weight = self.weights[currentRow][currentColumn-c.numSensorNeurons]) #aligns weights with neuron values
        
        pyrosim.End()
        #exit()
   
    def Start_Simulation(self, directOrGUI, lastSimul):
        print("solution - Start_Simulation() Start ID= ", str(self.myID), " - fitness= ", str(self.fitness))
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        if ( lastSimul == 1):  # for last simulation, do not let command line continuing/waiting
            #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) )
            #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 ")
            os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2>nul ")
        else:
            #works#os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
            #os.system("python3 simulate.py GUI 0 2&>1 &")
            #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
            os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2>nul &")

        print("solution - Start_Simulation() Completed - Start ID= ", str(self.myID), " - fitness= ", str(self.fitness))


    def Wait_For_Simulation_To_End(self, directOrGUI):
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f_read = open(fitnessFileName, "r")
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        self.fitness=float(f_read.read())
        f_read.close()
        os.system("rm "+fitnessFileName)
        #print("solution - Wait_For_Simulation_To_End() DONE reading fitnessFileName= ", fitnessFileName, " - fitness= ", self.fitness)
        
    def Mutate(self):
        #print("solution.py - Mutate()")
        randomRow=random.randint(0,2)       # 3 rows
        randomColumn=random.randint(0,1)    # 2 columns
        my_random=random.random()
        self.weights[randomRow,randomColumn] = (2*(my_random)-1)
    
    def Set_ID(self, myID_arg):
        self.myID = myID_arg

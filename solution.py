import math
import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import constants as c
class SOLUTION:
    def __init__(self, myID_arg):
        self.sensorNeurons=[0,1,2,3,4,5,6,7,8,9,10,11,c.numSensorNeurons-1]
        self.motorNeurons=[c.numSensorNeurons, c.numSensorNeurons+1, c.numSensorNeurons+2,c.numSensorNeurons+3, c.numSensorNeurons+4,c.numSensorNeurons+5,c.numSensorNeurons+6,c.numSensorNeurons+7, c.numSensorNeurons+8,c.numSensorNeurons+9,c.numSensorNeurons+10,c.numSensorNeurons+11]
        self.weights = 2*(np.random.rand(c.numSensorNeurons,c.numMotorNeurons))-1
        self.l=1.0
        self.w=1.0
        self.h=1.0
        self.box1_x=0
        self.box1_y=0
        self.box1_z=(self.h)/2
        self.myID = myID_arg
        self.fitness = 0
        self.myCurrentGeneration = 0

    def Create_World(self):
        #print("solution - Create_World() Start ")
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[(self.box1_x-2.0),(self.box1_y+2.0),self.box1_z] , size=[self.w,self.l,self.h])
        pyrosim.End()

    def Generate_Body(self):
        #print("solution - Generate_Body() Start ")
        pyrosim.Start_URDF("body.urdf")
        
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[self.w,self.l,self.h])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2]) 
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.25,0] , size=[1,0.15,0.15])
        pyrosim.Send_Cube(name="SecondLeftLeg", pos=[-0.5,-0.25,0] , size=[1,0.15,0.15])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.25,0] , size=[1,0.15,0.15])
        pyrosim.Send_Cube(name="SecondRightLeg", pos=[0.5,-0.25,0] , size=[1,0.15,0.15])
        
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0.25,-0.5] , size=[0.15,0.15,1])
        pyrosim.Send_Cube(name="SecondLeftLowerLeg", pos=[0,-0.25,-0.5] , size=[0.15,0.15,1])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0.25,-0.5] , size=[0.15,0.15,1])
        pyrosim.Send_Cube(name="SecondRightLowerLeg", pos=[0,-0.25,-0.5] , size=[0.15,0.15,1])
         
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
        type = "revolute", position = [0,-0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
        type = "revolute", position = [0,0.5,1.0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" ,
        type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_SecondLeftLeg" , parent= "Torso" , child = "SecondLeftLeg" ,
        type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" ,
        type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "Torso_SecondRightLeg" , parent= "Torso" , child = "SecondRightLeg" ,
        type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        
        
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" ,
        type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" ,
        type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" ,
        type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "SecondLeftLeg_SecondLeftLowerLeg" , parent= "SecondLeftLeg" , child = "SecondLeftLowerLeg" ,
        type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" ,
        type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name = "SecondRightLeg_SecondRightLowerLeg" , parent= "SecondRightLeg" , child = "SecondRightLowerLeg" ,
        type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
   
        pyrosim.End()


    def Generate_Brain(self): 
        brain_file_name = "brain"+str(self.myID)+".nndf"
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="SecondLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="SecondRightLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="SecondLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=(c.numSensorNeurons-1), linkName="SecondRightLowerLeg")
        
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+1, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+2, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+3, jointName = "Torso_SecondLeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+4, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+5, jointName = "Torso_SecondRightLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+6, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+7, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+8, jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+9, jointName = "SecondLeftLeg_SecondLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+10, jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+11, jointName = "SecondRightLeg_SecondRightLowerLeg")
        
        for currentRow in self.sensorNeurons:
            for currentColumn in self.motorNeurons:
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn , weight = self.weights[currentRow][currentColumn-c.numSensorNeurons-1]) #aligns weights with neuron values
        
        pyrosim.End()
   
    def Start_Simulation(self, directOrGUI, lastSimul):
        print("solution - Start_Simulation() Start ID= ", str(self.myID), " - directOrGUI= ", directOrGUI, " - lastSimul= ", lastSimul )
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        if ( lastSimul == 1):  # for last simulation, do not let command line continuing/waiting
            #os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2>nul ")
            os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID))
            #time.sleep(180)
            #os.system("sleep 180 ")
            #print("solution - after last lastSimul " )
        else:
            os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " & 2>nul ")

        #print("solution - Start_Simulation() Completed - Start ID= ", str(self.myID), " - fitness= ", str(self.fitness))


    def Wait_For_Simulation_To_End(self, directOrGUI):
        #print("solution - Wait_For_Simulation_To_End() directOrGUI= ", directOrGUI)
        fitnessFileName = "fitness"+str(self.myID)+".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f_read = open(fitnessFileName, "r")
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        self.fitness=float(f_read.read())
        f_read.close()
        os.system("rm "+fitnessFileName+ " 2>nul ")#new
        
    def Mutate(self):  #
        randomRow=random.randint(0,c.numSensorNeurons-1)
        randomColumn=random.randint(0,c.numMotorNeurons-1)
        my_random=random.random()
        self.weights[randomRow,randomColumn] = (2*(my_random)-1)
    
    def Set_ID(self, myID_arg):
        self.myID = myID_arg

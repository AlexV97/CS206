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
#        print("ROBOT constructor - dict self.sensors=", self.sensors)
#        print("ROBOT constructor - dict self.motors=", self.motors)
#        print("ROBOT constructor - dict self.nn.neurons=", self.nn.neurons)
#        print("ROBOT constructor - dict self.nn.synapses=", self.nn.synapses)
        
    def Prepare_To_Sense(self):
        self.sensors = {
        }
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self,i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Act(self,i):
#ok#        print("robot Act - robotId=", self.robotId)
#ok#        print("robot Act - sensors=", self.sensors)
#        print("robot Act - motors=", self.motors)
#        print("robot Act - self.nn.Print()()=", self.nn.Print()) #not ok: self.nn.Print()()= None
#        print("robot Act - self.nn.Get_Neuron_Names()=", self.nn.Get_Neuron_Names())
        for neuronName in self.nn.Get_Neuron_Names():
            ##print("Act - current neuronName=", neuronName)#, self.nn.Get_Name())
            if (self.nn.Is_Motor_Neuron(neuronName)):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) #Step 67
                #self.nn.Get_Motor_Neurons_Joint(jointName).Set_Value(desiredAngle, self)
                #self.motors[motor].Set_Value(desiredAngle, self) ## NameError: name 'motor' is not defined
                self.motors[jointName].Set_Value(desiredAngle, self)
                #print("Act - current Motor neuronName=", neuronName, " - jointName=", jointName, " is a neuron", " - desiredAngle =", desiredAngle)
                
            #for motor in self.motors:
            #    self.motors[motor].Set_Value(i, self)
        
    def Save_Values_Sensors(self):
        for sensor in self.sensors.values():
            sensor.Save_Values()
            
    def Think(self):
        #print("robot - Think():")
        self.nn.Update()
        self.nn.Print()
        
    

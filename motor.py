import numpy
import constants as c
import pybullet as p
import math
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.indexRange)
        self.Prepare_To_Act(c.amplitude, c.frequency, c.phaseOffset)
        
    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset    = c.phaseOffset

        for i in range(c.indexRange):
            self.motorValues[i] = numpy.sin(math.pi/4)*numpy.sin(((i*2*self.frequency*math.pi/(c.indexRange))+self.offset))
        print("Prepare_To_Act self.motorValues=", self.motorValues)

    def Set_Value(self,i, currentrobot):
        print("motor - Set_Value i=", i, " - currentrobot =", currentrobot)
        self.motorValues[i] = numpy.sin(math.pi/4)*numpy.sin(((i*2*self.frequency*math.pi/(c.indexRange))+self.offset))

        self.motorValues[i] = pyrosim.Set_Motor_For_Joint(
            bodyIndex = currentrobot.robotId,  #robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.amplitude * self.motorValues[i],
            maxForce = 80)


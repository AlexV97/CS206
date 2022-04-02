import numpy
import constants as c
import pybullet as p
import math
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self,
                jointName,
                amplitude,
                frequency,
                phaseOffset):
        self.jointName = jointName
        self.amplitude = amplitude
        self.frequency = frequency
        self.phaseOffset = phaseOffset
        self.motorValues = (amplitude * numpy.sin(frequency)*numpy.linspace(0, 2*numpy.pi, c.indexRange)+self.phaseOffset)
        #self.motorValues = numpy.zeros(c.indexRange)
        #self.Prepare_To_Act()

    def Set_Value(self, robot_id, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot_id,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.MAX_JOINT_FORCE)


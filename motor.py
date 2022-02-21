class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.indexRange)
        Prepare_To_Act()
        
    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitude = c.amplitude #= amplitude
        self.frequency = c.frequency #= frequency
        self.offset    = c.offset #= offset
   

    def Set_Value(self,i, currentrobot):
        #pass
        self.motorValues[i] = numpy.sin(math.pi/4)*numpy.sin(((i*2*c.frequency_BackLeg*math.pi/(c.indexRange))+c.phaseOffset_BackLeg))

        self.values[i] = pyrosim.Set_Motor_For_Joint(
            bodyIndex = currentrobot,  #robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.amplitude * targetAngles_FrontLeg[i],
            maxForce = 80)
        #
        #if i==(c.indexRange-1):
        #    print("i=",i," - sensor ", self.linkName, "- values = ", self.values)

        

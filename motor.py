class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.indexRange)
        Prepare_To_Act()
        
    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitude = c.amplitude #= amplitude
        self.frequency = c.frequency #= frequency
        self.offset    = c.offset #= offset
   

    def Set_Value(self,i):
        pass
        #self.values[i] = pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotId,  #robot,
        #jointName = self,
        #controlMode = p.POSITION_CONTROL,
        #targetPosition = self.amplitude * targetAngles_FrontLeg[i],
        #maxForce = 80)
        #
        #if i==(c.indexRange-1):
        #    print("i=",i," - sensor ", self.linkName, "- values = ", self.values)

        

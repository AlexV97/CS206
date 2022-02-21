class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.indexRange)
        Prepare_To_Act()
        
    def Prepare_To_Act(self, amplitude, frequency, offset):
        #targetAngles_BackLeg=numpy.zeros(c.indexRange)
        #targetAngles_FrontLeg=numpy.zeros(c.indexRange)
        self.amplitude = c.amplitude #= amplitude
        self.frequency = c.frequency #= frequency
        self.offset    = c.offset #= offset
        
        

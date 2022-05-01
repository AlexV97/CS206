import math
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
        if ( self.linkName != 'NoneType'):
            if ( ( self.linkName == 'RightLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+1*c.phaseOffset+c.phaseOffset/2)#
            elif ( ( self.linkName == 'RightLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+1*c.phaseOffset)+0.11*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'LeftLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset+c.phaseOffset/2)#
            elif ( ( self.linkName == 'LeftLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset)+0.11*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'BackLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2*c.phaseOffset+c.phaseOffset/2)#
            elif ( ( self.linkName == 'BackLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2*c.phaseOffset)+0.11*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'FrontLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+4*c.phaseOffset+c.phaseOffset/2)#
            elif ( ( self.linkName == 'FrontLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+4*c.phaseOffset)+0.11*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            else:
                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("../data/"+str(self.linkName)+"sensor.npy", self.values)
        
    def Save_Best_Values(self):
        numpy.save("../data_quadruped/"+str(self.linkName)+"sensor.npy", self.values)
        
    def __del__(self):
        self.Save_Values()
    

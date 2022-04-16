import math
import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
 #       print("sensor.py Get_Value() - self.linkName = ", self.linkName)
 #       if ( self.linkName != 'NoneType'):
 #           if ( ( self.linkName == 'FrontLeg') or ( self.linkName == 'BackLeg') ):
 #               self.values[i] = numpy.sin(i*c.marchingFreq)
 #           if ( ( self.linkName == 'FrontLeg') ):
 #               self.values[i] = numpy.sin(i*c.marchingFreq+c.phaseOffset)
 #           if ( ( self.linkName == 'BackLeg') ):
 #               self.values[i] = numpy.sin(i*c.marchingFreq)
 #           if ( ( self.linkName == 'FrontLeg') ):
### not too bad - cross between marching and jumping
###             if ( ( self.linkName == 'RightLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'LeftLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq-c.phaseOffset/2)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
####            elif ( ( self.linkName == 'BackLowerLeg') ):
####                self.values[i] = numpy.sin(i*c.marchingFreq-c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
####            elif ( ( self.linkName == 'FrontLowerLeg') ):
####                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            else:
###                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
## not too bad too - more jumping
##            if ( ( self.linkName == 'RightLowerLeg') ):
##                self.values[i] = numpy.sin(i*c.marchingFreq+c.phaseOffset/4)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
##            elif ( ( self.linkName == 'LeftLowerLeg') ):
##                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
##            elif ( ( self.linkName == 'BackLowerLeg') ):
##                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
##            elif ( ( self.linkName == 'FrontLowerLeg') ):
##                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset/4)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
##            else:
##                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
#            if ( ( self.linkName == 'RightLowerLeg') ):
#                self.values[i] = numpy.sin(i*c.marchingFreq/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
#            elif ( ( self.linkName == 'LeftLowerLeg') ):
#                self.values[i] = numpy.sin(i*c.marchingFreq/2+3*c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
#            elif ( ( self.linkName == 'BackLowerLeg') ):
#                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset/4)+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
#            elif ( ( self.linkName == 'FrontLowerLeg') ):
#                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset/4)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
### Prof recommended lower and upper of the legs
###        if ( self.linkName != 'NoneType'):
###            if ( ( self.linkName == 'RightLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'RightLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'LeftLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'LeftLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'BackLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'BackLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'FrontLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            elif ( ( self.linkName == 'FrontLowerLeg') ):
###                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
###            else:
###                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if ( self.linkName != 'NoneType'):
            if ( ( self.linkName == 'RightLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+1*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'RightLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+1*c.phaseOffset)+0.13*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'LeftLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'LeftLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+3*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'BackLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'BackLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'FrontLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+4*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'FrontLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+4*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            else:
                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("data/"+str(self.linkName)+"sensor.npy", self.values)
        
    def __del__(self):
        self.Save_Values()
    

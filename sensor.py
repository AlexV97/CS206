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
                self.values[i] = numpy.sin(i*c.marchingFreq*2+0.5*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'RightLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+0.5*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            if ( ( self.linkName == 'SecondRightLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+1.5*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'SecondRightLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+1.5*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'LeftLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+3.5*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'LeftLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+3.5*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'SecondLeftLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2.5*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'SecondLeftLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq*2+2.5*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'BackLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'BackLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+2*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'FrontLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset+c.phaseOffset/2)#+pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            elif ( ( self.linkName == 'FrontLowerLeg') ):
                self.values[i] = numpy.sin(i*c.marchingFreq+4*c.phaseOffset)+0.1*pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
            else:
                self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
                

    def Save_Values(self):
        #print("sensor Save_Values() started - self.linkName= ", self.linkName)
        numpy.save("../data/"+str(self.linkName)+"sensor.npy", self.values)
        #print("sensor Save_Values() ended - self.values= ", self.values)
        
    def Save_Best_Values(self):
        print("sensor Save_Best_Values() started - self.linkName= ", self.linkName)
        numpy.save("../data_hexapod/"+str(self.linkName)+"sensor.npy", self.values)
        print("sensor Save_Best_Values() ended - self.values= ", self.values)
        
    def __del__(self):
        self.Save_Values()
    

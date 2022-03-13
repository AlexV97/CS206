import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
        print("sensor.py Get_Value() - self.linkName = ", self.linkName)
        if ( self.linkName != 'NoneType'):
            self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save("data/"+str(self.linkName)+"sensor.npy", self.values)
        
    def __del__(self):
        self.Save_Values()
    

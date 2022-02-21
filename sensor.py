import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)  # instruction 65 refers of our index i as t for current time
        if i==(c.indexRange-1):
            print("i=",i," - sensor ", self.linkName, "- values = ", self.values)
        

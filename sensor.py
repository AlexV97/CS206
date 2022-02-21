import numpy
import constants as c

class SENSOR:
    def __init__(self, linkName):
        print("SENSOR __init__ - linkName=", linkName)
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)
        print("SENSOR self.values = ", self.values)

    def Get_Value(self):
        print("SENSOR - Get_Value - self", self.values)

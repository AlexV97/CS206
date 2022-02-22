import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.indexRange)

    def Get_Value(self,i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)  

    def Save_Values(self):
        #file_name = "../data/sensorValues_"
        #file_name += self.linkName
        #file_name += ".npy"
        #print('SENSOR Save_Values to file: ', file_name)
        #with open('../data/targetAngles_BackLegValues.npy','wb') as outputSensorValues_file:
        with open(file_name,'wb') as outputSensorValues_file:
            numpy.save(outputSensorValues_file, self.values)
        outputSensorValues_file.close()
        
        
    

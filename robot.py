import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #self.sensors = {
        #    #"sensor1" : "BackLeg",
        #    #"sensor2" : "FrontLeg"
        #}
        self.robotId = p.loadURDF("body.urdf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.motors = {
        
        }

        
    def Prepare_To_Sense(self):
        self.sensors = {
        
        }
        for linkName in pyrosim.linkNamesToIndices:
            print("ROBOT - Prepare_To_Sense for loop - linkName =", linkName)
            self.sensors[linkName] = SENSOR(linkName)
            #print(linkName)

    def Sense(self):
        #    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        #self.BackLeg.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        pass
        
    

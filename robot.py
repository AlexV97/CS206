import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

from sensor import SENSOR

class ROBOT:
    def __init__(self):
        #self.sensors = {
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
            #print("ROBOT - Prepare_To_Sense for loop - linkName =", linkName) # called only 3x with BackLeg, Torso, FrontLeg
            self.sensors[linkName] = SENSOR(linkName) # printing infinitely coordinates of BackLeg
        
        #print("Dictionary self.sensors = ")
        #for x,y in self.sensors.items():
        #    print(x,y)

    def Sense(self,i):
        #backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        for sensor in self.sensors.values():
            #sensor.Get_Value(i)
            #print("ROBOT Sense for sensor = ", sensor, " - i=", i)
            #self.values[i] = sensor.Get_Value(i)
            sensor.Get_Value(i)
            
            
        
        
    

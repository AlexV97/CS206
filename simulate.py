import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

from pathlib import Path

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

Path.cwd()

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues=numpy.zeros(100)
frontLegSensorValues=numpy.zeros(100)

for i in range(100):
    p.stepSimulation();
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60);

print("final backLegSensorValues=")
print(backLegSensorValues)

print("final frontLegSensorValues=")
print(frontLegSensorValues)

with open('../data/backLegSensorValues.npy','wb') as backleg_output_file:
    numpy.save(backleg_output_file,backLegSensorValues)
    
with open('../data/frontLegSensorValues.npy','wb') as frontleg_output_file:
    numpy.save(frontleg_output_file,frontLegSensorValues)

p.disconnect

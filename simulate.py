import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

from pathlib import Path

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


Path.cwd()

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues=numpy.zeros(1600)
frontLegSensorValues=numpy.zeros(1600)

for i in range(1600):
    positionRange=(random.random()*random.random()*math.pi)/2.0
    p.stepSimulation();
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,  #robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = -(positionRange),
    maxForce = 80)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,  #robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = (positionRange),
    maxForce = 80)
    time.sleep(1/480);

print("final backLegSensorValues=")
print(backLegSensorValues)

print("final frontLegSensorValues=")
print(frontLegSensorValues)

with open('../data/backLegSensorValues.npy','wb') as backleg_output_file:
    numpy.save(backleg_output_file,backLegSensorValues)
    
with open('../data/frontLegSensorValues.npy','wb') as frontleg_output_file:
    numpy.save(frontleg_output_file,frontLegSensorValues)

p.disconnect

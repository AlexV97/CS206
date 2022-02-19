import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

from pathlib import Path
amplitude_BackLeg = (math.pi)/2
frequency_BackLeg  = 10
phaseOffset_BackLeg  = 0
amplitude_FrontLeg  = (math.pi)/4
frequency_FrontLeg = 10
phaseOffset_FrontLeg = (math.pi)/4
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")


Path.cwd()

pyrosim.Prepare_To_Simulate(robotId)

indexRange=1000

backLegSensorValues=numpy.zeros(indexRange)
frontLegSensorValues=numpy.zeros(indexRange)
targetAngles_BackLeg=numpy.zeros(indexRange)
targetAngles_FrontLeg=numpy.zeros(indexRange)

for i in range(indexRange):
    targetAngles_BackLeg[i]=numpy.sin(math.pi/4)*numpy.sin(((i*2*frequency_BackLeg*math.pi/(indexRange))+phaseOffset_BackLeg))
    targetAngles_FrontLeg[i]=numpy.sin(math.pi/4)*numpy.sin(((i*2*frequency_FrontLeg*math.pi/(indexRange))+phaseOffset_FrontLeg))
    p.stepSimulation();
    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,  #robot,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,

    targetPosition = amplitude_BackLeg * targetAngles_BackLeg[i],
    maxForce = 80)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,  #robot,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,

    targetPosition = amplitude_FrontLeg * targetAngles_FrontLeg[i],
    maxForce = 80)
    time.sleep(1/480);

print("final backLegSensorValues=")
print(backLegSensorValues)

print("final frontLegSensorValues=")
print(frontLegSensorValues)


p.disconnect

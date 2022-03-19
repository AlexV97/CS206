from simulation import SIMULATION

import constants as c
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import sys

from pathlib import Path

#print("simulate.py number of arguments: ", len(sys.argv), " arguments")

if ( len(sys.argv) == 3 ):
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
    print("*** simulate - arguments passed directOrGUI=",directOrGUI, " - solutionID=", solutionID)
else:
    directOrGUI = 'DIRECT'
    solutionID = 0 
    print("*** simulate - no arguments passed to directOrGUI and solutionID so assuming for now DIRECT and 0")

simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()

#print("simulate.py: after simulation.Run()")
simulation.Get_Fitness()
#print("simulate.py: Simulation Completed ")
#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.setGravity(0,0,-9.8)
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
#
#
#Path.cwd()
#
#pyrosim.Prepare_To_Simulate(robotId)
#
#backLegSensorValues=numpy.zeros(c.indexRange)
#frontLegSensorValues=numpy.zeros(c.indexRange)
#targetAngles_BackLeg=numpy.zeros(c.indexRange)
#targetAngles_FrontLeg=numpy.zeros(c.indexRange)
#
#for i in range(c.indexRange):
#    targetAngles_BackLeg[i]=numpy.sin(math.pi/4)*numpy.sin(((i*2*c.frequency_BackLeg*math.pi/(c.indexRange))+c.phaseOffset_BackLeg))
#    targetAngles_FrontLeg[i]=numpy.sin(math.pi/4)*numpy.sin(((i*2*c.frequency_FrontLeg*math.pi/(c.indexRange))+c.phaseOffset_FrontLeg))
#    p.stepSimulation();
#    backLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#    frontLegSensorValues[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#    pyrosim.Set_Motor_For_Joint(
#    bodyIndex = robotId,  #robot,
#    jointName = "Torso_BackLeg",
#    controlMode = p.POSITION_CONTROL,
#    targetPosition = c.amplitude_BackLeg * targetAngles_BackLeg[i],
#    maxForce = 80)
#    pyrosim.Set_Motor_For_Joint(
#    bodyIndex = robotId,  #robot,
#    jointName = "Torso_FrontLeg",
#    controlMode = p.POSITION_CONTROL,
#    targetPosition = c.amplitude_FrontLeg * targetAngles_FrontLeg[i],
#    maxForce = 80)
#    time.sleep(1/480);
#
#print("final backLegSensorValues=")
#print(backLegSensorValues)
#
#print("final frontLegSensorValues=")
#print(frontLegSensorValues)
#
#
def __del__(self):
    p.disconnect()
#


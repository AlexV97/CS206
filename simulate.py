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

print("simulate.py number of arguments: ", len(sys.argv), " arguments")

if ( len(sys.argv) == 3 ):
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
    print("*** simulate - arguments passed directOrGUI=",directOrGUI, " - solutionID=", solutionID)
else:
    directOrGUI = 'DIRECT'
    solutionID = 0
    print("*** simulate - no arguments passed to directOrGUI and solutionID so assuming for now DIRECT and 0")

print("simulate.py: before SIMULATION(directOrGUI, solutionID)")
simulation = SIMULATION(directOrGUI, solutionID)
print("simulate.py: before simulation.Run()")
simulation.Run()
print("simulate.py: after simulation.Run()")
simulation.Get_Fitness()
print("simulate.py: Simulation Completed ")

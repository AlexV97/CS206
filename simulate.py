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

if ( len(sys.argv) == 3 ):
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]

else:
    directOrGUI = 'DIRECT'
    solutionID = 0


simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
#print("simulate.py: Simulation Completed ")

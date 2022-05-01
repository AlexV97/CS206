import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import parallelHillClimber as phc

#os.system("date ")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

#os.system("date ")


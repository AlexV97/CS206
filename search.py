import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import parallelHillClimber as phc

#os.system("date ")

phc = PARALLEL_HILL_CLIMBER()

#print("search.py just before phc.Evolve()")
phc.Evolve()
#print("search.py just before phc.Show_Best()")
phc.Show_Best()

#os.system("date ")


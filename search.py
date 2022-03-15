import os
from hillclimber import HILL_CLIMBER
import hillclimber as hc
hc = HILL_CLIMBER()

#print("search.py just before hc.Evolve()")
hc.Evolve()
#print("search.py after hc.Evolve()")
#for loop_call in range(5):
#    os.system("python3 generate.py")
#    os.system("python3 simulate.py")



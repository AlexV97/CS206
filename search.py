import os
from datetime import datetime
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import parallelHillClimber as phc

#os.system("date ")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

currentDateTime = datetime.now()
currentDateTime = str(currentDateTime)
currentDateTime = currentDateTime.replace(":","")
currentDateTime = currentDateTime.replace(".","")
currentDateTime = currentDateTime.replace(" ","")
currentDateTime = currentDateTime.replace("-","")
print("search.py about to copy ../data_quadruped into../data_quadruped_", currentDateTime)
os_command_line = "cp -R ../data_quadruped ../data_quadruped_" + currentDateTime
os.system(os_command_line)
#os.system("date ")


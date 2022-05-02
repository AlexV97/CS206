import os
from datetime import datetime
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import parallelHillClimber as phc

os.system("date > ../data_hexapod/Search_py_startTime.txt")

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
phc.Show_Best()

currentDateTime = datetime.now()
currentDateTime = str(currentDateTime)
currentDateTime = currentDateTime.replace(":","")
currentDateTime = currentDateTime.replace(".","")
currentDateTime = currentDateTime.replace(" ","")
currentDateTime = currentDateTime.replace("-","")
print("search.py about to copy ../data_hexapod into../data_hexapod_", currentDateTime)
os_command_line = "cp -R ../data_hexapod ../data_hexapod_" + currentDateTime
os.system(os_command_line)

#os.system("date ")



import math

# number of steps in simulation
indexRange          = 30000 #8000
# if common parameters for both legs
amplitude           = (math.pi)/4
frequency           = 10
phaseOffset         = (math.pi)/4
numberOfGenerations = 10
populationSize      = 10
numSensorNeurons    = 9    #4 #3
numMotorNeurons     = 8     #3 #2
motorJointRange     = 0.25#0.2 # 0.4 #0.33 #
MAX_JOINT_FORCE     = 80
marchingFreq        = frequency * 2
 

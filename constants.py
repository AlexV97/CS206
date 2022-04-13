import math

# number of steps in simulation
indexRange          = 40000#400000#30000 #8000
indexRange_GUI      = 4000000#400000#30000 #8000
# if common parameters for both legs
amplitude           = (math.pi)/4
frequency           = 20#10
phaseOffset         = (math.pi)/4
numberOfGenerations = 6#1
populationSize      = 6#1
numSensorNeurons    = 9    #4 #3
numMotorNeurons     = 8     #3 #2
motorJointRange     = 0.25#0.2 # 0.4 #0.33 #
MAX_JOINT_FORCE     = 80
marchingFreq        = frequency * 2
 

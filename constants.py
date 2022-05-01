import math

# number of steps in simulation
indexRange          = 10000#30000#8000#8000#7000#400000#30000 #8000
indexRange_GUI      = 10000#30000#8000#2000000000#80000000#400000#30000 #8000
# if common parameters for both legs
amplitude           = (math.pi)/4
frequency           = 15# 20 # #5#10#2
phaseOffset         = frequency/4#frequency/2#frequency/2#frequency/4#(math.pi)/4
numberOfGenerations = 20#10#10#16#1
populationSize      = 10#1
numSensorNeurons    = 9    #4 #3
numMotorNeurons     = 8     #3 #2
motorJointRange     = 0.25 #0.2 # 0.4 #0.33 #
MAX_JOINT_FORCE     = 80
marchingFreq        = frequency #* 2 #frequency
 

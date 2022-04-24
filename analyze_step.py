import numpy
import numpy.matlib
import matplotlib.pyplot
import matplotlib.figure
import matplotlib.markers

ones = numpy.matlib.ones(1)

with open('../data_quadruped/BackLowerLegsensor.npy','rb') as BackLowerLegsensor_input_file:
     BackLowerLegsensorValues = numpy.load(BackLowerLegsensor_input_file)

with open('../data_quadruped/FrontLowerLegsensor.npy','rb') as FrontLowerLegsensor_input_file:
     FrontLowerLegsensorValues = numpy.load(FrontLowerLegsensor_input_file)

with open('../data_quadruped/LeftLowerLegsensor.npy','rb') as LeftLowerLegsensor_input_file:
     LeftLowerLegsensorValues = numpy.load(LeftLowerLegsensor_input_file)

with open('../data_quadruped/RightLowerLegsensor.npy','rb') as RightLowerLegsensor_input_file:
     RightLowerLegsensorValues = numpy.load(RightLowerLegsensor_input_file)

BackLowerLeg_touch = numpy.greater_equal(BackLowerLegsensorValues, ones)
#print("analyze BackLowerLeg_touch= ",BackLowerLeg_touch )

FrontLowerLeg_touch = numpy.greater_equal(FrontLowerLegsensorValues, ones)
#print("analyze FrontLowerLeg_touch= ",FrontLowerLeg_touch )

LeftLowerLeg_touch = numpy.greater_equal(LeftLowerLegsensorValues, ones)
#print("analyze BackLowerLeg_touch= ",LeftLowerLeg_touch )

RightLowerLeg_touch = numpy.greater_equal(RightLowerLegsensorValues, ones)
#print("analyze BackLowerLeg_touch= ",RightLowerLeg_touch )

xor_backLower_frontLower = numpy.logical_xor(BackLowerLeg_touch,FrontLowerLeg_touch)
xor_leftLower_rightLower = numpy.logical_xor(LeftLowerLeg_touch,RightLowerLeg_touch)

xor_allLegs = numpy.logical_xor(xor_backLower_frontLower,xor_leftLower_rightLower)


#i_BackLowerLeg_touch  = BackLowerLeg_touch * 1
#i_FrontLowerLeg_touch = FrontLowerLeg_touch * 2
#i_LeftLowerLeg_touch  = LeftLowerLeg_touch * 4
#i_RightLowerLeg_touch = RightLowerLeg_touch * 8
#i_TotalAllLegs = i_BackLowerLeg_touch + i_FrontLowerLeg_touch + i_LeftLowerLeg_touch + i_RightLowerLeg_touch
#print(" analyze i_TotalAllLegs=", i_TotalAllLegs)


matplotlib.pyplot.plot((BackLowerLegsensorValues>0.999), label='BackLowerLegTouch', ls='', marker="o")
matplotlib.pyplot.plot((FrontLowerLegsensorValues>0.999)*2, label='FrontLowerLegTouch', ls='', marker="o")
matplotlib.pyplot.plot((LeftLowerLegsensorValues>0.999)*3, label='LeftLowerLegsensorTouch', ls='', marker="o")
matplotlib.pyplot.plot((RightLowerLegsensorValues>0.999)*4, label='RightLowerLegsensorTouch', ls='', marker="o")

#matplotlib.pyplot.plot((BackLowerLegsensorValues), label='BackLowerLegTouch', ls='', marker="o")
#matplotlib.pyplot.plot((FrontLowerLegsensorValues), label='FrontLowerLegTouch', ls='', marker="o")
#matplotlib.pyplot.plot((LeftLowerLegsensorValues), label='LeftLowerLegsensorTouch', ls='', marker="o")
#matplotlib.pyplot.plot((RightLowerLegsensorValues), label='RightLowerLegsensorTouch', ls='', marker="o")

# Plot
matplotlib.pyplot.plot()

# Adjusting limits to ignore 0s of when the legs are not touching anything
matplotlib.pyplot.ylim(0.5,4.5)

# Adding title
matplotlib.pyplot.title("Project A: Marching Quadrupede \n LowerLegsSensors Touching Ground")

# Adding legend
matplotlib.pyplot.legend()

# Adding Axis Labels
matplotlib.pyplot.xlabel("Foot Steps per Leg for each iteration i")
matplotlib.pyplot.ylabel("Separating Lower Leg Touching per line")

# Auto adjust layout
matplotlib.pyplot.tight_layout()

# Display
matplotlib.pyplot.show()

import numpy
import numpy.matlib
import matplotlib.pyplot
import matplotlib.figure
import matplotlib.markers

ones = numpy.matlib.ones(1)

with open('../data_hexapod/BackLowerLegsensor.npy','rb') as BackLowerLegsensor_input_file:
     BackLowerLegsensorValues = numpy.load(BackLowerLegsensor_input_file)

with open('../data_hexapod/FrontLowerLegsensor.npy','rb') as FrontLowerLegsensor_input_file:
     FrontLowerLegsensorValues = numpy.load(FrontLowerLegsensor_input_file)

with open('../data_hexapod/LeftLowerLegsensor.npy','rb') as LeftLowerLegsensor_input_file:
     LeftLowerLegsensorValues = numpy.load(LeftLowerLegsensor_input_file)
     
with open('../data_hexapod/SecondLeftLowerLegsensor.npy','rb') as SecondLeftLowerLegsensor_input_file:
     SecondLeftLowerLegsensorValues = numpy.load(SecondLeftLowerLegsensor_input_file)

with open('../data_hexapod/RightLowerLegsensor.npy','rb') as RightLowerLegsensor_input_file:
     RightLowerLegsensorValues = numpy.load(RightLowerLegsensor_input_file)
     
with open('../data_hexapod/SecondRightLowerLegsensor.npy','rb') as SecondRightLowerLegsensor_input_file:
     SecondRightLowerLegsensorValues = numpy.load(SecondRightLowerLegsensor_input_file)

BackLowerLeg_touch = numpy.greater_equal(BackLowerLegsensorValues, ones)
FrontLowerLeg_touch = numpy.greater_equal(FrontLowerLegsensorValues, ones)
LeftLowerLeg_touch = numpy.greater_equal(LeftLowerLegsensorValues, ones)
SecondLeftLowerLeg_touch = numpy.greater_equal(SecondLeftLowerLegsensorValues, ones)
RightLowerLeg_touch = numpy.greater_equal(RightLowerLegsensorValues, ones)
SecondRightLowerLeg_touch = numpy.greater_equal(SecondRightLowerLegsensorValues, ones)

xor_backLower_frontLower = numpy.logical_xor(BackLowerLeg_touch,FrontLowerLeg_touch)
xor_leftLower_secondleftLower = numpy.logical_xor(LeftLowerLeg_touch,SecondLeftLowerLeg_touch)
xor_rightLower_secondrightLower = numpy.logical_xor(RightLowerLeg_touch,SecondRightLowerLeg_touch)
xor_leftLower_rightLower = numpy.logical_xor(xor_leftLower_secondleftLower,xor_rightLower_secondrightLower)

xor_allLegs = numpy.logical_xor(xor_backLower_frontLower,xor_leftLower_rightLower)

matplotlib.pyplot.plot((BackLowerLegsensorValues>0.999), label='BackLowerLegTouch', ls='', marker="o")
matplotlib.pyplot.plot((FrontLowerLegsensorValues>0.999)*2, label='FrontLowerLegTouch', ls='', marker="o")
matplotlib.pyplot.plot((LeftLowerLegsensorValues>0.999)*3, label='LeftLowerLegsensorTouch', ls='', marker="o")
matplotlib.pyplot.plot((SecondLeftLowerLegsensorValues>0.999)*4, label='SecondLeftLowerLegsensorTouch', ls='', marker="o")
matplotlib.pyplot.plot((RightLowerLegsensorValues>0.999)*5, label='RightLowerLegsensorTouch', ls='', marker="o")
matplotlib.pyplot.plot((SecondRightLowerLegsensorValues>0.999)*6, label='SecondRightLowerLegsensorTouch', ls='', marker="o")

# Plot
matplotlib.pyplot.plot()

# Adjusting limits to ignore 0s of when the legs are not touching anything
matplotlib.pyplot.ylim(0.5,6.5)

# Adding title
matplotlib.pyplot.title("Project B: Marching Hexapod \n LowerLegsSensors Touching Ground")

# Adding legend
matplotlib.pyplot.legend(ncol=3, fontsize='x-small')

# Adding Axis Labels
matplotlib.pyplot.xlabel("Foot Steps per Leg for each iteration i")
matplotlib.pyplot.ylabel("Separating Lower Leg Touching per line")

# Auto adjust layout
matplotlib.pyplot.tight_layout()

# Display
matplotlib.pyplot.show()

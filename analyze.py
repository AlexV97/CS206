import numpy
import numpy.matlib
import matplotlib.pyplot


ones = numpy.matlib.ones(1)

with open('../data_hexapod/BackLowerLegsensor.npy','rb') as BackLowerLegsensor_input_file:
     BackLowerLegsensorValues = numpy.load(BackLowerLegsensor_input_file)
matplotlib.pyplot.plot(BackLowerLegsensorValues, label='BackLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_hexapod/FrontLowerLegsensor.npy','rb') as FrontLowerLegsensor_input_file:
     FrontLowerLegsensorValues = numpy.load(FrontLowerLegsensor_input_file)
matplotlib.pyplot.plot(FrontLowerLegsensorValues, label='FrontLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_hexapod/LeftLowerLegsensor.npy','rb') as LeftLowerLegsensor_input_file:
     LeftLowerLegsensorValues = numpy.load(LeftLowerLegsensor_input_file)
matplotlib.pyplot.plot(LeftLowerLegsensorValues, label='LeftLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_hexapod/SecondLeftLowerLegsensor.npy','rb') as SecondLeftLowerLegsensor_input_file:
     SecondLeftLowerLegsensorValues = numpy.load(SecondLeftLowerLegsensor_input_file)
matplotlib.pyplot.plot(SecondLeftLowerLegsensorValues, label='SecondLeftLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_hexapod/RightLowerLegsensor.npy','rb') as RightLowerLegsensor_input_file:
     RightLowerLegsensorValues = numpy.load(RightLowerLegsensor_input_file)
matplotlib.pyplot.plot(RightLowerLegsensorValues, label='RightLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_hexapod/SecondRightLowerLegsensor.npy','rb') as SecondRightLowerLegsensor_input_file:
     SecondRightLowerLegsensorValues = numpy.load(SecondRightLowerLegsensor_input_file)
matplotlib.pyplot.plot(SecondRightLowerLegsensorValues, label='SecondRightLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

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

i_xor_allLegs = xor_allLegs * 1
print("analyze i_xor_allLegs= ",i_xor_allLegs )
count_onlyOneLegTouching = numpy.count_nonzero(i_xor_allLegs)
count_numberIterations = i_xor_allLegs.size
percentTimeOneLegTouch = count_onlyOneLegTouching/count_numberIterations

print("analyze count_onlyOneLegTouching=", count_onlyOneLegTouching, " / count_numberIterations=", count_numberIterations, " = percentTimeOneLegTouch", percentTimeOneLegTouch)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

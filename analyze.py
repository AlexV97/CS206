import numpy
import numpy.matlib
import matplotlib.pyplot


ones = numpy.matlib.ones(1)

with open('../data_quadruped/BackLowerLegsensor.npy','rb') as BackLowerLegsensor_input_file:
     BackLowerLegsensorValues = numpy.load(BackLowerLegsensor_input_file)
matplotlib.pyplot.plot(BackLowerLegsensorValues, label='BackLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_quadruped/FrontLowerLegsensor.npy','rb') as FrontLowerLegsensor_input_file:
     FrontLowerLegsensorValues = numpy.load(FrontLowerLegsensor_input_file)
matplotlib.pyplot.plot(FrontLowerLegsensorValues, label='FrontLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_quadruped/LeftLowerLegsensor.npy','rb') as LeftLowerLegsensor_input_file:
     LeftLowerLegsensorValues = numpy.load(LeftLowerLegsensor_input_file)
matplotlib.pyplot.plot(LeftLowerLegsensorValues, label='LeftLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data_quadruped/RightLowerLegsensor.npy','rb') as RightLowerLegsensor_input_file:
     RightLowerLegsensorValues = numpy.load(RightLowerLegsensor_input_file)
matplotlib.pyplot.plot(RightLowerLegsensorValues, label='RightLowerLegValues', linewidth=3)
matplotlib.pyplot.legend()

BackLowerLeg_touch = numpy.greater_equal(BackLowerLegsensorValues, ones)

FrontLowerLeg_touch = numpy.greater_equal(FrontLowerLegsensorValues, ones)

LeftLowerLeg_touch = numpy.greater_equal(LeftLowerLegsensorValues, ones)
i_LeftLowerLeg_touch = LeftLowerLeg_touch * 1
count_LeftLowerLeg_touch = numpy.count_nonzero(LeftLowerLeg_touch)
count_LeftLowernumberIterations = i_LeftLowerLeg_touch.size
percentTimeLeftLowerLeg_touch = count_LeftLowerLeg_touch/count_LeftLowernumberIterations
print("analyze LeftLowerLeg_touch=", count_LeftLowerLeg_touch, " / count_numberIterations=", count_LeftLowernumberIterations, " = percentTimeLeftLowerLeg_touch", percentTimeLeftLowerLeg_touch)

RightLowerLeg_touch = numpy.greater_equal(RightLowerLegsensorValues, ones)

xor_backLower_frontLower = numpy.logical_xor(BackLowerLeg_touch,FrontLowerLeg_touch)
xor_leftLower_rightLower = numpy.logical_xor(LeftLowerLeg_touch,RightLowerLeg_touch)

xor_allLegs = numpy.logical_xor(xor_backLower_frontLower,xor_leftLower_rightLower)

i_xor_allLegs = xor_allLegs * 1
count_onlyOneLegTouching = numpy.count_nonzero(i_xor_allLegs)
count_numberIterations = i_xor_allLegs.size
percentTimeOneLegTouch = count_onlyOneLegTouching/count_numberIterations

print("analyze count_onlyOneLegTouching=", count_onlyOneLegTouching, " / count_numberIterations=", count_numberIterations, " = percentTimeOneLegTouch", percentTimeOneLegTouch)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

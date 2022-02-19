import numpy
import matplotlib.pyplot

with open('../data/targetAngles_BackLegValues.npy','rb') as targetAngles_BackLeg_input_file:
     targetAngles_BackLegValues = numpy.load(targetAngles_BackLeg_input_file)
matplotlib.pyplot.plot(targetAngles_BackLegValues, label='targetAngles_BackLegValues', linewidth=3)
matplotlib.pyplot.legend()

with open('../data/targetAngles_FrontLegValues.npy','rb') as targetAngles_FrontLeg_input_file:
     targetAngles_FrontLegValues = numpy.load(targetAngles_FrontLeg_input_file)
matplotlib.pyplot.plot(targetAngles_FrontLegValues, label='targetAngles_FrontLegValues', linewidth=3)
matplotlib.pyplot.legend()

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

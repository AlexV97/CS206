import numpy
import matplotlib.pyplot


with open('../data/backLegSensorValues.npy','rb') as backLeg_input_file:
    backLegSensorValues = numpy.load(backLeg_input_file)
matplotlib.pyplot.plot(backLegSensorValues, label='backLegSensorValues', linewidth=2)
matplotlib.pyplot.legend()

with open('../data/frontLegSensorValues.npy','rb') as frontLeg_input_file:
    frontLegSensorValues = numpy.load(frontLeg_input_file)
matplotlib.pyplot.plot(frontLegSensorValues, label='frontLegSensorValues', linewidth=3)
matplotlib.pyplot.legend()

matplotlib.pyplot.legend()
matplotlib.pyplot.show()

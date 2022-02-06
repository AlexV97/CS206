import numpy
import matplotlib.pyplot


with open('../data/backLegSensorValues.npy','rb') as backLeg_input_file:
    backLegSensorValues = numpy.load(backLeg_input_file)
    
matplotlib.pyplot.plot(backLegSensorValues)

with open('../data/frontLegSensorValues.npy','rb') as frontLeg_input_file:
    frontLegSensorValues = numpy.load(frontLeg_input_file)
    
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()

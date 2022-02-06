import numpy
import matplotlib.pyplot


with open('../data/backLegSensorValues.npy','rb') as input_file:
    backLegSensorValues = numpy.load(input_file)
    
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()

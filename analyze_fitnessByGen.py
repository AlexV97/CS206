import numpy
import numpy.matlib
import matplotlib.pyplot
import matplotlib.figure
import matplotlib.markers

ones = numpy.matlib.ones(1)

with open('../data_hexapod/Cumulative_BestFitness_PerGeneration.txt','rb') as FitnessByGen_input_file:
     FitnessByGen_Values = numpy.load(FitnessByGen_input_file)


matplotlib.pyplot.plot(FitnessByGen_Values, label='Fitness By Gen', ls='', marker="o")

# Plot
matplotlib.pyplot.plot()

# Adjusting limits to ignore 0s of when the legs are not touching anything
#matplotlib.pyplot.ylim(0.5,6.5)

# Adding title
matplotlib.pyplot.title("Project B: Marching Hexapod \n Fitness By Generation")

# Adding legend
matplotlib.pyplot.legend(ncol=3, fontsize='x-small')

# Adding Axis Labels
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Displacement Fitness")

# Auto adjust layout
matplotlib.pyplot.tight_layout()

# Display
matplotlib.pyplot.show()

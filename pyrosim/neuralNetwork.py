import pyrosim.pyrosim as pyrosim    ###
from pyrosim.neuron  import NEURON
from pyrosim.synapse import SYNAPSE

class NEURAL_NETWORK: 

    def __init__(self,nndfFileName):

        self.neurons = {}

        self.synapses = {}

        f = open(nndfFileName,"r")

        for line in f.readlines():

            self.Digest(line)

        f.close()


    def Print(self):
        print("neuralNetwork - Print():")
        print("")
        print("neuralNetwork - Print() - Print_Sensor_Neuron_Values():")
        print("")
        self.Print_Sensor_Neuron_Values()
        print("neuralNetwork - Print() - Print_Hidden_Neuron_Values():")
        print("")
        self.Print_Hidden_Neuron_Values()
        print("neuralNetwork - Print() - Print_Motor_Neuron_Values():")
        print("")
        self.Print_Motor_Neuron_Values()

        print("")
    
    def Update(self):
        for neuronName in self.neurons:
            print("neuralNetwork - Update() - Key=neuronName=", neuronName)
            self.neurons[neuronName] = NEURON(neuronName)
            if self.neurons[neuronName].Is_Sensor_Neuron(): #step - 34
                self.neurons[neuronName].Update_Sensor_Neuron()
            else: self.neurons[neuronName].Update_Hidden_Or_Motor_Neuron() #Step 50

    def Get_Motor_Neurons_Joint(neuronName):
        return self.neurons[neuronName].Get_Joint_Name()
        
    def Get_Neuron_Names(self):
        print("neuralNetwork - Get_Neuron_Names() - self=", self)
        self.Print_Sensor_Neuron_Values()
        neurons_keys=self.neurons.keys()
        print("neuralNetwork - neurons_keys=", neurons_keys)
        return neurons_keys
        
    def Is_Motor_Neuron(self, neuronName):
        print("neuralNetwork - Is_Motor_Neuron() - self", self, " - neuronName=", neuronName)
        print("")
        return (self.neurons[neuronName].Is_Motor_Neuron())

    def Is_Sensor_Neuron(self,neuronName):
        return self.neurons[neuronName].Is_Sensor_Neuron()
        
    def Is_Hidden_Neuron(self,neuronName):
        return self.neurons[neuronName].Is_Hidden_Neuron()
     
#    def Get_Name(self):
#        return self.neurons[neuronName].Get_Name()
        
    def Get_Motor_Neurons_Joint(neuronName):
        return self.neurons[neuronName].Get_Joint_Name()
        
    def Get_Value_Of(neuronName): #Step 68
        return self.NEURON.Get_Value(neuronName) #Step 68
        
# ---------------- Private methods --------------------------------------

    def Add_Neuron_According_To(self,line):

        neuron = NEURON(line)

        self.neurons[ neuron.Get_Name() ] = neuron

    def Add_Synapse_According_To(self,line):

        synapse = SYNAPSE(line)

        sourceNeuronName = synapse.Get_Source_Neuron_Name()

        targetNeuronName = synapse.Get_Target_Neuron_Name()

        self.synapses[sourceNeuronName , targetNeuronName] = synapse

    def Digest(self,line):

        if self.Line_Contains_Neuron_Definition(line):

            self.Add_Neuron_According_To(line)

        if self.Line_Contains_Synapse_Definition(line):

            self.Add_Synapse_According_To(line)

    def Line_Contains_Neuron_Definition(self,line):

        return "neuron" in line

    def Line_Contains_Synapse_Definition(self,line):

        return "synapse" in line

    def Print_Sensor_Neuron_Values(self):

        print("sensor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Sensor_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Hidden_Neuron_Values(self):

        print("hidden neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Hidden_Neuron():

                self.neurons[neuronName].Print()

        print("")

    def Print_Motor_Neuron_Values(self):

        print("motor neuron values: " , end = "" )

        for neuronName in sorted(self.neurons):

            if self.neurons[neuronName].Is_Motor_Neuron():

                self.neurons[neuronName].Print()

        print("")

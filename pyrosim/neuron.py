import math

import pybullet

import pyrosim.pyrosim as pyrosim

import pyrosim.constants as c

class NEURON: 

    def __init__(self,line):
 
        self.Determine_Name(line)

        self.Determine_Type(line)

        self.Search_For_Link_Name(line)

        self.Search_For_Joint_Name(line)

        self.Set_Value(0.0)

    def Add_To_Value( self, value ):
        #print("Add_To_Value() self=", self, "-self.Get_Value()=", self.Get_Value(), "+value=", value, "=",(self.Get_Value() + #value ) )
        #self.Set_Value( (self.Get_Value() + value ) ) # self.Set_Value( (self.Get_Value() ) ) - TypeError: 'int' object is not callable
        new_value=self.Get_Value() + value
        self.value = new_value

    def Get_Joint_Name(self):

        return self.jointName

    def Get_Link_Name(self):

        return self.linkName

    def Get_Name(self):

        return self.name

    def Get_Value(self):

        return self.value

    def Is_Sensor_Neuron(self):

        return self.type == c.SENSOR_NEURON

    def Is_Hidden_Neuron(self):

        return self.type == c.HIDDEN_NEURON

    def Is_Motor_Neuron(self):
        return self.type == c.MOTOR_NEURON

    def Print(self):
        self.Print_Value()

    def Set_Value(self,value):

        self.value = value

    def Update_Sensor_Neuron(self):
        self.Set_Value(pyrosim.Get_Touch_Sensor_Value_For_Link(self.Get_Link_Name()))
        
    def Allow_Presynaptic_Neuron_To_Influence_Me(self, weight, presynaptic_value):
        #print("Allow_Presynaptic_Neuron_To_Influence_Me() weight(", weight, ")*presynaptic_value(", presynaptic_value,")=", #weight*presynaptic_value)
        return(weight*presynaptic_value)

    def Update_Hidden_Or_Motor_Neuron(self, neurons, synapses):
        #self.Set_Value(math.pi/4.0)
        self.Set_Value = 0
        synapse_keys = synapses.keys()
        print("before for loop synapse_keys=", synapse_keys, " - neurons' value=", neurons[self.Get_Name()].Get_Value() )
        print("neuron value=", neurons[self.Get_Name()].Get_Value() )
        for each_synapse in synapses:
            print("each_synapse=", each_synapse)
            if ( each_synapse[1] == self.Get_Name()):
                print("pre-synaptic neurons =",each_synapse[0], " - post-synaptic neurons =",each_synapse[1] )
                print("initial self.Get_Value()=",self.Get_Value())
                val_to_add = self.Allow_Presynaptic_Neuron_To_Influence_Me(synapses[each_synapse].Get_Weight(), neurons[self.Get_Name()].Get_Value())
                val_to_add+=neurons[each_synapse[0]].Get_Value() # adding presynaptic neuron value
                print("trying to add:",val_to_add)
                self.Add_To_Value(val_to_add)
                print("after self.Get_Value()=",self.Get_Value())
        print("neuron value=", neurons[self.Get_Name()].Get_Value() )
        exit()
    
# -------------------------- Private methods -------------------------

    def Determine_Name(self,line):

        if "name" in line:

            splitLine = line.split('"')

            self.name = splitLine[1]

    def Determine_Type(self,line):

        if "sensor" in line:

            self.type = c.SENSOR_NEURON

        elif "motor" in line:

            self.type = c.MOTOR_NEURON

        else:

            self.type = c.HIDDEN_NEURON

    def Print_Name(self):

       print(self.name)

    def Print_Type(self):

       print(self.type)

    def Print_Value(self):

       print(self.value , " " , end="" )

    def Search_For_Joint_Name(self,line):

        if "jointName" in line:

            splitLine = line.split('"')

            self.jointName = splitLine[5]

    def Search_For_Link_Name(self,line):

        if "linkName" in line:

            splitLine = line.split('"')

            self.linkName = splitLine[5]

    def Threshold(self):

        self.value = math.tanh(self.value)

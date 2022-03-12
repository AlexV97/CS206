import pyrosim.pyrosim as pyrosim
import random
l=1.0
w=1.0
h=1.0
box1_x=0
box1_y=0
box1_z=h/2
class Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[(box1_x-2.0),(box1_y+2.0),box1_z] , size=[w,l,h])
    pyrosim.End()
class Create_Robot():  # 3-link, 2-joint robot
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[w,l,h])

    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
    type = "revolute", position = [1.0,0,1.0])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[w,l,h])

    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
    type = "revolute", position = [2.0,0,1.0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[w,l,h])

    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[w,l,h])

    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" ,
    type = "revolute", position = [1.0,0,1.0])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[w,l,h])
    
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" ,
    type = "revolute", position = [2.0,0,1.0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[w,l,h])

    pyrosim.End()
    
def Generate_Brain():
    sensor_dict = {
        0:"Torso",
        1:"BackLeg",
        2:"FrontLeg"
    }
    motor_dict = {
        3:"Torso_BackLeg",
        4:"Torso_FrontLeg"
    }
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")
    ## Initital - moving slowly toward viewer/right
    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0)
    ## 2nd hopping up and down, not moving much
    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0)
    ## 3rd hopping and rotating on itself
    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0)
    ## 4th hopping forward
    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.9)
    #pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0)
    ## 5th hopping twice forward then moving backward limping
    pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 3 , weight = 0.9)
    pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0)
    pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0)

    for name_of_sensor_neuron in sensor_dict.keys():
        for name_of_motor_neuron in motor_dict.keys():
                pyrosim.Send_Synapse(sourceNeuronName = sensor_dict[name_of_sensor_neuron] , targetNeuronName = motor_dict[name_of_motor_neuron] , weight = random.uniform(-1,1))

    pyrosim.End()
    
Create_World()
Create_Robot()
Generate_Body()
Generate_Brain()

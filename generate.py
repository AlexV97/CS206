import pyrosim.pyrosim as pyrosim
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
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3, jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4, jointName = "Torso_FrontLeg")
    pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 3 , weight = 10.)
    pyrosim.End()
    
Create_World()
Create_Robot()
Generate_Body()
Generate_Brain()

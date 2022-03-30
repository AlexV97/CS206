import pyrosim.pyrosim as pyrosim
import random
l=1.0
w=1.0
h=1.0
box1_x=0
box1_y=0
box1_z=h/2

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

Create_Robot()


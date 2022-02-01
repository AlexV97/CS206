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
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[w,l,h])
    pyrosim.Send_Joint(name = "Link0_Link1" , parent= "Link0" , child = "Link1" ,
    type = "revolute", position = [0,0,1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[w,l,h])
    pyrosim.Send_Joint(name = "Link1_Link2" , parent= "Link1" , child = "Link2" ,
    type = "revolute", position = [0,0,1.0])
    pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[w,l,h])
    
    pyrosim.End()
    
Create_World()
Create_Robot()

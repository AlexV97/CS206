import pyrosim.pyrosim as pyrosim
l=1
w=1
h=1
box1_x=0
box1_y=0
box1_z=h/2
class Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[box1_x,box1_y,box1_z] , size=[w,l,h])
    
pyrosim.End()
Create_World()


import pyrosim.pyrosim as pyrosim
l=1
w=1
h=1
box1_x=0
box1_y=0
box1_z=h/2
box2_x=1
box2_y=0
box2_z=h*3/2

pyrosim.Start_SDF("boxes.sdf")
box_ratio=1
for k in range(5):
    for j in range(5):
        box_ratio=1 # reset box ratio for each column going up
        for i in range(10): # height
            pyrosim.Send_Cube(name="Box", pos=[(box1_x+k),(box1_y+j),(box1_z+i)] , size=[box_ratio*w,box_ratio*l,box_ratio*h])
            box_ratio*=0.9
    
pyrosim.End()

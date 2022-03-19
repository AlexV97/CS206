import copy
import constants as c
import os
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        print("parallelHillClimber - __init__()")
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        print("*** parallelHillClimber - Evolve()")
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key].Start_Simulation("DIRECT")
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key].Wait_For_Simulation_To_End("DIRECT")
            this_sol_fitness = self.parents[entry_key].fitness
            print("phc Evolve() solution fitness=", this_sol_fitness)
        self.Evolve_For_One_Generation()
            
    def Spawn(self):
        print("parallelHillClimber - Spawn()")
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
        
    def Mutate(self):
        print("parallelHillClimber - Mutate()")
        self.child.Mutate()
        #exit()
        
    def Select(self):
        print("parallelHillClimber - Select()")
        if ( self.parent.fitness > self.child.fitness):
            self.parent = self.child
        
    def Evolve_For_One_Generation(self):
        print("parallelHillClimber - Evolve_For_One_Generation()")
        #self.Spawn()
        #self.Mutate()
        #self.child.Evaluate("DIRECT")
        #self.Print()
        ##exit() # step 62
        #self.Select()
        ##exit()
        pass

    def Print(self):
        print("Parent Fitness= ", self.parent.fitness, " - Child Fitness= ", self.child.fitness)

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass

import copy
import constants as c
import os
import time
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0

        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        self.Evaluate(self.parents)
        self.Evolve_For_One_Generation()
            
    def Spawn(self):
        #print("parallelHillClimber - Spawn()")
        self.children = {}
        for entry_key in range(0,c.populationSize):
            self.children[entry_key] = copy.deepcopy(self.parents[entry_key])
            self.children[entry_key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        #print("parallelHillClimber - Mutate()")
        for entry_key in range(0,c.populationSize):
            self.children[entry_key].Mutate()
        
    def Select(self):
        for entry_key in range(0,c.populationSize):
            #if ( self.parents[entry_key].fitness < self.children[entry_key].fitness ):
            if ( self.parents[entry_key].fitness > self.children[entry_key].fitness ):
                self.parents[entry_key] = self.children[entry_key]
        
    def Evolve_For_One_Generation(self):
        #print("parallelHillClimber - Evolve_For_One_Generation()")
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #self.Print()
        self.Select()
        #print("phc Evolve_For_One_Generation() after Select()")
        self.Print()


    def Print(self):
        print("")
        for entry_key in range(0,c.populationSize):
            print("phc Print() entry_key= " , entry_key, " - Parent Fitness= ", self.parents[entry_key].fitness, " - Child Fitness= ", self.children[entry_key].fitness)
        print("")

    def Show_Best(self):
        entry_key_lowest_parent = -1
        lowest_fitness=999
        for entry_key in range(0,c.populationSize):
            if ( self.parents[entry_key].fitness < lowest_fitness ):
                entry_key_lowest_parent = entry_key
                lowest_fitness          = self.parents[entry_key].fitness
        #print("*** phc Show_Best() Simulating lowest parent entry_key_lowest_parent= ", entry_key_lowest_parent, " - lowest_fitness= ", lowest_fitness)
        self.parents[entry_key_lowest_parent].Start_Simulation("GUI", 1)
                
    
    def Evaluate(self, solutions):

        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Start_Simulation("DIRECT", 0)
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Wait_For_Simulation_To_End("DIRECT")
            
        

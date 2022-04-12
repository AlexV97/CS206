import copy
import constants as c
import os
import time 
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf 2>nul ")
        os.system("rm fitness*.nndf  2>nul ")
        self.parents = {}
        self.nextAvailableID = 0

        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        #print("parallelHillClimber - Evolve()")
        self.Evaluate(self.parents)
        for gen in range( c.numberOfGenerations):
            self.Evolve_For_One_Generation()
          
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        #self.Print() # while debugging


    def Spawn(self):
        self.children = {}
        for i, parent in self.parents.items():
            self.children[i] = copy.deepcopy(parent)
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        for i, child in self.children.items():
            child.Mutate()

    def Select(self):
        for entry_key in range(0,c.populationSize):
            #if ( self.children[entry_key].fitness < self.parents[entry_key].fitness ):
            if ( self.children[entry_key].fitness > self.parents[entry_key].fitness ):
                self.parents[entry_key] = self.children[entry_key]
        
#    def Print(self):
#        #print("parallelHillClimber - Print()")
#        print("")
#        for entry_key in range(0,c.populationSize):
#            print("phc Print() entry_key= " , entry_key, " - Parent Fitness= ", self.parents[entry_key].fitness, " - Child Fitness= ", #self.children[entry_key].fitness)
#        print("")

    def Show_Best(self):
        #print("parallelHillClimber - Show_Best() c.populationSize= ", c.populationSize)
#        entry_key_lowest_parent = -1
#        lowest_fitness=999
#        for entry_key in range(0,c.populationSize):
#            print("parallelHillClimber - Show_Best() entry_key= ", entry_key, " - self.parents[entry_key].fitness= ", #self.parents[entry_key].fitness)
#            if ( self.parents[entry_key].fitness < lowest_fitness ):
#                entry_key_lowest_parent = entry_key
#                lowest_fitness          = self.parents[entry_key].fitness
###
        entry_key_best_parent = -1
        best_fitness=-999
        for entry_key in range(0,c.populationSize):
            print("parallelHillClimber - Show_Best() entry_key= ", entry_key, " - self.parents[entry_key].fitness= ", self.parents[entry_key].fitness)
            if ( self.parents[entry_key].fitness > best_fitness ):
                entry_key_best_parent = entry_key
                best_fitness          = self.parents[entry_key].fitness
###
        print("parallelHillClimber - Show_Best() Best Key = ", entry_key_best_parent, " Best Fitness = ", best_fitness)
        self.parents[entry_key_best_parent].Start_Simulation("GUI", 1)
                
    
    def Evaluate(self, solutions):
        #print("parallelHillClimber - Evaluate()")
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Start_Simulation("DIRECT", 0)
        #print("parallelHillClimber - Evaluate() - All Simulation Started")
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Wait_For_Simulation_To_End("DIRECT")
        #print("parallelHillClimber - Evaluate() - All Simulation Completed")
            
        

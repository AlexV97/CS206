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
        print("phc __init__ self.parents = ")
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            #print(" phc __init__() entry_key= ", entry_key, " - self.parents[entry_key].myID= ", self.parents[entry_key].myID)
    
    def Evolve(self):
        print("*** parallelHillClimber - Evolve()")
#        for entry_key in range(0,c.populationSize):
#            self.parents[entry_key].Start_Simulation("DIRECT")
#        for entry_key in range(0,c.populationSize):
#            self.parents[entry_key].Wait_For_Simulation_To_End("DIRECT")
#            this_sol_fitness = self.parents[entry_key].fitness
#            print("phc Evolve() solution fitness=", this_sol_fitness)
        self.Evaluate(self.parents)
        self.Evolve_For_One_Generation()
            
    def Spawn(self):
        print("parallelHillClimber - Spawn()")
        #self.child = copy.deepcopy(self.parent)
        #self.child.Set_ID(self.nextAvailableID)
        #self.nextAvailableID += 1
        #
        self.children = {}
        for entry_key in range(0,c.populationSize):
            self.children[entry_key] = copy.deepcopy(self.parents[entry_key])
            self.children[entry_key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            #print(" phc Spawn() entry_key= ", entry_key, " - self.children[entry_key].myID= ", self.children[entry_key].myID)
        #exit()
            
        
    def Mutate(self):
        print("parallelHillClimber - Mutate()")
        #self.child.Mutate()
        for entry_key in range(0,c.populationSize):
            self.children[entry_key].Mutate()
        #exit()
        
    def Select(self):
        print("parallelHillClimber - Select()")
        #if ( self.parent.fitness > self.child.fitness):
        #    self.parent = self.child
        for entry_key in range(0,c.populationSize):
            if ( self.parents[entry_key].fitness > self.children[entry_key].fitness ):
                self.parents[entry_key] = self.children[entry_key]
        
    def Evolve_For_One_Generation(self):
        print("parallelHillClimber - Evolve_For_One_Generation()")
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.Print()
        ##exit()
        #pass

    def Print(self):
        print("")
        for entry_key in range(0,c.populationSize):
            print("phc Print() entry_key= " , entry_key, " - Parent Fitness= ", self.parents[entry_key].fitness, " - Child Fitness= ", self.children[entry_key].fitness)
        print("")

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass
    
    def Evaluate(self, solutions):
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Start_Simulation("DIRECT")
        for entry_key in range(0,c.populationSize):
            solutions[entry_key].Wait_For_Simulation_To_End("DIRECT")
            #this_sol_fitness = solutions[entry_key].fitness
            #print("phc Evaluate() solution fitness=", this_sol_fitness)
        

import copy
import constants as c
from solution import SOLUTION
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        ##print("hillclimber - __init__()")
        #self.parent = SOLUTION()
        self.parents = {}
        self.nextAvailableID = 0
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            #print("parallellHillClimber for loop entry_key=", entry_key, "- self.parents=", self.parents[entry_key])
        #print("parallellHillClimber - self.parents=", self.parents, " - c.populationSize", c.populationSize)
        #pass
    
    def Evolve(self):
        print("*** hillclimber - Evolve() - calls self.parent.Evaluate()")
        #self.parent.Evaluate("GUI") # to show first random solution in GUI
        for entry_key in range(0,c.populationSize):
            self.parents[entry_key].Evaluate("GUI") # to show first random solution in GUI
            print("parallellHillClimber Evolve() entry_key=", entry_key, "- self.parents=", self.parents[entry_key])
        #for currentGeneration in range(c.numberOfGenerations):
        #    #print("*** parallelHillClimber - Evolve() - calls self.Evolve_For_One_Generation()")
        #    print("*** Evolve() Generation = ", currentGeneration)
        #    self.Evolve_For_One_Generation()
        #pass
            
    def Spawn(self):
        print("parallelHillClimber - Spawn()")
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
        
    def Mutate(self):
        print("parallelHillClimber - Mutate()")
        self.child.Mutate()
        #print("parallelHillClimber - Mutate() - self.parent.weights= \n", self.parent.weights)
        #print("parallelHillClimber - Mutate() - self.child.weights= \n", self.child.weights)
        #exit()
        
    def Select(self):
        print("parallelHillClimber - Select()")
        if ( self.parent.fitness > self.child.fitness):
            self.parent = self.child
        
    def Evolve_For_One_Generation(self):
        print("parallelHillClimber - Evolve_For_One_Generation()")
        #print("parallelHillClimber - self.parent=", self.parent)
        #print("parallelHillClimber - self.child=", self.child)
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        #exit() # step 62
        self.Select()
        #exit()

    def Print(self):
        print("Parent Fitness= ", self.parent.fitness, " - Child Fitness= ", self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        #pass

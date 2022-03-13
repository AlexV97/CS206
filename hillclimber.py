import copy
import constants as c
from solution import SOLUTION
class HILL_CLIMBER:
    def __init__(self):
        print("hillclimber - __init__()")
        self.parent = SOLUTION()
        self.child = SOLUTION() # needed?
        #pass
    
    def Evolve(self):
        print("hillclimber - Evolve()")
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    def Spawn(self):
        print("hillclimber - Spawn()")
        self.child = copy.deepcopy(self.parent)
        
    def Mutate(self):
        print("hillclimber - Mutate()")
        self.child.Mutate()
        #print("hillclimber - Mutate() - self.parent.weights= \n", self.parent.weights)
        #print("hillclimber - Mutate() - self.child.weights= \n", self.child.weights)
        #exit()
        
    def Select(self):
        print("hillclimber - Select()")
        self.child.Select()
        print("hillclimber - Select() - self.parent.fitness=", self.parent.fitness)
        print("hillclimber - Select() - self.child.fitness=", self.child.fitness)
        #exit()
        
    def Evolve_For_One_Generation(self):
        print("hillclimber - Evolve_For_One_Generation()")
        print("hillclimber - self.parent=", self.parent)
        print("hillclimber - self.child=", self.child)
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        exit() # step 62
        self.Select()
        #exit()

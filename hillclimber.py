import copy
import constants as c
from solution import SOLUTION
class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        #pass
    
    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            pass
            
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        
    def Mutate(self):
        pass
        
    def Select(self):
        pass
        
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()

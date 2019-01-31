### File: missionary.py
### Implements the missionaries and cannibals problem for state
### space search

from search import *

class MissionaryState:
    """
    Implement this.
    """
    def __init__(self, m, c, b):
        self.m = m
        self.c = c
        self.b = b
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "("+str(self.m)+","+str(self.c)+","+str(self.b)+")"
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
    
        """
        if self.m>3 or self.c>3 or self.b>1:return 1
        if self.m<0 or self.c<0 or self.b<0:return 1
        if (self.m<self.c and self.m!=0) or (self.m>self.c and self.m!=3):return 1
        return 0
        
        
    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.m==state.m and self.c==state.c and self.b==state.b
    
    def L01(self):
        if self.b==1:
            return MissionaryState(self.m,self.c-1,0)
        else:
            return MissionaryState(-1,-1,-1)
    def L10(self):
        if self.b==1:
            return MissionaryState(self.m-1,self.c,0)
        else:
            return MissionaryState(-1,-1,-1)  
    def L11(self):
        if self.b==1:
            return MissionaryState(self.m-1,self.c-1,0)
        else:
            return MissionaryState(-1,-1,-1)
    def L02(self):
        if self.b==1:
            return MissionaryState(self.m,self.c-2,0)
        else:
            return MissionaryState(-1,-1,-1)
    def L20(self):
        if self.b==1:
            return MissionaryState(self.m-2,self.c,0)
        else:
            return MissionaryState(-1,-1,-1)
    def R01(self):
        if self.b==0:
            return MissionaryState(self.m,self.c+1,1)
        else:
            return MissionaryState(-1,-1,-1)
    def R10(self):
        if self.b==0:
            return MissionaryState(self.m+1,self.c,1)
        else:
            return MissionaryState(-1,-1,-1)
    def R11(self): 
        if self.b==0:
            return MissionaryState(self.m+1,self.c+1,1)
        else:
            return MissionaryState(-1,-1,-1)
    def R02(self):
        if self.b==0:
            return MissionaryState(self.m,self.c+2,1)
        else:
            return MissionaryState(-1,-1,-1)
    def R20(self): 
        if self.b==0:
            return MissionaryState(self.m+2,self.c,1)
        else:
            return MissionaryState(-1,-1,-1)
    
    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["L01", "L10", "L11", "L02", "L20",
                "R01", "R10", "R11", "R02", "R20"]
    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.L01(), self.L10(), self.L11(), self.L02(), self.L20(),
                self.R01(), self.R10(), self.R11(), self.R02(), self.R20()]
Search(MissionaryState(3,3,1), MissionaryState(0,0,0))
import fmteach.ui

class PassedWaiting:
    def __init__ (self,covermerge):
        fmteach.ui.messages.error (f"This ({__file__}) is where you should add code for your passed/waiting listimplementation ")
        self._covermerge = covermerge
        self._passed = []
        self._waiting = []
        
        
    def mergeState (self,p,state):
        return None
    
    def insert (self,state):
        pass
    
    def hasWaiting (self):
        return len(self._waiting) > 0
    
    def pull (self):
        return self._waiting.pop ()

    def getStates (self):
        yield from self._passed

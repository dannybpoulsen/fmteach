import fmteach.vm.interface

class PassedWaiting:
    def __init__ (self,covermerge):
        self._covermerge = covermerge
        self._passed = []
        self._waiting = []


    def checkCover (self,p,state):
        if state.getLoc () != p.getLoc ():
            return False
        else:
            for ss,ps in zip (state.getValues (),p.getValues ()):
                if not self._covermerge.Covers (ps,ss):
                    return False

        return True
        
    def mergeState (self,p,state):
        if p.getLoc () != state.getLoc ():
            # Not the same location...thus the state cannot be merged
            return None
        else:
            #Try to merge the states values
            l = []
            for ss,ps in zip (state.getValues (),p.getValues ()):
                nval = self._covermerge.Merge (ss,ps)
                if nval == None:
                    return None
                l.append(nval)
            return fmteach.vm.interface.State (l,p.getLoc ())
            
    def insert (self,state):
        for p in self._passed:
            
            if self.checkCover (p,state):
                
                #We already have a state covering this one. Stop 
                return
            
        for i in range(0,len(self._passed)):
            nstate = self.mergeState (self._passed[i],state)
            if nstate:
                self._passed[i] = nstate
                self._waiting.append(nstate)
                return 
                
        self._passed.append(state)
        self._waiting.append(state)
        
        
    def hasWaiting (self):
        return len(self._waiting) > 0

    def pull (self):
        return self._waiting.pop ()

    def getStates (self):
        yield from self._passed

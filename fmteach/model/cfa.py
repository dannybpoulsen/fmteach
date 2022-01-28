class Location:
    def __init__ (self,name = None):
        self._name = name or "??"  

    def getName (self):
        return self._name

        
class Edge:
    def __init__ (self,fromm,to, instructions = None):
        self._from = fromm
        self._to = to
        self._instructions = instructions or []
        
    def getfrom (self):
        return self._from

    def getTo (self):
        return self._to

    def instructions (self):
        yield from self._instructions
    
class CFA:
    def __init__(self):
        self._edges = []
        self._locations = []
        self._edgesfrom = {}
        self._edgesto = {}
        

    def makeLocation (self,name = None):
        loc  = Location (name or f"loc{len(self._locations)}")
        self._locations.append (loc)
        self._edgesfrom[loc] = []
        self._edgesto[loc] = []
        return loc

    def setInitialLocation (self,location):
        self._initiallocation = location

    def getInitialLocation (self):
        return self._initiallocation 
    
        
    def makeEdge (self,fromm,to,instructions):
        self._edges.append (Edge (fromm,to,instructions))
        self._edgesfrom[fromm].append(self._edges[-1])
        self._edgesto[to].append(self._edges[-1])
        return self._edges[-1]

    def getEdgesFrom (self,loc):
        for e in self._edgesfrom[loc]:
            yield e


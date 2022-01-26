class Location:
    def __init__ (self,instructions,name = None):
        self._name = name or "??"

    def getName (self):
        return self._name

        
class Edge:
    def __init__ (self,from,to, instructions = None):
        self._from = from
        self._to = to
        self._instructions = instructions or []
        
    def getfrom (self):
        return self._from

    def getTo (self):
        return self._to

class CFA:
    def __init__(self):
        self._edges = []
        self._locations = []
        self._edgesfrom = {}
        self._edgesto = {}
        

    def makeLocation (self,name = None):
        self._locations.append (Location (name or f"loc{len(self._edges)}"))
        self._edgesfrom[self._location[-1]] = []
        self._edgesto[self._location[-1]] = []
        return self._locations[-1]

    def setInitialLocation (self,location):
        self._initiallocation = location

    def makeEdge (self,from,to,instructions):
        self._edges.append (from,to,instructions)
        self._edgesfrom[from].append(self._edges[-1])
        self._edgesto[to].append(self._edges[-1])
        return self._edges[-1]
    


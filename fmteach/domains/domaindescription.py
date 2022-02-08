import enum

class TriBool(enum.Enum):
    TT = 1
    FF = 2
    Unknown = 3


class Descriptor:
    def  __init__(self,valcreator,operations,covermerge,nondet = True):
        self._valcreator = valcreator
        self._operations = operations
        self._covermerge = covermerge
        self._nondet = nondet
        
    def valueCreator (self):
        return self._valcreator 

    def valueOperations (self):
        return self._operations 

    def valueCoverMerge (self):
        return self._covermerge 

    def initialPath (self):
        return None
    
    def hasNonDet (self):
        return self._nondet

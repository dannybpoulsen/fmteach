import enum

class Types(enum.Enum):
    I8 = 0
    I32 = 1
    Pointer = 2
    Bool = 3
    

class BoolConstant:
    def __init__(self,val = False):
        self._val = val

    def getType (self):
        return Types.Bool

class IntegerConstant:
    def __init__(self,val = 0):
        self._val = 0

    def getType (self):
        return Types.Integer

class Register:
    def __init__(self,name = None,typee = None ):
        self._name = name or "??"
        self._type = typee or Types.Integer

    def getType (self):
        return self._type

    def getName (self):
        return self._name
    
    


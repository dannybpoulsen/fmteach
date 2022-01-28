import enum
import numpy

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

    def __str__(self):
        return str(self._val)
    
    
class IntegerConstant:
    def __init__(self,val = 0,type = None  ):
        if type == Types.I8:
            self._val = numpy.int8 (val)
        if type == Types.I32:
            self._val = numpy.int32 (val)
        if type == Types.Pointer:
            self._val = numpy.int32 (val)
        if type == Types.Bool:
            self._val = numpy.int8 (val)
        
        self._type = type

    def getType (self):
        return type

    def __str__(self):
        return str(self._val)

    def  isRegister (self):
        return False

    def getValue (self):
        return self._val
    
class Register:
    def __init__(self,name = None,typee = None,id = 0 ):
        self._name = name or "??"
        self._type = typee or Types.Integer
        self._id = id 

    def getType (self):
        return self._type

    def getName (self):
        return self._name

    def getId (self):
        return self._id
    
    def __str__ (self):
        return self._name

    def  isRegister (self):
        return True
    

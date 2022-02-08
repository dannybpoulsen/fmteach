import  enum

class  Value:
    def __str__(self):
        return  "??"

class ConstantCreator:
    def __init__(self):
        self._val = Value ()
        
    def makeValue  (self,val, type):
        return self._val

class Operations:
    def Add (val1,val2):
        return self._val

    def Sub (val1,val2):
        return self._val
    
    def Div (val1,val2):
        return self._val
    
    def Mul (val1,val2):
        return self._val
    
    def Eq (val1,val2):
        return  self._val
    
    def NEq (val1,val2):
        return  self._val

    def LEq (val1,val2):
        return  self._val

    def GEq (val1,val2):
        return  self._val
    
    def Lt (val1,val2):
        return  self._val

    def Gt (val1,val2):
        return  self._val

    
class CoverMerge:
    # Check if val1 is larger than val2
    def  Covers (val1,val2):
        return True
    
    #Merge Value1 and Value2
    # Maay return None if a merge is impossible
    def Merge (val1,val2):
        return val1

    

    

    
    

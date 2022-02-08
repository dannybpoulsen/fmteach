from fmteach.domains.domaindescription import *
import  enum

class  Value:
    def __str__(self):
        return  "??"

    def TriBool (self):
        return TriBool.Unknown
    
class ConstantCreator:
    def __init__(self):
        self._val = Value ()
        
    def makeValue  (self,val, type):
        return self._val

    def makeNonDet (self,type):
        return self.makeValue (0,type)
    
    
class Operations:
    def Add (self,val1,val2):
        return val1

    def Sub (self,val1,val2):
        return val1
    
    def Div (self,val1,val2):
        return val1
    
    def Mul (self,val1,val2):
        return val1
    
    def Eq (self,val1,val2):
        return  val1
    
    def NEq (self,val1,val2):
        return  val1

    def LEq (self,val1,val2):
        return  val1

    def GEq (self,val1,val2):
        return  val1
    
    def Lt (self,val1,val2):
        return  val1

    def Gt (self,val1,val2):
        return  val1

    def Negate (self,val1):
        return val1
    
class CoverMerge:
    # Check if val1 is larger than val2
    def  Covers (self,val1,val2):
        return True

    #Merge Value1 and Value2
    # Maay return None if a merge is impossible
    def Merge (self,val1,val2):
        return val1

    

    

    
    
descr =  Descriptor (ConstantCreator (),Operations (),CoverMerge ())

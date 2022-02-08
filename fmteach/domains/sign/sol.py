from fmteach.domains.domaindescription import *
import fmteach.model.values
import numpy
import os

import  enum

class SignValues(enum.Enum):
    Bot = 0
    Zero = 1
    Plus  = 2
    Neg = 3
    All = 4


def symbToSign (l):
    if l == "B":
        return SignValues.Bot
    elif l == "0":
        return SignValues.Zero
    elif l == "+":
        return SignValues.Plus
    elif l == "-":
        return SignValues.Neg
    elif l == "A":
        return SignValues.All
    assert (False)
    
def readTable (path):
    table = []
    with open(path,'r') as ff:
        for l in ff.readlines ():
            table.append ([symbToSign(l) for  l in l.strip().split (",")])
    return table
mpath = os.path.split(os.path.abspath (__file__))[0]
addTable = readTable (os.path.join (mpath,"addtable.csv"))
subTable = readTable (os.path.join (mpath,"subtable.csv"))
divTable = readTable (os.path.join (mpath,"divtable.csv"))
mulTable = readTable (os.path.join (mpath,"multable.csv"))



        
    
class  Value:
    def __init__(self,val):
        self._val = val
    
    def __str__(self):
        return  str(self._val)

    def __hash__ (self):
        if type(self._val) == bool:
            return hash(self._val)
        return self._val.value

    def __eq__ (self,oth):
        if oth == None:
            return False
        return  oth._val == self._val
    
    def getValue (self):
        return self._val

    def TriBool (self):
        return TriBool.Unknown
        
def concToSign (val):
    if val < 0:
        return SignValues.Neg
    elif val == 0:
        return SignValues.Zero
    elif val > 0:
        return SignValues.Plus
    
    
    
class ConstantCreator:
    def makeValue  (self,val, type):
        
        if fmteach.model.values.Types.Bool == type:
            return Value (False)
        else:
            return Value (concToSign (val))
        assert(False)
        
    def makeNonDet (self,type):
        return Value (SignValues.All)
    
class Operations:
    def Add (self,val1,val2):
        return Value (addTable[val1.getValue ()][val2.getValue ()])
    
    def Sub (self,val1,val2):
        return Value (addTable[val1.getValue ()][val2.getValue ()])
    
    
    def Div (self,val1,val2):
        return Value (addTable[val1.getValue ()][val2.getValue ()])
    
    
    def Mul (self,val1,val2):
        return Value (addTable[val1.getValue ()][val2.getValue ()])
    
    
    def Eq (self,val1,val2):
        return Value (False)
    
    def NEq (self,val1,val2):
        return Value (False)     

    def LEq (self,val1,val2):
        return Value (False)
        
    def GEq (self,val1,val2):
        return Value (False)
        
        
    def Lt (self,val1,val2):
        return Value (False)
                 

    def Gt (self,val1,val2):
        return Value (False) 

    def Negate (self,val1):
        return Value (False)
    
class CoverMerge:
    # Check if val1 is larger than val2
    def  Covers (self,val1,val2):
        if val1.getValue () == SignValues.All or val2.getValue () == SignValues.Bot:
            return True
        else:
            return val1.getValue () == val2.getValue ()

    #Merge Value1 and Value2
    # Maay return None if a merge is impossible
    def Merge (self,val1,val2):
        
        if val1.getValue () == val2.getValue ():
            return val1
        elif val1.getValue () == SignValues.Bot:
            return val2
        elif val2.getValue () == SignValues.Bot:
            return val1
        else:
            return Value(SignValues.All)
            
    

    

    
    
descr =  Descriptor (ConstantCreator (),Operations (),CoverMerge (),True)

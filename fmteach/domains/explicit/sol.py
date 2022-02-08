from fmteach.domains.domaindescription import *
import fmteach.model.values
import numpy

import  enum

class  Value:
    def __init__(self,val):
        self._val = val
    
    def __str__(self):
        return  str(self._val)

    def getValue (self):
        return self._val

    def TriBool (self):
        if self._val == 0:
            return TriBool.FF
        else:
            return TriBool.TT
        
    
    
class ConstantCreator:
    def makeValue  (self,val, type):
        if fmteach.model.values.Types.I8 == type:
            return Value (numpy.int8 (val))
        if fmteach.model.values.Types.I32 == type:
            return Value (numpy.int32 (val))
        if fmteach.model.values.Types.Pointer == type:
            return Value (numpy.int32 (val))
        if fmteach.model.values.Types.Bool == type:
            return Value (numpy.int8 (val))
        assert(False)

    def makeNonDet (self,type):
        return self.makeValue (10,type)
    
class Operations:
    def Add (self,val1,val2):
        return Value (val1.getValue () + val.getValue ())
    
    def Sub (self,val1,val2):
        return Value (val1.getValue () - val.getValue ())
    
    
    def Div (self,val1,val2):
        return Value (val1.getValue () / val.getValue ())
    
    
    def Mul (self,val1,val2):
        return Value (val1.getValue () * val.getValue ())
    
    
    def Eq (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        if v1 == v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
         
    def NEq (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        
        if v1 != v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
         

    def LEq (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        
        if v1 <= v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
         
    def GEq (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        
        if v1 >= v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
    
    def Lt (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        
        if v1 < v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
         

    def Gt (self,val1,val2):
        v1,v2 = val1.getValue (),val2.getValue ()
        
        if v1 > v2:
            return Value (numpy.int8(1))
        else:
             return Value (numpy.int8(0))
         

    def Negate (self,val1):
        if val1.getValue () == 0:
            return Value (numpy.int8(1))
        else:
            return Value (numpy.int8(0))
    
class CoverMerge:
    # Check if val1 is larger than val2
    def  Covers (self,val1,val2):
        return val1.getValue () == val2.getValue ()

    #Merge Value1 and Value2
    # Maay return None if a merge is impossible
    def Merge (self,val1,val2):
        if val1.getValue () == val2.getValue ():
            return val1
        else:
            None

    

    

    
    
descr =  Descriptor (ConstantCreator (),Operations (),CoverMerge (),False)

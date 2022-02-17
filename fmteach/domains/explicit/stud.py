from fmteach.domains.domaindescription import *
import fmteach.model.values
import numpy

import  enum

class ConstantCreator:
    def makeValue  (self,val, type):
        assert(False)

    def makeNonDet (self,type):
        assert(False)


class Operations:
    def Add (self,val1,val2):
        assert(False)

        
    def Sub (self,val1,val2):
        assert(False)
    
    def Div (self,val1,val2):
        assert(False)
    
    def Mul (self,val1,val2):
        assert(False)
    
    def Eq (self,val1,val2):
        assert(False)
        
    def NEq (self,val1,val2):
        assert(False)

    def LEq (self,val1,val2):
        assert(False)
        
    def GEq (self,val1,val2):
        assert(False)
        
    def Lt (self,val1,val2):
        assert(False)

    def Gt (self,val1,val2):
        assert(False)
    def Negate (self,val1):
        assert(False)

class CoverMerge:
    # Check if val1 is larger than val2    
    def  Covers (self,val1,val2):
        assert(False)
    #Merge Value1 and Value2
    # Maay return None if a merge is impossible
    def Merge (self,val1,val2):
        assert(False)


descr =  Descriptor (ConstantCreator (),Operations (),CoverMerge (),False)

    




    

    
    

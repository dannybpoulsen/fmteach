import fmteach.instructions
import fmteach.cfa
import fmteach.values


class Program:
    def __init__(self):
        self._registers = []
        self._cfas = fmteach.cfa.CFA ()

    def getCFA (self):
        return self._cfas

    def makeRegister (self,name = None,type = None):
        self._registers.append (fmteach.values.Regsiter (name or f"reg_{len(self._registers)}",
                                                         type or fmteach.values.Types.Integer)
                                
    
    def  getRegisters (self):
        return self._registers
    
    
    

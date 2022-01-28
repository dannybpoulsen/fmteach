import fmteach.model.instructions
import fmteach.model.cfa
import fmteach.model.values


class Program:
    def __init__(self):
        self._registers = {}
        self._cfas = fmteach.model.cfa.CFA ()

    def getCFA (self):
        return self._cfas

    def makeRegister (self,name = None,type = None):
        nn = name or f"reg_{len(self._registers)}"
        self._registers[nn]  = fmteach.model.values.Register (nn,   type or fmteach.model.values.Types.Integer,len(self._registers))
                                
        return self._registers[nn]
                             
    def  getRegisters (self):
        return self._registers.values ()
    
    
    def findRegister (self,name):
        return self._registers[name]



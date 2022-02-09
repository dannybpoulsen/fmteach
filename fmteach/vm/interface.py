import enum
import io
import fmteach.domains

class PathStatus(enum.Enum):
    Satis = 1
    Unknown = 2
    NSatis = 3
    
    
class State:
    def __init__ (self, values, loc,path = None):
        self._values = values
        self._loc = loc
        self._path = path
        
    def copy (self,nloc = None):
        return State (self._values.copy (),nloc or self._loc)

    def find (self,reg):
        assert reg.getId () < len(self._values), f"{reg.getId ()}, {len(self._values)}"
        return self._values[reg.getId ()]

    def set (self,reg,val):
        self._values[reg.getId ()] = val

    def getLoc (self):
        return self._loc

    def getValues (self):
        yield from self._values

    def __hash__ (self):
        return hash ((tuple(self._values),self._loc))

    def __str__ (self):
        s = ",".join ([str(v) for v in self._values])
        return self._loc.getName () +f"[{s}]"

    def __eq__(self,oth):
        return self._loc == oth._loc and self._values == oth._values

    def Assume (self,val):
        if val.TriBool () == fmteach.domains.TriBool.TT:
            return PathStatus.Satis
        elif val.TriBool () == fmteach.domains.TriBool.FF:
            return PathStatus.NSatis
        else:
            return PathStatus.Unknown
        
    def Assert (self,val):
        if val.TriBool () == fmteach.domains.TriBool.TT:
            return PathStatus.Satis
        elif val.TriBool () == fmteach.domains.TriBool.FF:
            return PathStatus.NSatis
        else:
            return PathStatus.Unknown

        
    @staticmethod
    def buildInitialState (prgm,domain):
        makeValue = domain.valueCreator ()
        regs = list(prgm.getRegisters ())
        values = [None]*len(regs)
        for f in regs:
            type = f.getType ()
            values[f.getId ()] = makeValue.makeValue (0,type)
        return State(values,prgm.getCFA ().getInitialLocation (),domain.initialPath ())



    

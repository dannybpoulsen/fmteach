import enum

class InstructionCode(enum.Enum):
    Add = 1
    Sub = 2
    Div = 3
    Mul = 4
    Eq = 5
    NEq = 6
    LEq = 7
    Lt = 8
    GEq = 9
    Gt = 10
    #
    NonDet = 11
    Assign = 12
    Assume = 13
    #
    Read = 16
    Store = 17
    #
    Skip = 19
    #
    Assert = 20
    
class Instruction:
    def __init__ (self,code = InstructionCode.Skip, operators = []):
        self._code = code
        self._operators = operators

    def getOpCode (self):
        return self._code

    def getOp (self,index):
        assert(len(self._operators <  index))
        return self._operators[index]

    def __str__(self):
        formatstr = None
        if self._code.value <= 10:
            formatstr = "{1} = {0} {2} {3}"
        elif self._code == InstructionCode.NonDet:
            formatstr = "{1} = {0}"
        elif self._code == InstructionCode.Assign or self._code == InstructionCode.Alloc:
            formatstr = "{1} = {2}"
        elif self._code == InstructionCode.Read:
            formatstr = "{1} = {0} {2}"
        elif self._code == InstructionCode.Store:
            formatstr = " {0} {2} @ {1}"
        elif self._code == InstructionCode.Bottom:
            formatstr = " {1} = {0}"
        elif self._code == InstructionCode.Skip:
            formatstr = "{0}"
        
        elif self._code == InstructionCode.Assume:
            formatstr = "{0}  {2}"
        elif self._code == InstructionCode.Assert:
            formatstr = "{0}  {2}"
        
        
        return formatstr.format (self._code.name,*self._operators)

import fmteach.ui

from fmteach.vm.interface import PathStatus

class VM:
    def __init__ (self,domain):
        self._valcreator = domain.valueCreator ()
        self._operations = domain.valueOperations ()

    def ExecuteInstructions(self,nstate,instr):
        def lookup (v):
            if v.isRegister():
                return nstate.find (v)
            else:
                return self._valcreator.makeValue(v.getValue (),v.getType ())

        for i in instr:
            op = i.getOpCode ()

            if op == fmteach.model.instructions.InstructionCode.Add:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Add (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Sub:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Sub (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Mul:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Mul (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Div:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Div (l,r))
            if op == fmteach.model.instructions.InstructionCode.Eq:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Eq (l,r))
            elif op == fmteach.model.instructions.InstructionCode.NEq:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.NEq (l,r))
            elif op == fmteach.model.instructions.InstructionCode.LEq:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.LEq (l,r))
            elif op == fmteach.model.instructions.InstructionCode.GEq:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.GEq (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Gt:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Gt (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Lt:
                res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
                nstate.set(res,self._operations.Lt (l,r))
            elif op == fmteach.model.instructions.InstructionCode.Assign:
                res,l = i.getOp (0),lookup(i.getOp(1))
                nstate.set(res,l)
            elif op == fmteach.model.instructions.InstructionCode.NonDet:
                res = i.getOp(0)
                val = self._valcreator.makeNonDet (res.getType ())
                nstate.set(res,val)
                
            elif op == fmteach.model.instructions.InstructionCode.Assume:
                ass = lookup(i.getOp(0))
                res = nstate.Assume (ass)
                if res == PathStatus.NSatis:
                    return False

            elif op == fmteach.model.instructions.InstructionCode.NegAssume:
                ass = lookup(i.getOp(0))
                res = nstate.Assume(self._operations.Negate (ass))
                if res == PathStatus.NSatis:
                    return False

                
        return True
    

    

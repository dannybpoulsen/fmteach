import io
import fmteach.ui
import fmteach.model.values
import fmteach.model.instructions

import numpy
import graphviz


class State:
    def __init__ (self, values, loc):
        self._values = values
        self._loc = loc

    def copy (self,nloc = None):
        return State (self._values.copy (),nloc or self._loc)

    def find (self,reg):
        return self._values[reg.getId ()]

    def set (self,reg,val):
        self._values[reg.getId ()] = val

    def getLoc (self):
        return self._loc
    
    def __hash__ (self):
        return hash ((tuple(self._values),self._loc))
    
    @staticmethod
    def buildInitialState (prgm):
        regs = list(prgm.getRegisters ())
        values = [None]*len(regs)
        for f in regs:
            type = f.getType ()
            if fmteach.model.values.Types.I8 == type:
                values[f.getId ()] =(numpy.int8 (0))
            if fmteach.model.values.Types.I32 == type:
                values[f.getId ()]= (numpy.int32 (0))
            if fmteach.model.values.Types.Pointer == type:
                values[f.getId ()] =  (numpy.int32 (0))
            if fmteach.model.values.Types.Bool == type:
                values[f.getId ()] = (numpy.bool (False))
        return State(values,prgm.getCFA ().getInitialLocation ())


class LookupValue:
    def __init__(self,state):
        self._state = state


def executeInstructionSequence (nstate,instrs):
    def lookup (v):
        if v.isRegister():
            return nstate.find (v)
        else:
            return v.getValue ()

    for i in instrs:
        op = i.getOpCode ()
        
        if op == fmteach.model.instructions.InstructionCode.Add:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l+r)
        elif op == fmteach.model.instructions.InstructionCode.Sub:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l-r)
        elif op == fmteach.model.instructions.InstructionCode.Mul:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l*r)
        elif op == fmteach.model.instructions.InstructionCode.Div:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l/r)
        if op == fmteach.model.instructions.InstructionCode.Eq:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l==r)
        elif op == fmteach.model.instructions.InstructionCode.NEq:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l!=r)
        elif op == fmteach.model.instructions.InstructionCode.LEq:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l<=r)
        elif op == fmteach.model.instructions.InstructionCode.GEq:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l>=r)
        elif op == fmteach.model.instructions.InstructionCode.Gt:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l>r)
        elif op == fmteach.model.instructions.InstructionCode.Lt:
            res,l,r = i.getOp (0),lookup(i.getOp(1)),lookup(i.getOp(2))
            nstate.set(res,l<r)
        elif op == fmteach.model.instructions.InstructionCode.Assign:
            res,l = i.getOp (0),lookup(i.getOp(1))
            nstate.set(res,l)
        
        elif op == fmteach.model.instructions.InstructionCode.Assume:
            ass = lookup(i.getOp(0))
            if not ass:
                return False

        elif op == fmteach.model.instructions.InstructionCode.NegAssume:
            ass = lookup(i.getOp(0))
            if (ass):
                return False
        
        
        
    return True
    
        
def constructLabel (edge):
    ss = io.StringIO ()
    for i in edge.instructions ():
        ss.write (str(i))
    return ss.getvalue ()

def run_sol (whlan):
    compiler = fmteach.whlang.compiler.ExplicitCompiler ()
    prgm  = compiler.BuildProgram (whlan)
    
    
    fmteach.ui.messages.message ("Initiating CFA2DOT")
    
    dot = graphviz.Digraph('CFA') 
    cfa = prgm.getCFA ()
    initial = State.buildInitialState (prgm)
    visited = set()
    waiting = [initial]
    visited.add(initial)
    
    while len(waiting) > 0:
        
        state = waiting.pop ()
        loc = state.getLoc ()
        dot.node (str(state))
        
        for e in cfa.getEdgesFrom (loc):
            to = e.getTo ()
            nstate = state.copy (to)
            dot.node (str(nstate))
            if executeInstructionSequence (nstate,e.instructions ()):
                label = constructLabel (e)
                dot.edge (str(state),str(nstate),label = label)
            
                if nstate not in visited:
                    waiting.append (nstate)
                    visited.add (nstate)
    dot.view ()    
        
    
    fmteach.ui.messages.message ("Done")

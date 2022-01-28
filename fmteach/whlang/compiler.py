import fmteach.ui
import fmteach.model.values
import fmteach.model.program

class Compiler:
    def BuildProgram (self,ast):
        self._program = fmteach.model.program.Program ()
        ast.visit (self)
        self._program.getCFA ().setInitialLocation (self._start)
        return self._program
    
    def visitProgram (self,program):
        for vd in program.getVarDec ():
            vd.visit (self) 
        program.getStmt ().visit (self)
        
        
    def visitVarDeclaration (self,vd):
        self._program.makeRegister (vd.getName().getName(),vd.getType ())
        self._instrs = []
        

    def visitExprConstant (self,constant):
        self._expr = fmteach.model.values.IntegerConstant (constant.getValue (),constant.getType ())
        self._instrs = []
        
        
    def visitExprVariable (self,variable):
        self._expr = self._program.findRegister (variable.getName ())
        self._instrs = []
        
        
    
    def visitExprBinary (self,binop):
        left =  binop.getLeft ()
        right = binop.getRight ()
        instrs = []
        
        for l in [left,right]:
            l.visit (self)
            l._expr = self._expr
            instrs = instrs+ self._instrs
            
            
        nvar = self._program.makeRegister (None,binop.getType ())
        
        ninst = None

        op = binop.getOp ()
        if op == fmteach.whlang.nodes.BinOp.Add:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Add,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Sub:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Sub,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Div:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Div,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Mul:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Mul,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Eq:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Eq,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.NEq:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.NEq,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.LEq:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.LEq,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Lt:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Lt,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.GEq:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.GEq,[nvar,left._expr,right._expr])
        elif op == fmteach.whlang.nodes.BinOp.Gt:
            ninst = fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Gt,[nvar,left._expr,right._expr])

        instrs.append(ninst)
        self._instrs = instrs
        self._expr = nvar
        
        
    def visitStmtAssign (self,assign):
        startloc = self._program.getCFA().makeLocation ()
        endloc = self._program.getCFA().makeLocation ()
        assign.getExpression ().visit(self)
        reg = self._program.findRegister (assign.getVariable ().getName ())
        instrs = self._instrs + [fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Assign,[reg,self._expr])]
        self._program.getCFA ().makeEdge (startloc,endloc,instrs)
        self._start = startloc
        self._end = endloc
        
    def visitStmtNonDet (self,nondet):
        startloc = self._program.getCFA().makeLocation ()
        endloc = self._program.getCFA().makeLocation ()
        reg = self._program.findRegister (nondet.getVariable ().getName ())
        instrs = self._instrs + [fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.NonDet,[reg])]
        self._program.getCFA ().makeEdge (startloc,endloc,instrs)
        self._start = startloc
        self._end = endloc
        
        
    def visitStmtSequence (self,sequence):
        cfa = self._program.getCFA ()
        start = cfa.makeLocation ()
        end = cfa.makeLocation ()
        
        prev = start
        for s in sequence.getStatements ():
            s.visit (self)
            cfa.makeEdge (prev,self._start,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])
            prev  = self._end
        cfa.makeEdge (prev,end,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])
        self._start = start
        self._end = end
            
    def visitStmtIf (self,iff):
        cfa = self._program.getCFA ()
        start = cfa.makeLocation ()
        condcheck = cfa.makeLocation ()
        end = cfa.makeLocation ()
        
        iff.getCondition ().visit (self)
        condition = self._expr
        cfa.makeEdge (start,condcheck,self._instrs)
        
        
        iff.getIfBranch ().visit (self)

        cfa.makeEdge (condcheck,self._start,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Assume,[condition])])
        cfa.makeEdge (self._end,end,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])
        
        iff.getElseBranch ().visit (self)
        cfa.makeEdge (condcheck,self._start,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.NegAssume,[condition])])
        cfa.makeEdge (self._end,end,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])
        
        
        
        self._start = start
        self._end = end
        

    def visitStmtWhile (self,whilee):
        cfa = self._program.getCFA ()
        start = cfa.makeLocation ()
        condcheck = cfa.makeLocation ()
        end = cfa.makeLocation ()
        
        
        whilee.getCondition ().visit (self)
        condition = self._expr
        cfa.makeEdge (start,condcheck,self._instrs)
        
        whilee.getStatement ().visit (self)
        
        cfa.makeEdge (condcheck,self._start,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Assume,[condition])])
        cfa.makeEdge (self._end,start,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])
        
        cfa.makeEdge (condcheck,end,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.NegAssume,[condition])])
        
        
        
        self._start = start
        self._end = end
        

    def visitStmtSkip (self,skip):
        cfa = self._program.getCFA ()
        self._start = cfa.makeLocation ()
        self._end = cfa.makeLocation ()
        cfa.makeEdge (self._start,self._end,[fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Skip,[])])




class ExplicitCompiler (Compiler):
     def visitStmtNonDet (self,nondet):
        startloc = self._program.getCFA().makeLocation ()
        endloc = self._program.getCFA().makeLocation ()

        max = 0
        if nondet.getVariable().getType () == fmteach.model.values.Types.I8 or nondet.getVariable().getType () == fmteach.model.values.Types.Bool:
            max = (1 << 8)
        elif nondet.getVariable().getType () == fmteach.model.values.Types.I32 or nondet.getVariable().getType () == fmteach.model.values.Types.Pointer:
            max = (1 << 32)
        reg = self._program.findRegister (nondet.getVariable ().getName ())
        
        for i in range(0,max):
            instrs = self._instrs + [fmteach.model.instructions.Instruction (fmteach.model.instructions.InstructionCode.Assign,[reg,fmteach.model.values.IntegerConstant (i,nondet.getVariable().getType ())])]
            self._program.getCFA ().makeEdge (startloc,endloc,instrs)
        self._start = startloc
        self._end = endloc
        
      

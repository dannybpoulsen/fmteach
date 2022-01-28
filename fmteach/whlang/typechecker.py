import fmteach.ui
import fmteach.model.values

class Typechecker:
    def Check (self,ast):
        self._variables = {}
        self._ok = True
        ast.visit (self)
        return self._ok
    
    def visitProgram (self,program):
        for vd in program.getVarDec ():
            vd.visit (self)
            if not self._ok:
                return 
        program.getStmt ().visit (self)
        
        
    def visitVarDeclaration (self,vd):
        if vd.getName ().getName () in self._variables:
            fmteach.ui.messages.error (f"On {vd.getLocation ()} --- {vd.getName ()} already defined")
            self._ok = False
        else:
            self._variables[vd.getName ().getName ()] = vd.getType ()
    

    def visitExprConstant (self,constant):
        pass
    
    def visitExprVariable (self,variable):
        if variable.getName () not in self._variables:
            fmteach.messages.error (f"On {vd.getLocation ()} --- {vd.getName ()} not defined")
            self._ok = False
        else:
            variable.setType (self._variables.get(variable.getName (),None))

    
    def visitExprBinary (self,binop):
        left =  binop.getLeft ()
        right = binop.getRight ()

        for l in [left,right]:
            l.visit (self)
        
        if left.getType () != right.getType ():
            fmteach.ui.messages.error (f"On {binop.getLocation ()} --- Arithmetic expressions must have same type")
            self._ok = False

        if binop.getOp ().value  <= 4:
            binop.setType (left.getType ())
        else:
            binop.setType (fmteach.model.values.Types.Bool)
        
    
    def visitStmtAssign (self,assign):
        if assign.getVariable ().getName () not in self._variables:
            fmteach.ui.messages.error (f"On {assign.getLocation ()} --- {assign.getVariable ().getName ()} not defined")
            self._ok = False
        assign.getExpression ().visit(self)
        if assign.getExpression ().getType () != self._variables.get(assign.getVariable ().getName (),None):
            fmteach.ui.messages.error (f"Must have same type")
            self._ok = False
    
    def visitStmtNonDet (self,nondet):
        nondet.getVariable ().visit (self);            
    
    def visitStmtSequence (self,sequence):
        for s in sequence.getStatements ():
            s.visit (self)
        
    def visitStmtIf (self,iff):
        iff.getCondition ().visit (self)
        iff.getIfBranch ().visit (self)
        iff.getElseBranch ().visit (self)

        if iff.getCondition ().getType () != fmteach.model.values.Types.Bool:
            fmteach.ui.messages.error (f"Must be bool")
            self._ok = False
        
        

    def visitStmtWhile (self,whilee):
        whilee.getCondition ().visit (self)
        whilee.getStatement ().visit (self)
        
        if whilee.getCondition ().getType () != fmteach.model.values.Types.Bool:
            fmteach.ui.messages.error (f"Must be bool")
            self._ok = False
        

    def visitStmtSkip (self,skip):
        pass

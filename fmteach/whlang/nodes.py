
import enum

class Location:
    def __init__(self,filename,line,col):
        self._filename = filename
        self._line = line
        self._col = col

    def __str__(self):
        return f"s{self._filename}:{self._line}-{self._col}"

class Node:
    def __init__ (self,startloc):
        self._start =startloc
    
    def visit (self,visitor):
        raise RuntimeError ("No visitor function implemented")

    def getLocation (self):
        return self._start
    
class Program (Node):
    def __init__ (self,vardec,stmt,startloc):
        super ().__init__(startloc)
        self._vardec = vardec
        self._stmt = stmt
    
    def visit (self,v):
        v.visitProgram (self)

    def getVarDec (self):
        return self._vardec

    def getStmt (self):
        return self._stmt

    
    
class VarDeclaration (Node):
    def __init__(self,name,type,startloc):
        super().__init__(startloc)
        self._name = name
        self._type = type
        
    def getName (self):
        return self._name

    def getType (self):
        return self._type

    def visit (self,v):
        v.visitVarDeclaration (self)

    def __str__(self):
        return f"{self._type.name} {self._name}"


class Expression(Node):
    def __init__(self,startloc,type = None):
        super ().__init__ (startloc)
        self._type = type
    
    def getType (self):
        return self._type
    
    def setType (self,t):
        self._type = t
    
class ExprConstant(Expression):
    def __init__(self,val,type,startloc):
        super().__init__(startloc,type)
        self._val = val

    def visit (self,v):
        v.visitExprConstant (self)
        
    def getValue (self):
        return self._val

class ExprVariable(Expression):
    def __init__(self,name,startloc):
        super().__init__(startloc)
        self._name = name

    def visit (self,v):
        v.visitExprVariable (self)
        
    def getName (self):
        return self._name

        
    
class BinOp(enum.Enum):
    Add = 1
    Div = 2
    Mul = 3
    Sub = 4
    LEq = 5
    GEq = 6
    Lt = 7
    Gt = 8
    Eq = 9
    NEq = 10
    

class ExprBinary(Expression):
    def __init__(self,left,right,op,startloc):
        super().__init__(startloc)
        self._left = left
        self._right = right
        self._op = op
        
    def getLeft (self):
        return self._left
    

    def getRight (self):
        return self._right

    def getOp (self):
        return self._op
    
    def visit (self,v):
        v.visitExprBinary (self)
        

class StmtSkip (Node):
    def __init__ (self,loc):
        super().__init__(loc)

    def visit (self,v):
        v.visitStmtSkip (self)
        
    
class StmtAssign (Node):
    def __init__ (self,variable,expr,loc):
        super().__init__(loc)
        self._var = variable
        self._expr = expr

    def visit (self,v):
        v.visitStmtAssign (self)
        
    def getVariable (self):
        return self._var

    def getExpression (self):
        return self._expr

class StmtNonDet (Node):
    def __init__ (self,variable,loc):
        super().__init__(loc)
        self._var = variable
        
    def visit (self,v):
        v.visitStmtNonDet (self)
        
    def getVariable (self):
        return self._var

    
class StmtSequence (Node):
    def __init__(self,stmts,loc):
        super().__init__(loc)
        self._stmts = stmts

    def visit (self,v):
        v.visitStmtSequence (self)
        
    def getStatements (self):
        return self._stmts


class StmtIf (Node):
    def __init__(self,cond,stmt,estmt,loc):
        super().__init__(loc)
        self._cond = cond
        self._stmt = stmt
        self._else = estmt

    def visit (self,v):
        v.visitStmtIf (self)

    def getCondition (self):
        return self._cond

    def getIfBranch (self):
        return self._stmt

    def getElseBranch (self):
        return self._else
    
        
class StmtWhile (Node):
    def __init__(self,cond,stmt,loc):
        super().__init__(loc)
        self._cond = cond
        self._stmt = stmt


    def visit (self,v):
        v.visitStmtWhile (self)

    def getCondition (self):
        return self._cond

    def getStatement (self):
        return self._stmt
        


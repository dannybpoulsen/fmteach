import enum

class Location:
    def __init__(self,filename,line,col):
        self._filename = filename
        self._line = line
        self._col = col


class Node:
    def __init__ (self,startloc):
        self._start =startloc

    def accept (self,visitor):
        raise RuntimeError ("No visitor function implemented")

class VarDeclaration (Node):
    def __init__(self,name,type,startloc):
        super().__init__(startloc)
        self._name = name
        self._type = type
        
    def getName (self):
        return self._name

    def getType (self):
        return self._type

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
    

class StmtAssign (Node):
    def __init__ (self,variable,expr,loc):
        super().__init__(loc)
        self._var = variable
        self._expr = expr

class StmtSequence (Node):
    def __init__(self,stmts,loc):
        super().__init__(loc)
        self._stmts = stmts


class StmtIf (Node):
    def __init__(self,cond,stmt,estmt,loc):
        super().__init__(loc)
        self._cond = cond
        self._stmt = stmt
        self._else = estmt

class StmtWhile (Node):
    def __init__(self,cond,stmt,loc):
        super().__init__(loc)
        self._cond = cond
        self._stmt = stmt




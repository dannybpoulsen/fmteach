import pyparsing as pp

import fmteach.whlang.nodes
import fmteach.model.values
import fmteach.ui


class Parser:

    def __init__(self):
        name = pp.Regex (r"[a-z]+").setParseAction (lambda  s,l,t: t[0])
        vardec = self.varDeclarationParser (name)
        expr = self.expressionParser (name)
            
        prgm = (vardec + self.stmtParser (name,expr)).setParseAction (lambda s,l,t: fmteach.whlang.nodes.Program (t[0],t[1],fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))) )
        self._parser = prgm 
        
        
    def ParseString (self,inp):
        self._filename = "str"
        try:
            return  self._parser.parseString (inp,parseAll = True)[0]
        except pp.ParseException as p:
            fmteach.ui.messages.error (str(p))
            return None


    def stmtParser (self,name,expr):
        seq = pp.Forward ()
        assign = (name + pp.Literal (":=") + expr).setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtAssign (t[0],t[2],fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        nondet = (name + pp.Literal (":=") + pp.Literal ("NonDet")).setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtNonDet (t[0],fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
    
        iff = (pp.Literal ("If") + expr + seq +  pp.Literal ("Else") + seq).setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtIf (t[1],t[2],t[4],fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        whilee = (pp.Literal ("While") + expr + seq).setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtWhile (t[1],t[2],fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))        
        skip = (pp.Literal ("Skip")).setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtSkip (fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        stmt = (iff | whilee | assign | nondet | skip).setParseAction (lambda s,l,t: t[0])
        seq << (pp.Literal ("{") +  pp.delimitedList (stmt, ";") + pp.Literal ("}")  )
        return  seq.setParseAction (lambda s,l,t: fmteach.whlang.nodes.StmtSequence(t[1:-1],
                                                                                    fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        
        
    def expressionParser (self,name):
        expr = pp.Forward ()
        
        i8 = pp.Regex (r"[0-9]+i8").setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprConstant (int(t[0].replace("i8","")),
                                                                                                       fmteach.model.values.Types.I8,
                                                                                                     fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        i32 = pp.Regex (r"[0-9]+i32").setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprConstant (int(t[0].replace("i32","")),
                                                                                                       fmteach.model.values.Types.I32,
                                                                                                       fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        addr = pp.Regex (r"[0-9]+a").setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprConstant (int(t[0].replace("a","")),
                                                                                                      fmteach.model.values.Types.Pointer,
                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        paran = (pp.Literal ('(') + expr + pp.Literal (')')).setParseAction (lambda s,l,t: t[0])
        
        LEq = (pp.Literal ('(') + expr + pp.Literal ("<=") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.LEq,
                                                                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        GEq = (pp.Literal ('(') + expr + pp.Literal (">=") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.GEq,
                                                                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        Gt = (pp.Literal ('(') + expr + pp.Literal (">") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.Gt,
                                                                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        Lt = (pp.Literal ('(') + expr + pp.Literal ("<") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.Lt,
                                                                                                                                                    fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        Eq = (pp.Literal ('(') + expr + pp.Literal ("==") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.Eq,
                                                                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        
        NEq = (pp.Literal ('(') + expr + pp.Literal ("!=") + expr +  pp.Literal (')')).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[1],
                                                                                                                                                      t[3],
                                                                                                                                                      fmteach.whlang.nodes.BinOp.NEq,
                                                                                                                                                      fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        
        
        factor = GEq | Gt | Lt | Eq | NEq | LEq | paran | i8 | i32 | addr | name.setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprVariable (t[0],
                                                                                                                   fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        mul = (factor + pp.Literal ("*") + factor).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[0],
                                                                                                                  t[2],
                                                                                                                   fmteach.whlang.nodes.BinOp.Mul,
                                                                                                                   fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        div = (factor + pp.Literal ("/") + factor).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[0],
                                                                                                                   t[2],
                                                                                                                   fmteach.whlang.nodes.BinOp.Div,
                                                                                                                    fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        
        
        term =  mul |  div  | factor
        
        
        add = (term  + pp.Literal ("+") + term).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[0],
                                                                                                                   t[2],
                                                                                                                   fmteach.whlang.nodes.BinOp.Add,
                                                                                                                   fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))

        sub = (term + pp.Literal ("-") + term).setParseAction (lambda s,l,t: fmteach.whlang.nodes.ExprBinary (t[0],
                                                                                                                   t[2],
                                                                                                                   fmteach.whlang.nodes.BinOp.Sub,
                                                                                                                    fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))))
        
        
        
        
        return (expr << (add | sub | term))
                                                                                                            
        
                                                                                                    
        
    def varDeclarationParser (self,name):
        boolean = (pp.Literal ("Bool")+name).setParseAction (lambda s,l,t: fmteach.whlang.nodes.VarDeclaration (t[1],
                                                                                                         fmteach.model.values.Types.Bool,
                                                                                                         fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))
                                                                                                         ))
        int8 = (pp.Literal ("I8")+name).setParseAction (lambda s,l,t: fmteach.whlang.nodes.VarDeclaration (t[1],
                                                                                                         fmteach.model.values.Types.I8,
                                                                                                         fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))
                                                                                                         ))

        int32 = (pp.Literal ("I32")+name).setParseAction (lambda s,l,t: fmteach.whlang.nodes.VarDeclaration (t[1],
                                                                                                         fmteach.model.values.Types.I32,
                                                                                                         fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))
                                                                                                         ))

        pointer = (pp.Literal ("Addr")+name).setParseAction (lambda s,l,t: fmteach.whlang.nodes.VarDeclaration (t[1],
                                                                                                         fmteach.model.values.Types.Pointer,
                                                                                                         fmteach.whlang.nodes.Location (self._filename,pp.lineno(l,s),pp.col(l,s))
                                                                                                         ))

        

        
        return pp.delimitedList((boolean  | int8 | int32 | pointer), delim=";").setParseAction (lambda s,l,t: [t])
    


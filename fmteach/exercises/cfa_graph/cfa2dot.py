import fmteach.whlang.compiler
import fmteach.ui 
import graphviz


def run (whlan):
    compiler = fmteach.whlang.compiler.Compiler ()
    model  = compiler.BuildProgram (whlan)

    dot = graphviz.Digraph('CFA') 
    
    
    fmteach.ui.messages.message ("Initiating CFA2DOT")

    fmteach.ui.messages.error (f"This ({__file__}) is where you should add your algorithm ")
    
    fmteach.ui.messages.message ("Done")

    dot.view ()    
    

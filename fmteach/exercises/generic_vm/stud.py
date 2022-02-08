import fmteach.whlang.compiler
import fmteach.ui 

def run (whlan,domain):
    compiler = fmteach.whlang.compiler.Compiler ()
    model  = compiler.BuildProgram (whlan)
        
    fmteach.ui.messages.message ("Initiating CFA2DOT")

    fmteach.ui.messages.error (f"This ({__file__}) is where you should add your algorithm ")

    fmteach.ui.messages.message ("Done")


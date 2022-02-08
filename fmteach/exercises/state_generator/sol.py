import io
import fmteach.ui
import fmteach.domains
import fmteach.vm.sol
import fmteach.vm.interface
import fmteach.reach



def run_sol (whlan,domain,engine,genstates):

    if domain.hasNonDet ():
        compiler = fmteach.whlang.compiler.Compiler ()
    else:
        compiler = fmteach.whlang.compiler.ExplicitCompiler ()
        
    prgm  = compiler.BuildProgram (whlan)
    
    
    
    fmteach.ui.messages.message ("Initiating State Generation")
    initial = fmteach.vm.interface.State.buildInitialState (prgm,domain)
    
    for s in genstates (initial,prgm.getCFA(),engine,domain):
        fmteach.ui.messages.message (str(s))
        
        
    fmteach.ui.messages.message ("Done")

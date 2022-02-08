import io
import fmteach.ui
import fmteach.domains
import fmteach.vm.sol
import fmteach.vm.interface

import graphviz

def constructLabel (edge):
    ss = io.StringIO ()
    for i in edge.instructions ():
        ss.write (str(i))
    return ss.getvalue ()

def run_sol (whlan,domain):
    engine  = fmteach.vm.sol.VM (domain)
    
    compiler = fmteach.whlang.compiler.Compiler ()
    prgm  = compiler.BuildProgram (whlan)
    
    
    
    fmteach.ui.messages.message ("Initiating CFA2DOT")
    
    dot = graphviz.Digraph('CFA') 
    cfa = prgm.getCFA ()
    initial = fmteach.vm.interface.State.buildInitialState (prgm,domain)
    visited = set()
    
    waiting = [initial]
    visited.add(initial)

    while (len(waiting) > 0):
        state = waiting.pop  ()
        dot.node (str(hash(state)), label = str(state))
        loc = state.getLoc ()
        for e in cfa.getEdgesFrom (loc):
            to = e.getTo ()
            nstate = state.copy (to)
            
            if engine.ExecuteInstructions (nstate,e.instructions ()):
                dot.node (str(hash(nstate)),label = str(nstate))
            
                label = constructLabel (e)
                dot.edge (str(hash(state)),str(hash(nstate)),label = label)            
                if nstate not in visited:
                    waiting.append (nstate)
                    visited.add (nstate)
    
    dot.view ()    
        
    
    fmteach.ui.messages.message ("Done")

import io
import fmteach.ui 
import graphviz

def constructLabel (edge):
    ss = io.StringIO ()
    for i in edge.instructions ():
        ss.write (str(i))
    return ss.getvalue ()

def run_sol (whlan):
    compiler = fmteach.whlang.compiler.Compiler ()
    prgm  = compiler.BuildProgram (whlan)
    

    fmteach.ui.messages.message ("Initiating CFA2DOT")
    
    dot = graphviz.Digraph('CFA') 
    cfa = prgm.getCFA ()
    initial = cfa.getInitialLocation ()
    visited = set()
    waiting = [initial]
    visited.add(initial)
    
    while len(waiting) > 0:
        
        loc = waiting.pop ()
        dot.node (str(loc),label=loc.getName ())
        
        for e in cfa.getEdgesFrom (loc):
            to = e.getTo ()
            dot.node (str(to),label=to.getName ())
            
            label = constructLabel (e)
            dot.edge (str(loc),str(to),label = label)
            
            if to not in visited:
                waiting.append (to)
                visited.add (to)
    
    dot.view ()    
        
    
    fmteach.ui.messages.message ("Done")

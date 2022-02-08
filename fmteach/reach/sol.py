import fmteach.reach.pw

def generateStates (state,cfa,engine,domain):
    passed = fmteach.reach.pw.PWSol (domain.valueCoverMerge())
    passed.insert (state)
    while (passed.hasWaiting ()):
        state =passed.pull  ()
        loc = state.getLoc ()
        for e in cfa.getEdgesFrom (loc):
            to = e.getTo ()
            nstate = state.copy (to)
            if engine.ExecuteInstructions (nstate,e.instructions ()):
                passed.insert (nstate)

    yield from passed.getStates ()
            

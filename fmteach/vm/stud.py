import fmteach.ui



class VM:
    def __init__ (self,domain):
        self._valcreator = domain.valueCreator ()
        self._operations = domain.valueOperations ()
        
    def ExecuteInstructions(self,nstate,instr,pathcontrol,predcontrol):
        fmteach.ui.messages.error (f"This ({__file__}) is where you should add your VM implementation")
    

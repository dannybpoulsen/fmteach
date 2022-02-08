import  os
import fmteach.exercises.descriptor
import fmteach.domains
import fmteach.vm.sol
import fmteach.vm.stud
import fmteach.reach


from fmteach.exercises.state_generator.sol import *


class ExerciseDescr (fmteach.exercises.descriptor.ExerciseDescriptor):
    def __init__ (self,name,readmefile,call,solcall):
        super ().__init__(name,readmefile,call,solcall)
        
    def addToParser (self,parser):
        domains = list(fmteach.domains.domainnames())
        subp = parser.add_parser (self._name)
        subp.add_argument ("--readme",dest="readme",action="store_true")
        subp.add_argument ("--solution",dest="solution",action="store_true")
        subp.add_argument ("--domain",default=domains[0],dest="domain",choices = domains)
        
        
        subp.set_defaults (func=self)

    def __call__ (self,args,model):
        if args.solution:            
            domains =  fmteach.domains.soldomains
            domain = domains [args.domain]
            engine = fmteach.vm.sol.VM (domain)
            genstates = fmteach.reach.genStatesSol 
            
        else:
            domains =  fmteach.domains.studdomains
            domain = domains [args.domain]
            engine = fmteach.vm.stud.VM (domain)
            genstates = fmteach.reach.genStatesStud
        
        if args.readme:
            with open(self._readmefile,'r') as ff:
                print (ff.read ())
        elif args.solution:
            self._solcall (model,domain,engine,genstates)
    
        else:
            self._call (model,domain,engine,genstates)
            


path = os.path.join (os.path.split(os.path.abspath(__file__))[0],"README.md")
descr = ExerciseDescr ("StateGenerator",path,run_sol,run_sol)


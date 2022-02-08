import  os
import fmteach.exercises.descriptor
import fmteach.domains

from fmteach.exercises.generic_vm.stud import *
from fmteach.exercises.generic_vm.sol import *


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
        else:
            domains =  fmteach.domains.studdomains
        domain = domains [args.domain]
        if args.readme:
            self.showReadme ()
        elif args.solution:
            self._solcall (model,domain)
    
        else:
            self._call (model,domain)



path = os.path.join (os.path.split(os.path.abspath(__file__))[0],"README.md")
descr = ExerciseDescr ("GenericVM",path,run,run_sol)


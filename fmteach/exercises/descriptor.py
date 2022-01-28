class ExerciseDescriptor:
    def __init__ (self,name,readmefile,call,solcall):
        self._name = name
        self._readmefile = readmefile
        self._call = call
        self._solcall = solcall
        
    def addToParser (self,parser):
        subp = parser.add_parser (self._name)
        subp.add_argument ("--readme",dest="readme",action="store_true")
        subp.add_argument ("--solution",dest="solution",action="store_true")
        
        subp.set_defaults (func=self)

    def __call__ (self,args,model):
        if args.readme:
            with open(self._readmefile,'r') as ff:
                print (ff.read ())
        elif args.solution:
            self._solcall (model)
    
        else:
            self._call (model)
    
    

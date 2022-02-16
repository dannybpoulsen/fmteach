# Generic VM  

If we continue our exploration of formal methods we very quickly end
up implementing somethings constantly:   
- A worklist algorithm,  
- a "VM" loop over all the instructions in our program.   
	
In this exercise we will implement a "generic" (in
__fmteacah/vm/interface.py__ )  VM that can be
"plugged" into a worklist algorithm. The VM should  only require  that 
- the state it is given implements the StateInterface in
  __fmteacah/vm/interface.py__

- That the __domain__ constructor parameter implements the interface
  in __fmteach/domains/dummy/sol.py__ . In the domains folder we will
  implement the different domains/value representation you see throughout the course. 

-

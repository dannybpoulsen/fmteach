# State Generator

In this exercise we continue our development of a generic formal methods framework. In particular, 
- we will add an implementation of a PassedWaiting-List --- that is a structure that integrates the passed-list and waiting set into one. Your implementation should be added to __fmteach/reach/pw/stud.py__ 
- we will add an algorithm for enumerating all reachable states. This algorithm should use the VM from the exerciseand your newly implemented passed-waiting list. Your implementation should be added to __fmteach/reach/stud.py__. 

-- Once you have your PassedWaitingList implemented and the state space enumeration implemented. Then you can start adding your implementation of the domains (sign/explicit) we discussed (in __fmteach/domains/NAME/stud.py__)
	- For the sign domain you are allowed to only implement it for the mathematical operators and not for Booleans

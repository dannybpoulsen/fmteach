

# Explicit State Space Enumeration  

In this exercise you will implement  an algorithm for counting the
number of explicit states in  a program. You can probably reuse most
of the code from the ExplicitGraph exercises.

- After implementing the state space counter you should experiment
  with modifying the programs in the programs-folder (add extra
  NonDeterministic value, add more brances etc). Try to see if you can
  predict how much the state space increase with the changes you make.

- The while-compiler in _fmteach/whlang/compiler'_ annotates some locations as 'Avoid'--- those reached after violating an assert. On a location, you can check this annotation with getAttr (). Modify your State space counter to also count the number of states that are in a bad location 


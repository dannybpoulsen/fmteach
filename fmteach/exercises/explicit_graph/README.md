

# Explicit State Space Graph  

In this exercise we will  create a graphical view of the
explicit state graph of our program. Like in the previus exercise a
template for your solution is available in
__fmteach/exercises/cfa2dot.py__.  

For solving this exercise you will need to
- Create your own (or find a proper)  representation of values 
  - Python integers are not  applicable as they have infinite
    biwidth and thus does not capture the overflow semantics of finite
    width bitvectors. Consider using numpy bitvectors ;-)
	
- create your own representation of a state. All registers in a program
  has a unique id (starting from zero) thus you can store all
  variable assignments in a list and use a variables id  to access the
  value of thaat variable in a given state. 
  
- Create a function (transfer) that takes a state and a list of instructions as
  parameters. It should update the state according to that sequence of
  instructions. 
  
- Have a method for copying states, and a method for checking whether
  two states are equivalent. 

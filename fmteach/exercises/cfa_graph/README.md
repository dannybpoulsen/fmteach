# Create a Graphical View of  The Compiled Program

In this exercise you are asked to write code that produces a graphical
over view of the CFA (Control-Flow-automaton) of a compiled
program. The file __fmteach/exercises/cfa_graph/cfa2dot__ already has
to core setup ready i.e. the  program has been compiled and available
in the variable __model__. 

- For showing the graph it is recommended to use the graphviz library
- You should use a worklist algorithm for iterating over all locations
  of the program
  - Python  has list and set construction data structures
	that you can use for representing the __waiting__ and __passed__
	list of the worklist algorithm

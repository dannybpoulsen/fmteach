import  os
import fmteach.exercises.descriptor
from fmteach.exercises.explicit_graph.cfa2dot import *
from fmteach.exercises.explicit_graph.cfa2dot_sol import *



path = os.path.join (os.path.split(os.path.abspath(__file__))[0],"README.md")
descr = fmteach.exercises.descriptor.ExerciseDescriptor ("ExplicitGraph",path,run,run_sol)


import  os
import fmteach.exercises.descriptor
from fmteach.exercises.enum_explicit.enum import *
from fmteach.exercises.enum_explicit.enum_sol import *



path = os.path.join (os.path.split(os.path.abspath(__file__))[0],"README.md")
descr = fmteach.exercises.descriptor.ExerciseDescriptor ("EnumerateExplicit",path,run,run_sol)


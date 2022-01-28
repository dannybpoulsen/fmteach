import os
import importlib

def search_exercises ():
    root = os.path.split(os.path.abspath(__file__))[0]
    for f in os.listdir (root):
        if os.path.isdir (os.path.join (root,f)) and not f.startswith("__"):
            
            mod = importlib.import_module (f"fmteach.exercises.{f}")
            yield mod.descr

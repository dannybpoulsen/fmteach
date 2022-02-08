import os
import importlib
from fmteach.domains.domaindescription import * 

studdomains = {}
soldomains = {}

def search_domains ():
    root = os.path.split(os.path.abspath(__file__))[0]
    for f in os.listdir (root):
        if os.path.isdir (os.path.join (root,f)) and not f.startswith("__"):
            
            mod = importlib.import_module (f"fmteach.domains.{f}.stud")
            studdomains[f] = mod.descr

            mod = importlib.import_module (f"fmteach.domains.{f}.sol")
            soldomains[f] = mod.descr


search_domains ()


def domainnames ():
    yield from studdomains.keys()

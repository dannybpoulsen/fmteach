import os

path = os.path.split(os.path.abspath (__file__))[0]

def getFiles ():
    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            if f.endswith ("while"):
                yield os.path.join (dirpath,f)


import sys

class Messager:
    def message (self,s):
        sys.stdout.write (f"Message: {s}\n")

    def error (self,s):
        sys.stdout.write (f"Error:   {s}\n")
    
    def warning (self,s):
        sys.stdout.write (f"Warning: {s}\n")
    

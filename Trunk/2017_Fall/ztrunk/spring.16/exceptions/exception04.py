"""
Won't even return to a function that it was called from...
"""

def no_return():
    print("I am about to raise an exception") 
    raise Exception("This is always raised") 
    print("This line will never execute") 
    return "I won't be returned"
    
    
def call_exceptor():
    print("call_exceptor starts here...") 
    no_return()
    print("an exception was raised...") 
    print("...so these lines don't run")



call_exceptor()
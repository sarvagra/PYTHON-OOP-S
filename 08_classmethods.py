# syntax : use @classmethod before the method.
# to give inputs without creating objects , we can use class method :

class access():
    
    def __init__(self ,val) :
        
        self.value=val 
        
    @classmethod
    def func1(cls,val):
        return cls(val)
    
a=access.func1("hey")
a.value
    
# to add an external function into a class , use : <class name>.<function name> = classmethod(<function name>)
# add below function to a the class access

def func2(cls,new_val):
     print(new_val)

access.func2=classmethod(func2)
access.func2("pew")              #we just accessed the function from class access\


# to delete a function use : del <class name>.<function name>

del access.func1

#func1 is deleted



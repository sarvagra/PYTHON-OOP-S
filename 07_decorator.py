# we can use decorators to decorate our functions as follows:

def deco(func):
    def inner_def():  
        print ("this is the start of my function")
        func
        print ("this is the end of my function")
    return inner_def 

@deco 
def test():
    print("this is the function")
    
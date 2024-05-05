# importing abc class for abstraction

import abc

class abst():

    @abc.abstractmethod
    def one(self):
        return "this is the first function"
    
    @abc.abstractmethod
    def two(self):
        return "this is the second function"
    
    @abc.abstractmethod 
    def three(self):
        return "this is the third function"
    
class abst2(abst):
    def one(self):
        return "this will store numbers"
    
    def two(self):
        return "this will store words"
    
    def three(self):
        return "this will store sentences"
    


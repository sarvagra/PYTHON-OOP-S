# using property methods to get , set or delete private variables.

class prop():

    def __init__ (self,cost):
        self.__cst=cost

    @property              #lets user access thhe variable and update it
    def access(self):
        return self.__cst
    
    @access.setter         # updates the value of variable
    def set(self, cost1):
        self.__cst=cost1
    
    @access.deleter       # deletes the variable
    def del_access(self):
        del self.__cst
    
    

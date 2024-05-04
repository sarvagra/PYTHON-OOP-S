# multi-level inheritance

class one:
    def main1(self):
        return "this is class one"
    
class two(one):
    def main2(self):
        return "this is class two"

class three(two):
    pass

# now after creating an object and calling class 3 , we find that class 3 has properties of class two which has the properties of class 1.

obj = three()
obj.main1()
obj.main2()



# multiple inheritance

class one:
    def main1(self):
        return "this is class one"
    
class two:
    def main2(self):
        return "this is class two"

class three(one , two):
    pass

# now after creating an object and calling class 3 , we find that class 3 has properties of both class one and two.

obj = three()
obj.main1()
obj.main2()

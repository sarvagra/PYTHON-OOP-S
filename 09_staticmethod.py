# static method is used for memory optimisation , also we can give inputs without making objects.

class statmethod:
    
    @staticmethod
    def name(n):
        print(n)
        
    @staticmethod
    def age(a):
        print(a)
        
        
    @staticmethod 
    def ident(card):
        print(card)
        statmethod.name("sarvagra")
        statmethod.age("18")

statmethod.ident("identity")


# encapsulation promotes data from bring modefied by user as it hides variables by making them private

# Code below illustrates the use of encapsulation

class bike:
    def __init__(self , model, year, company, speed):
        self.__model=model
        self.__year=year
        self.__company=company
        self.__model=model

        b= bike("H2r",2020,"KAWASAKI",300)

        # now the variables cant be accessed by user as theyre private

# create a bank account program with balance,deposit and withdraw functions keeping balance as private.

class bank:
    def __init__(self,bal):
        self.__balance=bal

    def deposit(self,depo):
        self.__balance=self.__balance + depo

    def withdraw(self, wdr):
        if self.__balance>=wdr :
            self.__balance= self.__balance-wdr
        else :
            print("Not enough balance to withdraw!")

    def balance(self):
        return self.__balance
    
sarv= bank(1000)      #creating an object to set value in balance


    #now we can perform deposit and withdraw functions.
    
        

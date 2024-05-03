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

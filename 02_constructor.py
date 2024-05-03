# constructor is used to declare variables. Syntax : def __init__(pointer, var1,var2,var3...,var_n)
class new :    
    def __init__(first,a,b,c):
        first.a1=a
        first.b1=b
        first.c1=c 

    def print(first) :                         #prints the data input
        return first.a1 ,first.b1,first.c1
    
# create a class to store students data and print it 

class student_data :    
    def __init__(detail,n,std,roll):
        detail.name=n
        detail.cls=std
        detail.rn=roll

    def print(detail) :                         #prints the data input
        return detail.name ,detail.cls,detail.ron
    
alex = student_data ("alex","12th",9920)
alex.print()

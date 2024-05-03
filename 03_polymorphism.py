# displays the sum if two numbers are input or concatenates if two string are input or combines two lists if lists are input.

# a function changes itself accordingly with the object passed in it

class detail1:
    def name(self):
        print("Sarvagra")

class detail2:
    def name(self):
        print("Singh")

def call(x):
    for i in x:
        i.name()

detail1=detail1()
detail2=detail2()

x= [detail1,detail2]
call(x)

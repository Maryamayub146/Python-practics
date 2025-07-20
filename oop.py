class Students:
    name = "maryam"

s1 = Students()
print(type(s1.name))


# create a car factpry
class Car:
    car = "bmw"
    brand = "lux"

c1 = Car()
print(c1.car)  

# create a student class that takes name and marks of 3 subjects as arguments in constructor

class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name ,"ur marks avg is",sum/3)       
        
s1 = Students("tony",[22,33,44])
s1.get_avg()
s2 = Students("mary",[33,44,55]) 
s2.get_avg() 

# abstraction mean hide the unneccssary things only show essentail features

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.brk = True
        self.acc = True
        print("done start car")

c1 = Car() 
c1.start()     


# create a account class with 2 attributes balance and account no
# create method for debit credit and printing the balance
 
class Account:
    def __init__(self,balance,accountno):
        self.balance = balance
        self.account = accountno


ac1 = Account(22212,437879)
print(ac1.account)


              
   
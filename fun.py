# Functions & Recursion in Python 
def cal_fun(a,b):
    return a+b

sum = cal_fun(2,5)
print(sum)

# print of average of 3 number 
def avg(a,b,c):
    sum = a +b +c
    avgg = sum / 3
    print(avgg)
    return avgg
avg(2,3,4)

# python two types 1: built in function 2:user defind function
# built in function ==> print("function") <== this is built in fun  print() len() , type(), range()
# user defined ==> those function jo hum khud create krty ha un ko user defined func katy ha

# default parameters

# WAF to print a factorial function



def cal_fac(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
        print(fact)

cal_fac(5)

# WAF to convert to USD to PK

def convert(usd):
    pk = usd * 281
    print(usd , " USD ="  , pk ,"PKS")

convert(100) 


# WAP to print lenght of list
cities = ["one","two","three"]
citie = ["one","two","three","hdjhj","shghdg"]


def print_len(list):
    print(len(list))

print(len(cities))
print(citie)

# single line py print krna using parameter





 



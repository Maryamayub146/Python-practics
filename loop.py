# loops in python
count = 5
while count <=10:
   print(count)
   count += 1
# print number from 1 to 100

number = 0
while number<=100:
   number +=1
   print(number)

# print numbers from 100 to 1

number2 = 100
while number2 >=1:
 number2 -= 1
 print(number2)

#  print the multiplication of number n
i = 1
while i <=10:
   print(i*3)
   i +=1 


string = "maryam"

print(string.replace("m","n"))

 # print the elemests of the following list using
# [11,22,33,44,55,66,77,88,99,100]
number = [11,22,33,44,55,66,77,88,99,100]
index = 0
while index < len(number):
   print(number[index])
   index +=1

# # tarverse krna
# # same as a print of heros name
heros = ["shadid","captain","ali","mary","harry"]
idx = 0
while idx <len(heros):
   print(heros[idx])
   idx +=1

# # search for a number X in this tuple using loop
num = (1,2,3,4,5,6,7,8,9,99,66,77)

x = 6
indx = 0
while indx < len(num):
   if(num[indx]==x):
      print("final found" , indx)
      break 
   indx +=1


# # loops in python
# # list tuple string
str  =  "appna"

for char in str:
   if(char == "n"):
      print("done found")
      break
   print(char)   


# # rint the elemest of the follwoing list using loop
list = [1,2,3,4,5,6,7,8,9]

for el in list:
   print(el)


# # search a number X n this tuple sing loop
tuple = (1,2,3,4,5,6,7,8,9,4)

x = 4
i = 0
for el in tuple :
   if(el == x):
     print("found 4",i)
   i += 1
   
# # range 
number_range = range(10)

for ele in number_range :
   print(ele)

print("this is range value")
# another method 
# odd or even number print using (start , steps ,stops)
for i in range(1 , 10 , 2):
   print(i)

# # print the number of 1 to 100

for value in range(1 ,10):
    print(value)


# # prints number from 100 to 1
for us in range(10 ,0 , -1):
   print(us)

# # print the multiplication table on any number of n

table = int(input("print any table"))

for i in range(1,11):
   print(table * i)

     
# # print of sum number using n
n = 10
i = 0

for i in range(1,n+1):
   i +=1
   print("total",i)

# range
seq = range(6)

for i in seq:
   print (i)

# WAP TO SUME FRIST 10 NUMBERS

n = 5
sum = 0
for i in range(1, n+1):
    sum += i
    print(sum)






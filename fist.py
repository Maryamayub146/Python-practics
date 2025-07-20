# string ,variables, data types , conditional statment
str1 = "maryam"
str2 = "ayubjjjhjpython fist.py"
full_name = str2.endswith("ee")
full_name = str2.capitalize()
full_name = str1.replace("maryam","marium muzamil")
full_name = str2.find("py")
full_name = str1.count("a")
print(full_name)

# WAP to take a input user name and print length

# Frist_Name = input("Enter Your name : ")
# print(Frist_Name)
# print("lenght of ur str :",len(Frist_Name))

# WAP to find occurance of "$" in a string
str = "this is $ now $i $33 want to count $ done"
count = str.count("$")
print(count)

# gussing the number 
number = 7
guss = int(input("gues the number :"))
if guss==number :
   print("win")
elif guss > number :
   print("wrong")

print("try again")

# student marks sheet
# WAP to check the number are even are odd

num = int(input("enter any number "))

rem = num%2

if rem == 0 :
   print("even")
else :
   print("odd ")  

 #WAP to find the greatest number entered by user
# WAP to check if a number is a multple of 7 or not  
with open("practics.text","r") as f:
    data = f.read()

new = data.replace("my","me")
print(new) 

with open("practics.text","w") as f:
    f.write(new) 



# r w a b t .....r+ w+ a+   
    
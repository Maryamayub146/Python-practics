# Dictionary & Set in Python
dictopnary = {
    "name" : "maryam",
    "age"  : 22,
    "is_adult" : "yes",

}
dictopnary["age"] = "222"
print(type(dictopnary))

# nested dictionary
students = {
    "name" : "maryam",
    "subject" : {
        "phy" : 33,
        "chmy" : 33,
        "math" : 44
    },
    "age" : 22,
    "value": "mary"
}
print(len(students))
print(students.values())
print(students.keys())
print(students.items())

# set of dictionary
collection = {1,2,3,4,4,5,"hello","marr"}


print(collection.pop())

empty_set = set()

# different subjects ka classroom bnana ha hr students ka hr subject ka liya class romm create krna ha 
subjects = {"python","java","JS","c++","c","python","c","c++"}
print(len(subjects))

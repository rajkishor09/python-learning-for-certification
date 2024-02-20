# one way of defining dictionary
my_dict = {"name" : "John", "age" : 30, "city" : "New York"}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])

keys = my_dict.keys()
print("looping keys =>")
for k in keys:
    print(k, my_dict[k], sep=": ")

# another way of defining dictionary
my_dict = dict(name = "John", age = 30, city = "New York")
print(my_dict)
print(type(my_dict))

# another way of defining dictionary
my_dict2 = {}
my_dict2["name"] = "John"
my_dict2["age"] = 30
print(my_dict2)
print(type(my_dict2))

print(my_dict2.get("na", "raj")) # if key is not present, it will return "raj"

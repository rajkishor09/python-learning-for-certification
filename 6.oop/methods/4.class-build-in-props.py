class Classy:
    pass

# print file currently being run or module name (when imported) 
print(Classy.__module__)
obj = Classy()
print(obj.__module__)
# prints class name
print(Classy.__name__)
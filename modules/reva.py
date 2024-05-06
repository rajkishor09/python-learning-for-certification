print("my name is reva") # prints when imported in index.py file, no need to call any method
print("Module name: ", __name__) # prints this module name which is "reva"

counter = 0
   
if __name__ == "__main__":
   print("I prefer to be a module.") # this will print when we run this file directly
else:
   print("I like to be a module.") # this will be printed when we import this file as module in other file

def sum(a, b):
    return a + b

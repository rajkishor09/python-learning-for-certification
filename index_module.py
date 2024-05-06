from sys import path
path.append('./modules') # load module from different path
import reva

print("Module name: ", __name__)

print(reva.counter)
print(reva.sum(5, 8))
print(reva.sum("raj", "reva"))
from platform import *
print(platform())
print(machine())
print(processor())
print("System :", system())
print(version())
print("Processor: ", processor())

print(python_implementation())
for atr in python_version_tuple():
    print(atr)

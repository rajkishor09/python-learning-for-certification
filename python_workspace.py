from platform import *
print(platform())
print(machine())
print(processor())
print(system())
print(version())

print(python_implementation())
for atr in python_version_tuple():
    print(atr)

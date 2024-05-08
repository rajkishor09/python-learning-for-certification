"""
Example of class with class variables
"""

class ExampleClass:
    counter = 0  # Note: this is a static variable
    def __init__(self, val = 1):
        self._some = "Hi" # single underscore means, variable name change in future. Don't refer it.
        self.__first = val # __first is class local variable
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)
# __dict__ prints all the variable available in object
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# prints private variable value
print(example_object_3._ExampleClass__first) # double underscore variable are mangled by Python. To access such variables use _ClassName__variable.
example_object_3._ExampleClass__first = 90
print(example_object_3._ExampleClass__first)
print(example_object_3._some)

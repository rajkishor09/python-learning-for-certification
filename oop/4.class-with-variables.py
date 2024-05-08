class ExampleClass:
    def __init__(self, val = 1):
        self.first = val # first is public variables

    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5 # dynamically add a prop

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

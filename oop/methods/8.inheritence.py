class Super:
    super_var = "super"
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    sub_var = "sub"
    def __init__(self, name):
        super().__init__(name) # without knowing the name of super class
        # Super.__init__(self, name) # another way to call base __init__

obj = Sub("Raj")

print(obj)
print(obj.super_var, obj.sub_var)

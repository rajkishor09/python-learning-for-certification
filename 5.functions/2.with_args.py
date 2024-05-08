print("OPTIONAL ARGS")
def sum(a=0, b=0): # optional parameters
    return a + b

print(sum(1,2))
print(sum(1))
print("REST Args with LIST")
def calc(**rest): # like JS rest param which has type list
    print(type(rest))
    print(rest)

calc(a=1, b=2, c=3)

print("REST Args with TUPLE")
def calc2(*rest): # like JS rest param which has type tuple
    print(type(rest))
    print(rest)

calc2(1, 2, 3)

print("MIXED ARGS: string, tuple & list")
"""
some method
"""
def mixed_args(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

mixed_args("John", 1, 2, 3, a=1, b=2)
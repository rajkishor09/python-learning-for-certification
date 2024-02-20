# NOTE: in tuples value cannot be changed like list
my_tuple = (1, True, "hello")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

my_tuple2 = ("India", "USA", "UK")
#my_tuple2[0] = "China" #this is not allowed

my_tuple3 = ("raj", ) # by adding trailing comma, we can declare single element tuple
print(type(my_tuple3))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2 # we can merge or concatenate tuple using + sign
print(tuple3)

tuple_to_list = list(tuple3) # we can convert tuple to list using list()
print(tuple_to_list)
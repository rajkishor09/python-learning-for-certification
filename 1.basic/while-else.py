
while input("continue? :") == "Y":
    qty = input("enter quantity :")
    if int(qty) <= 0:
        print("invalid quantity")
        break
else:
    # executes when while loop exits without calling break
    print("thanks")


while input("continue? :") == "Y":
    qty = input("enter quantity :")
    if int(qty) <= 0:
        print("invalid quantity")
        break
else:
    # executes when while loop executed without break
    print("thanks")

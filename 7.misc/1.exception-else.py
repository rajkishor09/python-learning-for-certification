# any one is from except or else will execute
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2)) # else part
print(reciprocal(0)) # except part
    
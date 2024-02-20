def positive_num(number):
    if number <0:
        raise ValueError("Number must be positive")

try:
    number = int(input("Enter a number: "))
    positive_num(number)
except ValueError:
    print("Invalid input")
except KeyboardInterrupt:
    print("You cancelled the operation")
finally:
    print("Thank you")


def generate(numbers):
    i= 0
    while i < numbers:
        yield i # return values and continues execution till condition is met
        i += 1

for n in generate(5):
    print(n)
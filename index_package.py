from sys import path
path.append('./packages')
from calc.two.addl import do as sumOfTwo
from calc.three.addl import do as sumOfThree

print(sumOfTwo(2, 7))
print(sumOfThree(2, 4, 4))
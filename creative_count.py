import numpy as np, numpy.random
from random import uniform, sample, choice
import sys

def f(n, s):
    r = min(s, 1)
    x = uniform(max(0, r - (r - s / n) * 2), r)
    return n < 2 and [s] or sample([x] + f(n - 1, s - x), n)

#
#   Creates an equation with decimal numbers
#
def decimal_num(n, s):

    # Generates an equation with the given size and total
    def f(n, s):
        r = min(s, 1)
        x = uniform(max(0, r - (r - s / n) * 2), r)
        return n < 2 and [s] or sample([x] + f(n - 1, s - x), n)

    x = f(n, s)
    s = ""
    for i in x:

        # This is here to make the outcome more unique by giving 3 options to change the math
        c = choice([0, 1, 2])
        if c == 0:
            subMax = uniform(i + 1, i + 10)
            subMin = subMax - i
            s = s + "+(" + str(subMax) + "-" + str(subMin) + ")"

        elif c == 1:
            mulMax = uniform(0.00000001, i - 0.00000001)
            mulMin = i / mulMax
            s = s + "+(" + str(mulMax) + "*" + str(mulMin) + ")"
        
        else:
            s = s + "+" + str(i)
    print(s[1:])

#
#   Creates an equation with whole numbers
#
def whole_num(n, m):
    s = ""
    nums = np.random.multinomial(m, np.ones(n)/n).tolist()
    for i in nums:
        s = s + "+" + str(i)
    print(s[1:])


try:
    size = int(sys.argv[2])
    total = int(sys.argv[3])
except:
    print("Invalid argument")

if sys.argv[1] == "d":
    decimal_num(size, total)
elif sys.argv[1] == "w":
    whole_num(size, total)
else:
    print("Invalid argument")
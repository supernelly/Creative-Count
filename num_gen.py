import numpy as np, numpy.random
from random import *

def f(n, s):
    r = min(s, 1)
    x = uniform(max(0, r - (r - s / n) * 2), r)
    return n < 2 and [s] or sample([x] + f(n - 1, s - x), n)

def decimalNum(n, s):
    x = f(n, s)
    s = ""
    for i in x:
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

def wholeNum(n, m):
    s = ""
    nums = np.random.multinomial(m, np.ones(n)/n).tolist()
    for i in nums:
        s = s + "+" + str(i)
    print(s[1:])


decimalNum(5, 15) # (size, total)
#wholeNum(3, 40) # (size, total)
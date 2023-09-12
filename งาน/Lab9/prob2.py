from pkg_maths.fact import fact
from pkg_maths.fib import fib

import random
min = 1
max = 4
num = random.randint(min, max)
print(f"fact of {num} is {fact(num)}")
print(f"fib of {num} is {fib(num)}")
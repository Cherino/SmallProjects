import datetime
import sys
sys.setrecursionlimit(200001)

i = [0, 1]
def fib(i):
    if len(i) < 200000:
        return i
    elif i[-1] + i[-2] > 0:
        i.append(i[-1] + i[-2])
        return fib(i)
    else:
        return i
print(f"Starting Fibonacci sequence generation at {datetime.datetime.now()}")
fib(i)
print(f"Fibonacci sequence generation completed at {datetime.datetime.now()}")
print(f"Generated {len(i)} Fibonacci numbers.")
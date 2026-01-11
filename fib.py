import datetime
import sys
sys.setrecursionlimit(200001)

i = [0, 1]
def fib(i):
    if len(i) < 200000 and i[-1] + i[-2] > 0:
        i.append(i[-1] + i[-2])
        return fib(i)
    else:
        return i
print(f"Starting Fibonacci sequence generation at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
fib(i)
print(f"Fibonacci sequence generation completed at {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
print(f"Generated {len(i)} Fibonacci numbers.")
import math

func = input("Enter the function to integrate (do not include dx)\n(use 'x' as the variable, e.g., 'x**2 + 3*x + 2'): ")
def eval_func(func_str):#validates the function string
    for i in func_str:
        if i not in "0123456789x+-*/(). ^emath.sin/cos/tan/log/exp/pi": #Valid characters in function string
            raise ValueError("Invalid character in function string.") #Raise error if invalid character found
        if 'e' in func_str:
            func_str = func_str.replace('e', str(math.e)) #Replace 'e' with Euler's number
        if '^' in func_str:
            func_str = func_str.replace('^', '**') #Replace '^' with '**' for power operation
    return lambda x: eval(func_str.replace('x', f'({x})')) #lambda x allows a change in x when operating the function
def calculate_area(func_str, lower_bound, upper_bound, steps, delta):#Calculates area using trapezoidal rule
    total_area = 0.0 #area intitalised as float
    fx = eval_func(func_str)#look at eval_func function @line 4
    for i in range(steps): #Iterate over number of steps
        dx1 = lower_bound + i * delta #dx1 is the left endpoint of the sub-interval
        dx2 = lower_bound + (i + 1) * delta #dx2 is the right endpoint of the sub-interval
        total_area += (fx(dx1) * delta + ((fx(dx2)-fx(dx1)) * delta / 2)) #Trapezoidal rule formula
    return total_area #return total summed area

print("Welcome to Trapezoidal Rule area calculator")
print('-'*40)
print("note that if you wish to use exponential functions, use 'e' to represent Euler's number\n"
"Also, you can use ^ to represent powers (e.g., x^2 for x squared)\n"
"and If you wish to use pi or other functions, use 'math.pi', 'math.sin()', etc.\n"
"such that your inputs may be 0, math.i/2, x^2*math.sin(x), etc.")
print('-'*40) #Menu specifies what inputs are valid, this makes use of the math module in py
#bounds are defined in terms of the integration symbol S
lower_bound = eval(input("Enter Lower bound for your integral: "))
upper_bound = eval(input("Enter Upper bound for your integral: "))
#steps define the sub-intervals used in the trapezoidal rule
steps = int(input("Enter number of steps for your integral: "))
if steps > 10000:#over 10,000 steps seems arbitrary and slows down computation so a limit is set
    print("Warning: High number of steps may slow down computation.\n"
    "setting steps to max of 10000")
    steps = 10000
#delta is calculated as the width of each sub-interval by dividing the range by number of steps
delta = (upper_bound - lower_bound) / steps
area = calculate_area(func, lower_bound, upper_bound, steps, delta)#look at calculate_area function @line 13
print(f"The approximate area under the curve from {lower_bound} to {upper_bound} is: {area}")

while True:#Loop to allow user to recalculate with different step sizes
    again = input("Change step size? (y/n) ").strip().lower()
    if again == 'y':
        steps = int(input("Enter number of steps: "))
        if steps > 10000:
            print("Warning: High number of steps may slow down computation.\n" \
            "setting steps to max of 10000")
            steps = 10000
        delta = (upper_bound - lower_bound) / steps
        area = calculate_area(func, lower_bound, upper_bound, steps, delta)
        print(f"The approximate area under the curve from {lower_bound} to {upper_bound} is: {area}")
    else:
        print("Exiting program.")
        break

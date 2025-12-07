import math
def eval_func(func_str):# converts function string to callable function and validates it
    for i in str(func_str):
        if i not in "0123456789x+-*/(). <>^emath.sin/cos/tan/log/exp/pi": #Valid characters in function string
            raise ValueError("Invalid character in function string.") #Raise error if invalid character found
        if 'e' in func_str:
            func_str = func_str.replace('e', str(math.e)) #Replace 'e' with Euler's number
        if '^' in func_str:
            func_str = func_str.replace('^', '**') #Replace '^' with '**' for power operation
    return lambda x: eval(func_str.replace('x', f'({x})')) #lambda x allows a change in x when operating the function

def calculate_dx(func_str, x):#Calculates derivative using first principles
    fx = eval_func(func_str)
    h = 0.0000000001 # Small value for numerical differentiation
    return (fx(x + h) - fx(x)) /  h  #first principles formula

def newton_raphson(func_str, derivative, initial_guess):
    fx = eval_func(func_str) #look at eval_func function @line 2
    dfx = derivative
    h = 0.0000000001
    max_iterations = 100
    guess = initial_guess
    for i in range(max_iterations):
        f_value = fx(guess)
        df_value = dfx(guess)
        if df_value == 0:
            raise ValueError("Derivative is zero. No solution found.")
        next_guess = guess - f_value / df_value
        if abs(next_guess - guess) < h:
            print(f"Root found: {next_guess} after {i+1} iterations.")
            return next_guess
        guess = next_guess
    print(f"Maximum iterations reached. Last guess: {guess}")

print("Welcome to Newton-Raphson Root Finder")
print('-'*40)
print("NOTE: If you wish to use exponential functions, use 'e' to represent Euler's number\n"
"Also, you can use ^ to represent powers (e.g., x^2 for x squared)\n"
"and If you wish to use pi or other functions, use 'math.pi', 'math.sin()', etc.\n"
"such that your inputs may be 0, math.i/2, x^2*math.sin(x), etc.")
print('-'*40) #Menu specifies what inputs are valid, this makes use of the math module in py
func = input("Enter the function to integrate (do not include dx)\n(use 'x' as the variable, e.g., 'x**2 + 3*x + 2'): ")
x = float(input("Enter your initial guess for the root: "))
newton_raphson(func, lambda t: calculate_dx(func, t), x)

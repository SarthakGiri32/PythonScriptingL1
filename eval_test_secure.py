from math import *


def secret_function():
    print("Secret key is 1234")


def function_creator(safedt):
    expr = input("Enter the expression(in terms of x): ")
    x = int(input("Enter the value of x: "))
    safedt['x'] = x
    print(safedt)
    # y = eval(expr, globaldt)
    y = eval(expr, {"__builtins__": None}, safedt)
    print("y=", y)


safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
             'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
             'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
             'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
             'tan', 'tanh']
dt = locals()
safe_dict = dict([(k, dt.get(k)) for k in safe_list])
function_creator(safe_dict)

def secret_function():
    print("Secret key is 1234")


def function_creator():
    expr = input("Enter the expression(in terms of x): ")
    x = int(input("Enter the value of x: "))
    y = eval(expr)
    print("y=", y)


function_creator()

# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
print("Part 1")


def other_function(number):
    return number + 10


def normal_function(func):
    result = func(1)
    print(result)


normal_function(other_function)

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
print("Part 2")

lambda_func = lambda number: number + 20

normal_function(lambda_func)


# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
print("Part 3")


def normal_function_v2(func, *args):
    for argument in args:
        result = func(argument)
        print(result)


normal_function_v2(lambda_func, 1, 2, 3)

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
print("Part 4")


def normal_function_format_output(func):
    result = func(1)
    print(str(result).center(20))
    print("Result: {:^20.2f}".format(result))


normal_function_format_output(other_function)


def func(var_a, var_b):

    if (type(var_a) is not int) or (type(var_b) is not int):

        return print("str")


    else:
        if var_a > var_b:
            return print(">")
        elif var_a == var_b:
            return print("=")
        elif var_a < var_b:
            return print("<")


func(1, 2)
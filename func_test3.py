def foo(x):
    def bar(x):
        return x + 1.0

    return print(bar(x * 2))


#foo(3)

def foo (numbers_list = []):
    if numbers_list:
        numbers_list.append(1)
    else:
        numbers_list.append(2)
    return print(numbers_list)

foo()
foo()

numbers_list = [3, 6, 1, 8]
def foo(ls):
    return print(ls.sort())
foo(numbers_list)


def outer_function(a):
    a += 1
    def inner_function(b):
        a += b
        return print(a)
    return inner_function(1)

outer_function(1)
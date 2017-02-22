
def max_value(a: int, b: int) -> int:
    """"Get two numbers and returns max"""
    if a>b:
        return a
    elif b>a:
        return b
    print("END")


#print(max_value.__annotations__)
#print(max_value(3, 3))
#print(max_value(3, -5))

s = "world"

def increment_lst(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item + l)
    return new_lst

l = [1, 2, 3]

l2 = increment_lst(l)

print(l)
print(l2)
print(l is l2)
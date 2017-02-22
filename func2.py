def get_pi():
    return 3.14

p = get_pi()

#print(p)

def max_value(a, b):
    if a>b:
        return a
    elif b>a:
        return b
    print("EMPTY")

print(max_value(3, 3))
print(max_value(3, -5))
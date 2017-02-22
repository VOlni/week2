def a(x, y, z):
    if x:
        return print(y)
    else:
        return print(z)

def b(q, r):
    return a(q>r, q, r)

a(False, 2, 3)
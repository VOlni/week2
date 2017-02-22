def a(x):
    return x + 1


def b(x):
    return x + 1.0


def c(x, y):
    return x + y


def d(x, y):
    return x > y


def e(x, y, z):
    return x >= y and x <= z


def f(x, y):
    x + y - 2

#print(type(d('monty', 'python')))
#print(d('monty', 'python'))

def show_full_name(name, surname, patronymic = None):
    return 'Fullname: {} {} {}'.format(name, patronymic, surname)

#ex1
#record = {'surname': 'ivanko', 'name': 'kolya', 'age': 15}
#show_full_name(**record)

#ex2
#record1 = {'surname': 'ivanko', 'name': 'kolya'}
#record2 = ['petrovich']
#show_full_name(**record1, *record2)

record = {'surname': 'ivanko', 'name': 'kolya'}
show_full_name(**record)
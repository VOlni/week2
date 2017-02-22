def hello(name, surname='', *, title='Mr.'):
    full_name = name
    if surname:
        full_name = full_name + ' ' + surname
    if title:
        full_name = title + ' ' + full_name
    print("Hello %s!" % full_name)

hello("Peter", 'Smith', title="Sir")

hello("John", title='Sir')

p = hello("world", title='')

print(p)
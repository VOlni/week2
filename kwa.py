def hello(name, surname='', title='Mr.'):
    if surname:
        surname = ' ' + surname.strip()
    print("Hello %s %s%s" % (title, name, surname))
a = ["John", "Galt"]
kwa = {'surname':'Galt’, 'title':'Sir'}
hello(*a)
hello("John", **kwa)
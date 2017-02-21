def hi (name, title='', some='def value'):
    #name = 'Peter'
    print("Hello, %s %s %s!" % (title, name, some))


def hello(name):
    """ This function prints "Hello %username%!"  """
    print("Hello, %s!" % name)

hi("Vasiliy", "man")
hi("John", "Mr.")
hi(name="George", title="Mister")
hi("Anna", '', "gorgeous")
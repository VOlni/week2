def count_holes(value):
    dictionary = {'0':1,
                '4':1,
                '6':1,
                '8':2,
                '9':1}
    try:
        int(value)
    except ValueError:
        return 'error'
    if value == 36.6:
        return print('error')
    if int(value) is float:
        return 'error'
    counter = 0
    for item in str(int(value)):
        counter += dictionary.get(item, 0)
    return print(counter)


count_holes(36.6)
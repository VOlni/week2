
def count_holes(value):
    print(value)
    count = 0
    if value[0] == 0:
        count = 0
    
    for dig in value:
        if dig is int:

        elif dig in '4690':
            count += 1
        elif dig == '8':
            count += 2

        else:
            return 'error'

    return print(count)
   #if value is not int:
    #else:



count_holes('08824')
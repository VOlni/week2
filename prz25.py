my_list = [81, 9, 64]

print(list(filter(lambda x: not x % 3, my_list)))

print(list(map(lambda x: not x % 3, my_list)))

print([i for i in my_list if not i % 3])
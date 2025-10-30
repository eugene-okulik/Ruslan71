my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print(my_dict['tuple'][-1])


my_dict['list'].append(60)
del my_dict['list'][1]
print(my_dict['list'][1])


my_dict[('i am a tuple',)] = 'some value'
del my_dict['dict']['b']
print(my_dict['dict'])

my_dict['set'].add(6)
my_dict['set'].remove(2)
print(my_dict['set'])

print(my_dict)

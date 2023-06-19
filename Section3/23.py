my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print(my_dict['key1'])

prices_lookup = {'apple' : 2.99, 'oranges' : 1.99, 'milk' : 5.80}
print(prices_lookup['apple'])

d = {'k1' : 123, 'k2' : [0,1,2], 'k3' : {'insideKey' : 100}}
print(d['k3']['insideKey'])

# Uppercase a string
d = {'key1':['a', 'b', 'c']}
mylist = d['key1']
letter = mylist[2]
print(letter)
print(letter.upper())

# Adds to the dictionary
d = {'k1' : 100, 'k2' : 200} 
d['k3'] = 300
print(d)

# Overrides to a new value
d['k1'] = 'NEW VALUE'
print(d)

d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d)
print(d.keys())
print(d.values())
print(d.items())
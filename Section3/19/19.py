print('This is a string {}'.format('INSERTED'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
print(result)
print("The result was {r:1.5f}".format(r=result))

name = "Jose"
print(f'Hello, his name is {name}')

name2 = "Sam"
age = 3
print(f'{name2} is {age} years old')
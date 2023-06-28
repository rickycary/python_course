# For Loops in Python

# Example #1
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print('hello')

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')
        
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

# Example #2
mystring = 'Hello World'
for letter in mystring:
    print(letter)
    
# Example #3
tup = (1,2,3)
for item in tup:
    print(item)
    
mylist = [(1,2), (3,4), (5,6), (7,8)]
for (a,b) in mylist:
    print(a)
#    print(b)

# Example #4
mylist = [(1,2,3), (5,6,7), (8,9,10)]
for a,b,c in mylist:
    print(b)
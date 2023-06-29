# Useful operators in python

# Example 1
mylist = [1,2,3]
for num in range(0,10,2):
    print(num)

# Example 2
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)
    
# Example 3
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1, mylist2):
    print(item)
    
# Example 4
mylist = [10, 20, 30, 40, 100]
print(min(mylist))
print(max(mylist))
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
print(shuffle(mylist))

from random import randint
print(randint(0,100))

# Example 5
result = input('Favorite Number: ')
print(result)
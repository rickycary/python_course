# Test Solutions 
#1
# Print only the words that start with s in this sentence

st = 'Print only the words that start with s in this sentence'
print(st)
print(st.split())

for word in st.split():
    if word[0] == 's':
        print(word)
        
#2
# Use range() to print all the even number from 0 to 10

print(list(range(0,11,2)))

#3 
# Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3. 

print(list(range(0,51,3)))

#4
# Print every word in this sentence that has an even number of letters

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word+ ' is even')
        
# 5
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For number which are multiples of both three and five print "FizzBuzz"

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
        
#6 
# Use list comprehension to creae a list of the first letters of every word in the string below.

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])

'''
Authour:Ibin Siby
Discription:create a tuple of numbers or strings
python program fo performing the following operations
1.use a for loop to print all elements of the tuple
2.use while loop to print elements of the tuple in reverse order
3.create a tuple of strings and use a loop to print only the strings that start with the letter 'b'.

'''
numbers=(10,20,30,40,50)
print("all elements:")
for num in numbers:
    print(num)

print("elements in reverse order:")
i=len(numbers)-1
while i>=0:
    print(numbers[i])
    i=i-1

fruits=("apple","banana","cherry","blueberry")
print("strings that start with 'b':")
for fruit in fruits:
    if fruit.startswith('b'):
        print(fruit)

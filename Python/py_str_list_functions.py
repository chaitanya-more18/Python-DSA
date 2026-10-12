# #STRING FUNCTIONS

# text = "Hello World"

# # ljust() aligns the string to the left
# print(text.ljust(20, "-"))

# # rjust() aligns the string to the right
# print(text.rjust(20, "-"))

# # partition() divides the string into three parts using the given separator
# print(text.partition(" "))

# # isupper() checks whether all the letters in the string are uppercase
# print( text.isupper())

# # islower() checks whether all the letters in the string are lowercase
# print(text.islower())



#LIST FUNCTIONS
numbers = [30, 10, 50, 20, 40]

# min() returns the smallest value from the list
print("Minimum value:", min(numbers))

# max() returns the largest value from the list
print("Maximum value:", max(numbers))

# sum() returns the total of all values in the list
print("Sum of values:", sum(numbers))

# sorted() returns a new sorted list
print("Sorted list:", sorted(numbers))

# enumerate() returns the index and value of each element
print("List elements with index:")

for index, value in enumerate(numbers):
    print(index, value)

# convert to tuple
a = [10, 20, 30]
b = tuple(a)
print(b)

# convert to set
a = [10, 20, 20, 30]
b = set(a)
print(b)
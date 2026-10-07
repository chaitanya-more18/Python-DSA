# Sum of first 10 even numbers

# sum=0
# for i in range(2,21,2):
#         sum += i
# print(sum)


#Accept 2 nos S and N, print square of first N nos starting from S

# S = int(input("Enter value of S: "))
# N = int(input("Enter valur of N: "))
# for i in range(S, N+1):
#     print(i**2)


#Reverse the string

# s = input("Enter your string: ")
# print(s[::-1])


#count vowels is sentence

# s = input("Enter your sentence: ")
# count=0
# for i in s:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         count+=1
# print("The no of vowels is",count)


#Remove duplicates from list

# data=["abc",123,"abc",81,123,9]
# unique = []
# for item in data:
#     if item not in unique:
#         unique.append(item)
# print(unique)


#Reverse the list

# l=[1,2,3,4,5]
# l.reverse()
# print(l)

#pattern print - right angled triangle

# for i in range(1,5):
#     for j in range(1,i):
#         print("*",end='')
#     print()


#pattern - pyramid

for i in range(1,5):
    for j in range(5-i):
        print(" ", end='')
    for k in range(2*i-1):
        print("*", end='')
    print()


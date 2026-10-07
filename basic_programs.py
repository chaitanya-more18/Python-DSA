# num = int(input("Enter a no: "))
# sum = 0
# while num>0:
#     sum += num%10
#     num //= 10
# print(sum)

#PALINDROME
# num = int(input("Enter a no: "))
# tmp=num
# sum = 0
# while num>0:
#     sum = sum*10 + (num%10)
#     num //= 10
# if tmp==sum:
#     print("Palindrome")
# else:
#     print("not palindrome")

#ARMSTRONG
# num = int(input("Enter a no: "))
# p=len(str(num))
# tmp=num
# sum = 0
# while num>0:
#     sum = sum + (num%10)**p
#     num //= 10
# if tmp==sum:
#     print("Armstrong")
# else:
#     print("not Armstrong")

# #CUBE SUM OF N NATURAL NUMBERS
# n = int(input("Enter a no. : "))
# sum=0
# for i in range(1,n+1):
#     sum =((n*(n+1))//2)**2
# print(sum)

#PATTERN
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()

#PATTERN 2
# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

#PATTERN 3
n=5
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    print()


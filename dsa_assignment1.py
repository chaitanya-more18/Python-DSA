# Calculate array sum

# n = int(input("Enter no. of elements: "))
# arr = []
# for i in range(n):
#     element=int(input(f"Enter {i+1} element: "))
#     arr.append(element)
# print(sum(arr))


# Find the smallest and largest element

# n = int(input("Enter no. of elements: "))
# arr = []
# for i in range(n):
#     element=int(input(f"Enter {i+1} element: "))
#     arr.append(element)

# sorted = sorted(arr)
# print("\nLargest element is ",max(arr))
# print("Second largest is", sorted[-2])
# print("Smallest element is ",min(arr))
# print("Second Smallest is", sorted[1])


# Count even odd numbers

# n = int(input("Enter no. of elements: "))
# arr = []
# for i in range(n):
#     element=int(input(f"Enter {i+1} element: "))
#     arr.append(element)

# even=0
# odd=0
# for i in arr:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"Even count is {even} and odd count is {odd}")


# Search an element

# n = int(input("Enter no. of elements: "))
# arr = []
# for i in range(n):
#     element=int(input(f"Enter {i+1} element: "))
#     arr.append(element)
# search = int(input("Enter element to seach: "))
# for i in range(0, len(arr)):
#     if arr[i]==search:
#         print(f"element found at {i} index")
# if search not in arr:
#     print("Element not present in array")


# Reverse the array

# n = int(input("Enter no. of elements: "))
# arr = []
# for i in range(n):
#     element=int(input(f"Enter {i+1} element: "))
#     arr.append(element)

# arr1=arr[::-1]
# arr2=list(reversed(arr))
# print(arr1)


# #a ab abc pattern
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+j), end="")
#     print()

# #a bb ccc pattern
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i), end="")
#     print()

# a bc def pattern
# num=0
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+num), end="")
#         num+=1
#     print()

#pyramid of a abc abcde
n=int(input("Enter no of rows: "))
for i in range(n):
    print(" "*(n-i+1), end=" ")
    for j in range(2*i+1):
        print(chr(65+j), end=" ")
    print()


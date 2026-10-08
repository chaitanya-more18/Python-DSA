#create a list of 10 numbers, print the sum of last 4 elements of the list ,
#find out diff between maximum and minimum element of the list, insert a number in a list at 6th position,
#this number must be 1/3rd 
#of number stored at 4th position.


l = [12,43,22,65,78,23,88,54,90,7]
sum = sum(l[-4:])
print(sum)

print(max(l)-min(l))

n=round((1/3)*l[3],2)
l.insert(5,n)

print("New list :",l)

name="Chaitanya"
print(max(name))
print(min(name))
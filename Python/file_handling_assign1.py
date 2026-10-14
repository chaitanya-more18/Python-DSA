# WRITE A PROGRAM TO READ A FILE AND COUNT VOWELS

# with open("Python\demo.txt","r") as f:
#     text = f.read()
# count=0
# for i in text:
#     if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         count+=1
# print("Count of vowels is :",count)


# Read all lines from file into a list. 
# print total number of lines and display 2nd and 4th line.

# with open("Python/demo.txt", "r") as file:
#     lines = file.readlines()

# print("Total lines:", len(lines))

# print("2nd line:", lines[1])
# print("4th line:", lines[3])

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# longest_word = max(words, key=len)
# print("The longest word is:", longest_word)

with open("Python/demo.txt", "r") as file:
    content = file.read()

words = content.split()
unique_words = set(words)

print("Total words:", len(words))
print("Unique words:", list(unique_words))

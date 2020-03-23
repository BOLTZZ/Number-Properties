def main():
    print("Finally we are pythoning")

if __name__ == "__main__":
    main()

name = "Darren"

print("Hello {}!".format(name))
# This puts the String value of the name in the curly brackets usiing format function.
# 1. Write a program that takes a name as user input and prints
# "Hello name".
# 2. Create a variable called x and set it to 10. Print x to the
# console.
# 3. Write a program that takes a number and tells the user if the
# number is greater than 10, less than 10, or equal to 10. Don't
# forget to convert the string into an integer.
# 4. Write a program that takes a number as a user input and tells
# the user if it is even or odd.
# 5. Create a list and write a program that prints each individual
# element to the console.
# 6. Write a program that uses a loop fill an empty list with 10
# numbers and prints the list to the console. The numbers can
# be random or simply put in the numbers 0-9 or 1-10 in
# ascending order.
# 7. Write a program that takes a number as user input and tells
# you how many numbers in a list are less than the number that
# the user gave.
# 8. Write a program that keeps asking the user to enter a word.
# For each word that the user enters, the program prints out
# each letter in the word on a new line. When the user enters
# “s
x = 10
print(x)
strInput = input("Please enter a number:")
intInput = int(strInput)
if intInput == 10:
    print(strInput + " is equal than 10")
elif intInput < 10:
    print(strInput + " is less than 10")
else:
    print(strInput + "is greater than 10")

if intInput%2 == 0:
    print(strInput + " is even")
else:
    print(strInput + " is odd")

test_list = [1, 2, 3, 4, 5]
lengthOfTestList = len(test_list)
for i in range(lengthOfTestList):
    print(test_list[i])

fill_list = []
for i in range(10):
    fill_list.append(i)
    print(fill_list[i])

lengthOfFillList = len(fill_list)
countOfLessNums = 0
for i in range(lengthOfFillList):
    if (intInput > fill_list[i]):
        countOfLessNums = countOfLessNums + 1
strCountOfLessNums = str(countOfLessNums)
print(strInput + " is larger than " + strCountOfLessNums + " numbers of the list")

while True:
    word = input("Enter a word:")
    wordLength = len(word)
    b = 1
    for b in range(wordLength):
        print(word[b])
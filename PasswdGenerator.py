import random

print('Welcome to password generator!\n')
WordNumber = input('Please input the number of words to use in password: ')
file = open("WordList.txt")

def getRandNumbers():
    number = []
    numbers = ""
    for x in range(int(WordNumber)):
        for i in range(5):
            digit = random.randint(1,6)
            numbers += str(digit)
        number.append(str(numbers))
        numbers = ""
    return number

numbers = getRandNumbers()
print(numbers)


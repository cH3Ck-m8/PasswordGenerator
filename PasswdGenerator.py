import random

print('Welcome to password generator!\n')

#file = open("WordList.txt")

def getRandNumbers():
    number = []
    numbers = ""
    WordNumber = input('Please input the number of words to use in password: ')
    for x in range(int(WordNumber)):
        for i in range(5):
            digit = random.randint(1,6)
            numbers += str(digit)
        number.append(str(numbers))
        numbers = ""
    return number

numbers = getRandNumbers()

for x in numbers:
    with open("WordList.txt", "rt") as file:
        wordList = file.read()
        lines = wordList.split("\n")
        for i in lines:
            values = i.split('\t')
            if values[0] == x:
                print(values[1])
                
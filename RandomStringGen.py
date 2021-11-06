import random

def generateRandomCharacter(mode: int):
    output = ""
    
    if mode == 1: # Numbers
        output += chr(random.randint(48, 57))
    elif mode == 2: # Uppercase letters
        output += chr(random.randint(65, 90))
    elif mode == 3: # Lowercase letters
        output += chr(random.randint(97, 122))
    elif mode == 4: # Symbols
        submode = random.randint(1, 3)
        if submode == 1:
            output += chr(random.randint(33, 47))
        elif submode == 2:
            output += chr(random.randint(91, 96))
        elif submode == 3:
            output += chr(random.randint(123, 126))
    else: # Unknown
        m = random.randint(1, 4)
        output = generateRandomCharacter(m)

    return output

def generateRandomWord(length: int):
    output = ""
    for i in range(length):
        output += generateRandomCharacter(random.randint(1, 4))
    return output
    
def randomWordMatch():
    length = int(input("Enter the length of this randomly generated text: "))
    matchWord = input("Enter the word you want to match: ")

    validMatchWord = False
    while not validMatchWord:
        if len(matchWord) != length:
            matchWord = input("Enter the word you want to match (make sure the length matches the rand word length!): ")
        else:
            validMatchWord = True

    output = ""

    attempts = 0
    wordAttempts = []

    while output != matchWord:
        output = generateRandomWord(length)

        for word in wordAttempts:
            if word == output:
                continue
        
        wordAttempts.append(output)
        attempts += 1
        print("Attempt #" + str(attempts) + ":", output)

length = int(input("Enter the length of this randomly generated text: "))
saveToFile = input("Would you like to save this text to a file? (y/n)")
if saveToFile == "y" or saveToFile == "Y":
    file = input("File name: ")
    with open(file, mode='w') as f:
        print(generateRandomWord(length), file=f)
else:
    print("Your random text is:", generateRandomWord(length))

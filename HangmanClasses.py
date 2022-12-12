class isItAWord:
    #a class which will check userInput from determineGameWord module on Hangman.py
    def __init__(self, word):
        #initialize attributes
        self.word = word
        #if this variable is true, it means there are special characters or numbers in the word
        self.status = True
        self.letter = False

    def checkIfItIsALetter(self):
        #this method ensures the input is 1 character long and a letter
        if(self.word.isalpha() and len(self.word) == 1):
            self.letter = True

class dashFormat:
    def __init__(self, word):
        #initialize attributes
        self.word = word
#a method that will print the dash format once the game has started
    def printDashes(self):
        print(" ")
        dashes = ""
        for i in range(len(self.word)):
            dashes += "_ "
        #find the number of spaces and apostraphies using a for loop and add them to a dictionary with the character as the value and its index as the key
        specialCharacterDict = {}
        index = 0
        for char in self.word:
            if(char == " " or char == "-"):
                specialCharacterDict[index] = char
            index += 1
        #for every element is specialCharacterDict, alter the dashes string
        for index, char in specialCharacterDict.items():
            #now delete dashes where space(s) or dashes should exist and put a space there
            #multiplying index by 2 in slicing because 1 underscore counts as two character because of the space that follows it
            dashes = dashes[0:index * 2] + char + dashes[index * 2 + 1:]
        print(dashes)
        return dashes



    #@param dashes is the string that is currently being displayed during the game, letter is the letter that has been correctly guessed, and index is the letter's index in the word(can be more than on)
    def printLettersAndDashes(self, dashes, letter, index = []):
        #this method will add correctly guessed letters to dashes string

        for i in range(len(index)):
            #if index == 0, meaning the correctly guessed letter is the first letter of the word, add it to front of the dashes string(capitalized since its the first letter in the word), then add the rest of the dashes string with the first underscore sliced out
            if(index[i] == 0):
                dashes = letter.upper() + dashes[1:]
            else:
                #if the letter guessed starts a word, capitalize it
                if(dashes[index[i] * 2 - 2] == "_" or dashes[index[i] * 2 - 2].isalpha() == True):
                    #if index[i] is before any spaces or dashes    #did index * 2 + 1 to delete unneeded underscores/spaces
                    dashes = dashes[0:index[i] * 2] + letter + dashes[index[i] * 2 + 1:]
                else:
                    #if index[i] is befo  re any spaces or dashes    #did index * 2 + 1 to delete unneeded underscores/spaces
                    dashes = dashes[0:index[i] * 2] + letter.upper() + dashes[index[i] * 2 + 1:]
        print(dashes)
        return dashes

from random import randint
from HangmanClasses import isItAWord
from HangmanClasses import dashFormat
def main():
    #run the game until the user enters 'n' for the startAnotherGame input once the round ends
    startAnotherGame = "y"
    while(startAnotherGame.lower() != "n"):
        gameWord = determineGameWord()
        chancesRemaining = 10
        print("\n\nChances Remaining: " + str(chancesRemaining))
        #use the dashFormat class to print out the dashes or spaces if they are present
        word = dashFormat(gameWord)
        dashesString = word.printDashes()
        #because there can be multiple missed letters at a time, add all of them to a list
        missedLetters = []
        #because a user can input a correctly guessed letter again, add said letters to a list and use that to prevent this situation
        correctlyGuessedLetters = []
        #this code below is everything needed to complete the game from the start of round 1 to the end, so put it in a while loop that ends when chancesRemaining equals 0
        while True:
            letterGuess = guessLetter(gameWord, missedLetters, correctlyGuessedLetters, dashesString, chancesRemaining)
            isLetterInWord, indexList = LetterInWord(letterGuess, gameWord, correctlyGuessedLetters)
            #if isLetterInWord is false, subtract 1 from chancesRemaining and call printOnlyDashes method from dashFormat class
            if(isLetterInWord == False):
                chancesRemaining -= 1
                if(chancesRemaining == 0):
                    break
                else:
                    #display the chances remaining and any missed letters
                    missedLetters.append(letterGuess)
                    chancesAndMissedLetters(chancesRemaining, missedLetters)
                    print(dashesString)
            #if isLetterInWord is true, print dashes with the correctly guessed letter
            else:
                #display chances remaining and any missed Letters
                chancesAndMissedLetters(chancesRemaining, missedLetters)
                #call printLettersAndDashes method from dashFormat class to print out new display!!!!
                newDisplay = dashFormat(gameWord)
                dashesString = newDisplay.printLettersAndDashes(dashesString, letterGuess, indexList)
                if("_" in dashesString):
                    continue
                else:
                    #this marks the end of the game, and display whether the user won or lost the game
                    if(chancesRemaining > 0):
                        print("\n\nCongragulations! You Won!!!!!!")
                    else:
                        print("\n\nGame over. The word/phrase was: " + gameWord.title() + ". Better luck next time!!!")
                    break
        #ask the user if they want to play again?
        startAnotherGame = input("\n\nDo you want to play again?(y/n): ")

#this method will determine the word the game will use
def determineGameWord():
    print("Welcome! \n\n-In this game of hangman, you(the user) can choose from our randomn list that contains the names of NFL teams or famous hollywood actors. \n\n-You will have 10 chances to figure out the word or phrase, using letters as guesses along the way. \n\n-Note: \n\t*Only enter lower case letters as guesses \n\t*The only special characters allowed in words/phrases are spaces or dashes \n\n-Good luck!")
    while True:
        #use a while loop to determine the word that'll be used in the game
        NFLTeams = ["Tampa Bay Bucaneers", "Green Bay Packers", "Dallas Cowboys", "New York Giants", "Arizona Cardinals", "Philadelphia Eagles", "Minnesota Vikings", "Buffalo Bills", "Kansas City Chiefs", "Las Vegas Raiders", "Miami Dolphins", "Seattle Seahawks", "Detroit Lions"]
        hollywoodActors = ["Tom Cruise", "Will Smith", "Johnny Depp", "Tom Hanks", "Jason Statham", "Tom Cruise", "Angelina Jolie", "Robert Downey Jr", "Dwayne Johnson", "Brad Pitt", "Chris Evans", "Keanu Reeves", "Ryan Reynolds"]
        #since the prompt that is coming up requires a number, use a try except block in case the user enters a letter
        try:
            userDecision = int(input("\n\nDo you want the name of a NFL Team(Enter '1') or an actor(Enter '2')?  "))
            if(userDecision == 1):
                #generate a number based on the number of NFL teams in the NFLTeams list, then pick one of the phrases in the list
                randomNumber = randint(0, len(NFLTeams) - 1)
                gameWord = NFLTeams[randomNumber]
                break
            elif(userDecision == 2):
                #generate a number based on the number of actors in the hollywoodActors list, then pick one of the names in the list
                randomNumber = randint(0, len(hollywoodActors) - 1)
                gameWord = hollywoodActors[randomNumber]
                break
            #if user input isn't 'y' or 'n', prompt them again
            else:
                print("\n\nInput wasn't '1' or '2'. Please try again.")
        except ValueError:
            print("\n\nInput must be '1' or '2'. Please try again.")

    return gameWord.lower() #@return gameWord.lower() which holds the word the game will use

def guessLetter(gameWord, missedList, correctList, dashesString, chancesRemaining):
    #this mehtod will complet one round of the game

    #use a while loop to ensure the guess is a letter and hasn't been guessed already
    while True:
        letterGuess = input("\n\nYour guess(one letter only): ")
        #use the checkWord class to ensure it is a letter
        check = isItAWord(letterGuess)
        check.checkIfItIsALetter()
        #check if the user input is a letter
        if(check.letter):
            #make sure letterGuess isn't in the lists given in the function parameters, which means it has not been guessed yet
            if(letterGuess not in missedList and letterGuess not in correctList):
                break
            else:
                print("\n\nYou have already tried this letter. Guess again!")
                print("\n\nChances Remaining: " + str(chancesRemaining))
                print("\n\n" + dashesString)
        else:
            print("\n\nNot a valid character. Please try again. ")
            continue
    return letterGuess

def LetterInWord(letter, word, correctlyGuessedLetters):
    #this method will determine whether the letter the user guessed is in their word, and its index using .find()

    #find all instances of the letter and add it to a list
    indexList = []
    if letter in word:
        letterInWord = True
        index = -1
        for char in word:
            index += 1
            if(letter == char):
                indexList.append(index)
                correctlyGuessedLetters.append(letter)
    else:
        letterInWord = False
        #make letterIndex variable -1, so it doesn't correlate to any of the letters in the word
        letterIndex = -1
    return letterInWord, indexList

#this method will display any missed letters and the amount of chances remaining at the start of a new round
def chancesAndMissedLetters(chancesRemaining, list):
    #if list has no contents
    if(len(list) == 0):
        print("\n\nMissed Letters: None")
    #if the missedLetters list isn't empty
    else:
        print("\n\nMissed Letters: ")
        for missedLetter in list:
            print("\t" + missedLetter)

    print("\n\nChances Remaining: " + str(chancesRemaining) + "\n\n")


main()

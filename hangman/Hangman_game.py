# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    print(lettersGuessed)
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    T = ""
    for u in secretWord:
        if u in lettersGuessed:
            T += u
        else:
            T+="_ "
    return T


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = string.ascii_lowercase
    delta = ""
    for letter in alphabet:
        if letter not in lettersGuessed:
            delta += letter
    print(delta)
    return delta

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    Welcome to the game, Hangman!
    '''
    # FILL IN YOUR CODE HERE...
    print(" Welcome to the game, Hangman!")
    print("I am thinking of a word ",len(secretWord)," letters long.")
    num_of_guess = 7
    lettersGuessed = []
    wrong_letters = []
    while num_of_guess > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("you have ",num_of_guess,"guesses left")
        print("Available letters: ",getAvailableLetters(lettersGuessed))
        n = input("please guess a letter: ")
        
        
        
        if n in secretWord and n not in lettersGuessed:
            lettersGuessed.append(n)
            print(lettersGuessed)
            print("Good guess: ",getGuessedWord(secretWord, lettersGuessed))  
            
           
        elif n in getAvailableLetters(lettersGuessed):
            if n not in wrong_letters:
                num_of_guess -= 1
                wrong_letters.append(n)
            print("Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed))
            
        
        elif n in lettersGuessed :
            print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))

        
        else:
            print("please insert an english alphabet ",getGuessedWord(secretWord, lettersGuessed))
    
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
   
    else:
        print("Sorry, you ran out of guesses. The word was ", secretWord)
            



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

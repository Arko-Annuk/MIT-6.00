#Problem Set 5 - Ghost
#Name: Arko Annuk
#Time: 4h

#TODO FOR TÜ TTL PROJECT: Add comments, shape the code better, consider adding a GUI

import string
import sys

wordFrag = []
wordlist = []



WORDLIST_FILENAME = "/home/gabriel/Documents/ps5/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    global wordlist
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  "), len(wordlist), "words loaded."
    return wordlist




def isCharValid(char):
    if char in string.ascii_letters and len(char) == 1:
        return True
    else:
        return False
    
        
def addCharFrag(char):
    global wordFrag
    wordFrag.append(char.lower())
    return wordFrag

    
def isFragWord(wordFragList):
    wordFragString = ''.join(wordFrag)
    if wordFragString in wordlist and len(wordFragString) >= 4:
        return True
    else:
        return False
    
def isFragViable(wordFragList):
    #Can words be formed with the given CHARS in wordlist?
    wordFragString = ''.join(wordFrag)
    for word in wordlist:
        if word.startswith(wordFragString):
            return True
    return False

def playerOneTurn():
    char = input('Please enter an alphabetical character as a string ')
    if isCharValid(char):
        addCharFrag(char)
        if isFragViable(wordFrag) == True and isFragWord(wordFrag) == False:
            print ('Player One adds ', char, ', to the word fragment. The fragment is now: ', wordFrag)
        else:
            print ('Player One input creates either an invalid fragment or a word, it loses')
            sys.exit()
    else:
        print ('Player One input is not valid, it loses')
        sys.exit()

def playerTwoTurn():
    char = input('Please enter an alphabetical character as a string ')
    if isCharValid(char):
        addCharFrag(char)
        if isFragViable(wordFrag) == True and isFragWord(wordFrag) == False:
            print ('Player Two adds ', char, ', to the word fragment. The fragment is now: ', wordFrag)
        else:
            print ('Player Two input creates either an invalid fragment or a word, it loses')
            sys.exit()
    else:
        return ('Player Two input is not valid, it loses')
        sys.exit()

def playGhost():
    while True:
        cmd = input('Enter 1 to start playerOneTurn, enter 2 to start playerTwoTurn ')
        if cmd == '1':
            playerOneTurn()
            return playGhost()
        elif cmd == '2':
            playerTwoTurn()
            return playGhost()
        else:
            print ('Invalid command.')
            return playGhost()

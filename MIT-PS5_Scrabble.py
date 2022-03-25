#Problem Set 5 - Scrabble
#Name: Arko Annuk
#Time: 8h 10min

import random
import string

wordlist = []
totalScore = []
sumScore = []

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

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


#Took me 2h to implement
def get_word_score(word, n):
    score = []
    global scoreSum
    global totalScore
    if word in wordlist and len(word) == n:
        score.append(50)
    if word in wordlist:
        for letter in word:
            score.append(SCRABBLE_LETTER_VALUES[letter])
    #print (sum(score))
    totalScore.append(sum(score))
    sumScore.append(sum(totalScore))

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter,end = " ") # print all on the same line
            

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 of the letters in the hand should be VOWELS.
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
    n: int >= 0
    returns: dictionary (string -> int)
    """    
    hand={}
    num_vowels = n // 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand

#Took me 2 hours to implement
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many instances of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for char in word:
        if char in hand:
            hand[char] -= 1
        if hand[char] == 0:
            del hand[char]
    return hand

#Took me 10 minutes to implement 
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    word: string
    hand: dictionary (string -> int)
    word_list: list of strings
    """
    for char in word:
        if char in hand and word in wordlist:
            return ('True')
    else:
        return ('False')

#Took me 2 hours 20 min to implement
def play_hand(hand, wordlist):
    print ('Current Hand:')
    display_hand(hand)
    action = input('\nEnter word, or a . to indicate that you are finished:')
    if action == '.':
        if sumScore == []:
            return 'Your score is 0 points' 
        else:
            return 'Your score is:', sumScore[-1], 'points'
    if is_valid_word(action, hand, wordlist) == 'True':
        get_word_score(action, HAND_SIZE)
        print (action, 'earned', totalScore[-1], 'points. Total points:', sumScore[-1])
        update_hand(hand, action)
        if hand == {}:
            return 'Your final score is:', sumScore[-1], 'points'
        else:
            return play_hand(hand, wordlist)
    else:
        print ('Your word is not valid, please try again')
        return play_hand(hand, wordlist)

#Took me 20 minutes to implement
def play_game(word_list):
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            print ('Game Ended: Your final score is:', sumScore[-1], 'points')
            break
        else:
            print ('Invalid command.')
    

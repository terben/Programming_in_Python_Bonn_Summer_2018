# module for the physics 718 word game.
# Large parts of this file were obtained from
# a somilar problem of the MIT 6.0001 OCW course.

# Original file by: Kevin Luu <luuk> and Jenna Wiens <jwiens>

# YOUR NAME HER PLEASE:

import numpy
import random
import string

# module constants
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words_alpha.txt"

def load_words(filename=WORDLIST_FILENAME):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(filename, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")

    return wordlist

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


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n, letter_values=SCRABBLE_LETTER_VALUES):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of
    letters, or the empty string "". You may not assume that the
    string will only contain lowercase letters, so you will have to
    handle uppercase and mixed case strings appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    letter_values: dict of values for lower case letters (and the '*')
    returns: int >= 0

    """

    # make sure that the whole word is in lowercase first
    word = word.lower()
    word_score = 0

    if word != "":
        for letter in word:
            word_score += letter_values[letter]

        word_score *= max(1, 7 * len(word) - 3 * (n - len(word)))

    return word_score

#
# Make sure you understand how this function works and what it does!
#
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
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n, vowels=VOWELS, consonants=CONSONANTS):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    vowels: string of vowels
    consonants: string of consonants
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(numpy.ceil(n / 3))
    num_consonants = n - num_vowels

    # hand a wildcard for a vowel:
    hand['*'] = 1
    num_vowels = num_vowels - 1

    for i in range(num_vowels):
        x = random.choice(vowels)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_consonants):
        x = random.choice(consonants)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    word = word.lower()
    new_hand = hand.copy()

    for letter in word:
        if letter in new_hand:
            new_hand[letter] = max(0, new_hand[letter] - 1)

    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()
    is_valid = True

    # first test whether the word is directly in the wordlist
    # or when we substitute a joker with a vowel:
    word_exists = False
    if ('*' not in word) and (word in word_list):
        word_exists = True
    else:
        for vowel in VOWELS:
            if word.replace('*', vowel) in word_list:
                word_exists = True

    if word_exists == True:
        letters_dict = get_frequency_dict(word)

        for letter in letters_dict:
            if letters_dict[letter] > hand.get(letter, 0):
                is_valid = False
    else:
        is_valid = False

    return is_valid

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    hand_length = 0
    for key in hand:
        hand_length = hand_length + hand[key]

    return hand_length

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

        # Display the hand

        # Ask user for input

        # If the input is two exclamation points:

            # End the game (break out of the loop)


        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)

            # update the user's hand by removing the letters of their inputted word


    # Hand is finished (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

    hand_score = 0

    print("Current hand: ", end=" ")
    display_hand(hand)

    user_word = input('Enter word, or "!!" to finish this hand: ')
    user_word = user_word.strip()
    handlen = calculate_handlen(hand)

    while user_word != "!!" and handlen > 0:
        if is_valid_word(user_word, hand, word_list) == True:
            score = get_word_score(user_word, handlen)
            hand_score = hand_score + score
            print('"{0}" earned you {1} points'.format(user_word, score))
            print('Total points for this hand: {0}'.format(hand_score))
        else:
            print("This is not a valid word! Please try again")

        hand = update_hand(hand, user_word)
        handlen = calculate_handlen(hand)

        if handlen > 0:
            print()
            print("Current hand: ", end=" ")
            display_hand(hand)

            user_word = input('Enter word, or "!!" to finish this hand: ')
            user_word = user_word.strip()

    if user_word == "!!":
        print("You finished this hand. Total score: {0}".format(hand_score))
    else:
        print("You ran out of letters. Total score: {0}".format(hand_score))

    print()
    return hand_score

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter, vowels=VOWELS, consonants=CONSONANTS):
    """
    Allow the user to replace all copies of one letter in the hand
    (chosen by user) with a new letter chosen from the VOWELS and
    CONSONANTS at random. The new letter should be different from
    user's choice, and should not be any of the letters already in the
    hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)

    """

    # we need to do nothing if the letter is not in the hand:
    if letter in hand:
        # choose arbitrarily a letter out of vowels and consonants
        # and do it as long as the new letter is in the hand already.
        #
        # NOTE: We could also argue that we substitute a vowel with
        #       a vowel only and a consonant with a consonant only.
        #       Both solutions are fine.
        letters = consonants + vowels

        newletter = letters[random.randint(0, len(letters) - 1)]
        while newletter in hand:
            newletter = letters[random.randint(0, len(letters) - 1)]

        # the new, returned hand should not modify the original hand.
        # Hence, we need a copy:
        newhand = hand.copy()

        newhand[newletter] = newhand[letter]
        newhand.pop(letter)

        hand = newhand

    return hand

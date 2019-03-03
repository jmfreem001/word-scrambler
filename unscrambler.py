from itertools import permutations as pm

# TODO: Update to show all english words from letter combinations like for scrabble.
# This would mean updating combinations variable and pribably making it its own function.

def unscramble():
    """Takes a user's input and outputs possible answers"""
    # Accept input of scrambled words and break into letters.
    scrambled_word = input("Please enter a word to be unscrambled: ")
    scrambled_letters = [letter for letter in scrambled_word]

    # Get all unique letter combinations into a list
    combinations = list(pm(scrambled_letters,len(scrambled_letters)))
    # TODO: Need to refactor to be simpler
    guesses = []
    for combo in combinations:
        string_guess = ''.join(combo)
        guesses.append(string_guess)
    guesses = set(guesses) # Elimiate potential duplicates

    # Assign english words to a variable.
    words = set(get_english_words('words_alpha.txt'))
    # Checks if word in English language and print potential answers
    answers = guesses.intersection(words)
    if answers:
        print("\nThe english words that can be made from those letters are:")
        for answer in answers:
            print("-" + answer)
    else:
        print("\nCould not make a word with those letters.")

def get_english_words(file):
    """Pulls txt file with a list"""
    doc = open(file,'r')
    # TODO: Get this function to accept a file length so that the outputted list just outputs words that match that length
    list = [word.rstrip() for word in doc]

    return list

unscramble()

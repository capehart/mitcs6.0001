# Problem Set 2, hangman.py
# Name: AC Capehart
# Collaborators: None
# Time spent: ~2 hours

import random
import string


class HangmanGame:
    def __init__(self, secret_word=None, allow_hints=False):
        self.wordlist = load_words()
        self.secret_word = secret_word or choose_word(self.wordlist)
        self.letters_guessed = []
        self.guesses_remaining = 6
        self.warnings_remaining = 3
        self.separator = "-" * 10
        self.allow_hints = allow_hints
        self.guessed_word = get_guessed_word(self.secret_word, self.letters_guessed)
        print("Welcome to the game Hangman!")
        print(f"I am thinking of a word that is {len(self.secret_word)} letters long.")
        print(self.separator)
        self.play()

    def print_status(self):
        print(f"You have {self.guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(self.letters_guessed)}")

    def guess(self, letter):
        self.letters_guessed.append(letter)
        if letter in self.secret_word:
            return True
        return False

    def get_guesses_remaining(self):
        return self.guesses_remaining

    def get_warnings_remaining(self):
        return self.warnings_remaining

    def decrement_guesses_remaining(self, qty=1):
        self.guesses_remaining -= qty

    def decrement_warnings_remaining(self):
        self.warnings_remaining -= 1

    def play(self):
        while self.guesses_remaining > 0:
            self.print_status()
            guess = input("Please guess a letter: ").lower()
            if guess in self.letters_guessed:
                if self.get_warnings_remaining() > 0:
                    self.decrement_warnings_remaining()
                    print(
                        "Oops! You've already guessed that letter.Oops! "
                        "You've already guessed that letter. You now "
                        "have {self.get_warnings_remaining()} warnings left. "
                        f"{get_guessed_word(self.secret_word, self.letters_guessed)}")
                else:
                    self.decrement_guesses_remaining()
                    print(
                        "Oops! You've already guessed that letter. "
                        "You have no warnings left so you lose one guess. "
                        f"{get_guessed_word(self.secret_word, self.letters_guessed)}")
                continue
            if guess not in string.ascii_lowercase:
                if self.allow_hints and guess == "*":
                    show_possible_matches(get_guessed_word(self.secret_word, self.letters_guessed), self.wordlist)
                    continue
                if self.get_warnings_remaining() > 0:
                    self.decrement_warnings_remaining()
                    print(
                        "Oops! That is not a valid letter. "
                        f"You have {self.get_warnings_remaining()} warnings left: "
                        f"{get_guessed_word(self.secret_word, self.letters_guessed)}")
                else:
                    self.decrement_guesses_remaining()
                    print(
                        "Oops! That is not a valid letter. "
                        "You have no warnings left so you lose one guess: "
                        f"{get_guessed_word(self.secret_word, self.letters_guessed)}")
                continue

            result = self.guess(guess)
            if result:
                print(f"Good guess: {get_guessed_word(self.secret_word, self.letters_guessed)}")
            else:
                print(
                    f"Oops! That letter is not in my word: {get_guessed_word(self.secret_word, self.letters_guessed)}")
                if guess in "aeiou":
                    self.decrement_guesses_remaining(qty=2)
                else:
                    self.decrement_guesses_remaining()

            if is_word_guessed(self.secret_word, self.letters_guessed):
                print("Congratulations, you won!")
                print(f"Your total score for this game is: {self.get_guesses_remaining() * len(set(self.secret_word))}")
                break
        if self.guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {self.secret_word}")


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    wordlist_filename = "words.txt"

    print("Loading word list from file...")
    in_file = open(wordlist_filename, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    """
    Take a list of letters that have been guessed and return True
    if all the letters in the secret word are accounted for

    :param secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    :param letters_guessed:  list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    :return: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    secret_word_set = set(secret_word)
    letters_guessed_set = set(letters_guessed)
    return secret_word_set.issubset(letters_guessed_set)


def get_guessed_word(secret_word, letters_guessed):
    """
    Given a target word and a list of letters guessed, return a string that shows the letters in place
    with a "_ " for any letters not yet guessed
    :param secret_word: string, the word the user is guessing
    :param letters_guessed: list (of letters), which letters have been guessed so far
    :return: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += "_ "
    return guessed


def get_available_letters(letters_guessed):
    """
    Given a list of letters guessed, return a string of the remaining letters in the alphabet
    :param letters_guessed: list (of letters), which letters have been guessed so far
    :return: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available


def hangman(secret_word=None):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    HangmanGame(secret_word)


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False
        if my_word[i] == "_" and other_word[i] in my_word:
            return False
    return True


def show_possible_matches(my_word, wordlist):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    matched = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched.append(word)
    if matched:
        print(" ".join(matched))


def hangman_with_hints(secret_word=None):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    HangmanGame(secret_word, allow_hints=True)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    hints = input("Do you want to play with hints? (y/N): ").lower()
    if hints and hints.startswith("y"):
        print("Hints are enabled. Use * to show possible matches.")
        hangman_with_hints()
    else:
        hangman()

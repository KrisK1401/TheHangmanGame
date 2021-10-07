"""
Simple hangman game with 5 lives and couple of harsh feedbacks from the program
"""

import random
from vocabulary import words
from drawing import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def string():
    pass


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 5

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b']) --> 'a b'
        print('You have', lives, 'lives remaining and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie L - S T)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # punishes the user by taking one life away
                print('\nYour letter,', user_letter, 'is not in it you duffus')

        elif user_letter in used_letters:
            print('\nAre you alright? You have already said that letter')

        else:
            print('\nEmmm...what is that?')

    # gets here when len(word_letters) == 0 OR when user lost all the lifes
    if lives == 0:
        print(lives_visual_dict[lives])
        print('YOU-LOSE, better luck next time. The word was', word)
    else:
        print('Pff...that was pure luck')


if __name__ == '__main__':
    hangman()

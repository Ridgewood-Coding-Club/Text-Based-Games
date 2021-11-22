import os

from words import get_word

correct_letters = []
guessed_letters = []
lives = 5
word = get_word()  # Gets word from words.py
hidden_word = ''


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def get_letters():
    global guessed_letters  # Grants access to guessed_letters
    result = ''  # creates an empty string
    for _ in guessed_letters:  # loops through the list and appends it to result followed by a comma
        result += _ + ', '
    return result


if __name__ == '__main__':
    for _ in word:
        hidden_word += '_'  # hides the word (replaces letters with "_"'s)
    while '_' in hidden_word:  # while there are unknown letters game will continue to go.
        if lives > 0:  # lives check
            clear_console()
            # print(word) prints the answer
            print('Lives: ' + str(lives))
            print('Your word is: ' + hidden_word)
            print('Your guessed letters: ' + get_letters())
            letter = input('Guess a letter: ')
            if letter not in guessed_letters:  # checks if you guessed the letter
                guessed_letters.append(letter)
                if letter in word:  # checks if the letter is in the word
                    correct_letters.append(letter)  # adds to correct letters
                    hidden_word = ''
                    for let in word:
                        if let not in correct_letters:
                            hidden_word += '_'
                        else:
                            hidden_word += let
                else:
                    # print('That letter is incorrect!')
                    lives -= 1
            else:
                print('You guessed that letter already!')
        else:
            print('Out of lives. You lose! The word was: ' + word)
            break  # breaks out of while loop
    if lives != 0:
        print('You win! The word was: ' + word)

# Quickly put together version of hangman.

from random import randint
word_list = ['cat', 'dog', 'goose', 'fire', 'bulldozer', 'alfalfa', 'myth', 'website',
             'grapes', 'spider', 'fables']
display = []
hidden = []
correct_guesses = []
wrong_guesses = []
import os


# randomly select a word based on index position in the word list
def word_select():
    i = randint(0, (len(word_list) - 1))
    secret_word = word_list[i]
    hide_word(secret_word)


# takes secret word as argument and creates a blank display
def hide_word(secret_word):
    x = 0
    for letter in secret_word:
        display.append(" - ")
        hidden.append(secret_word[x])
        x += 1
    print display
    make_guess(secret_word)
#test    print hidden


# asks for raw input, confirms input to some extend (more control required)
# checks to see if letter already guessed, right or wrong
# if already guessed, make_guess() is rerun
# if valid and novel guess, guess is fed as argument to check_guess()
def make_guess(secret_word):
    print "\n" * 10
# replace breaks with ascii hangman
    print display
    print "\n"
    print "You have %s guesses left..." %(10 - len(wrong_guesses))
    print "\n"
    guess = raw_input("Guess a letter: ")
    if len(guess) < 1:
        make_guess(secret_word)
    if len(guess) > 1:
        make_guess(secret_word)
    if guess in correct_guesses:
        print "You already guessed that and it was right."
        make_guess(secret_word)
    if guess in wrong_guesses:
        print "you already guessed that and it was wrong."
        make_guess(secret_word)
    else:
        check_guess(guess, secret_word)

# iterates through word based on 0-len(word) range and incrementation of local variable
# if guess is correct, the letter will replace blanks in the display
# if guess is incorrect, letter is added to a wrong list
# length of wrong list determines game-end
# until game-end, make_guess() and check_guess() are cycled
def check_guess(guess, secret_word):
    l = 0
    while l <= (len(hidden) - 1):
        if guess == hidden[l]:
            display[l] = guess
            correct_guesses.append(guess)
            l += 1
            print display
        else:
            l += 1
    if " - " not in display:
        win_game(secret_word)
    if guess not in hidden:
        if guess not in wrong_guesses:
# create a variable to move along ascii hangman art
            wrong_guesses.append(guess)
            if len(wrong_guesses) == 10:
                end_game(secret_word)
        print wrong_guesses
        print "WRONG! guess again"
        make_guess(secret_word)
    else:
        print display
        make_guess(secret_word)

# end of game function
# shows secret word
# prompts for new game or quit
def end_game(secret_word):
    print "\n" * 10
    print "game over"
    print "The secret word was %s " %(secret_word)
    again = raw_input("play again or press 'q' to quit")
    if again == 'q':
        quit()
    else:
        word_select()

def win_game(secret_word):
    print "\n" * 10
    print " You correctly guessed %s ! GREAT JOB!" %(secret_word)
    again = raw_input("play again or press 'q' to quit")
    if again == 'q':
        quit()
    else:
        word_select()


word_select()
from random import randint
word_list = ['cat', 'dog', 'goose', 'fire', 'bulldozer', 'alfalfa', 'myth', 'website',
             'grapes', 'spider', 'fables']

display = []
hidden = []
correct_guesses = []
wrong_guesses = []
draw = 0



import os


# randomly select a word based on index position in the word list
def word_select(draw):
    i = randint(0, (len(word_list) - 1))
    secret_word = word_list[i]
    hide_word(draw, secret_word)


# takes secret word as argument and creates a blank display
def hide_word(draw, secret_word):
    x = 0
    for letter in secret_word:
        display.append(" - ")
        hidden.append(secret_word[x])
        x += 1
    print display
    make_guess(draw, secret_word)
#test    print hidden


# asks for raw input, confirms input to some extend (more control required)
# checks to see if letter already guessed, right or wrong
# if already guessed, make_guess() is rerun
# if valid and novel guess, guess is fed as argument to check_guess()
def make_guess(draw, secret_word):
    print "\n" * 7
    hangman(draw)
# replace breaks with ascii hangman
    print display
    print "\n"
    print "You have %s guesses left..." %(7 - len(wrong_guesses))
    print "\n"
    guess = raw_input("Guess a letter: ")
    if guess.isalpha() == False:
        print "Please enter a letter..."
        make_guess(draw, secret_word)
    guess = guess.lower()
    if len(guess) < 1:
        print "Please enter one letter..."
        make_guess(draw, secret_word)
    if len(guess) > 1:
        print "Please enter only one letter..."
        make_guess(draw, secret_word)
    if guess in correct_guesses:
        print "You already guessed that and it was right."
        make_guess(draw, secret_word)
    if guess in wrong_guesses:
        print "you already guessed that and it was wrong."
        make_guess(draw, secret_word)
    else:
        check_guess(draw, guess, secret_word)

# iterates through word based on 0-len(word) range and incrementation of local variable
# if guess is correct, the letter will replace blanks in the display
# if guess is incorrect, letter is added to a wrong list
# length of wrong list determines game-end
# until game-end, make_guess() and check_guess() are cycled
def check_guess(draw, guess, secret_word):
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
#           create a variable to move along ascii hangman art
            wrong_guesses.append(guess)
            draw += 1
            if len(wrong_guesses) == 7:
                end_game(secret_word)
        print wrong_guesses
        print "WRONG! guess again"
        make_guess(draw, secret_word)
    else:
        print display
        make_guess(draw, secret_word)

# end of game function
# ends when player out of guesses
# shows secret word
# prompts for new game or quit
def end_game(secret_word):
    print "\n" * 10
    hangman(7)
    print "\n" * 2
    print "GAME OVER"
    print "The secret word was %s " %(secret_word)
    again = raw_input("play again or press 'q' to quit")
    if again == 'q':
        quit()
    else:
        empty_lists()
        word_select(0)

# win game function
# game ends with complete word guessed
# victory art displayed
# option for new game or quit
def win_game(secret_word):
    print "\n" * 10
    hangman(8)
    print "\n" * 2
    print " You correctly guessed %s ! GREAT JOB!" %(secret_word)
    again = raw_input("play again or press 'q' to quit")
    if again == 'q':
        quit()
    else:
        empty_lists()
        word_select(0)

# empties all lists created during game play to start fresh
# uses slice function [:] means at all indexes
def empty_lists():
    display[:] = []
    hidden[:] = []
    correct_guesses[:] = []
    wrong_guesses[:] = []

# a series of ascii hangman designs leading up to a victory or defeat
# variable "draw" used as reference for series of "if ==" checks
# print and move on
def hangman(draw):
    if draw == 0:
        print " _____"
        print " |   |"
        print "     |"
        print "     | ()"
        print "     |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 1:
        print " _____"
        print " |   |"
        print " o   |"
        print "     | ()"
        print "     |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 2:
        print " _____"
        print " |   |"
        print " o   |"
        print " |   | ()"
        print "     |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 3:
        print " _____"
        print " |   |"
        print " o   |"
        print "/|   | ()"
        print "     |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 4:
        print " _____"
        print " |   |"
        print " o   |"
        print "/|\  | ()"
        print "     |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 5:
        print " _____"
        print " |   |"
        print " o   |"
        print "/|\  | ()"
        print "/    |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 6:
        print " _____"
        print " |   |"
        print " o   |"
        print "/|\  | ()"
        print "/ \  |-[]-"
        print "     | /\ "
        print " ========"
    if draw == 7:
        print " _____"
        print " |   |"
        print " X   |"
        print "/|\  | ()"
        print "/ \  |-[]-"
        print "DEAD!| /\ "
        print " ========"
    if draw == 8:
        print " _____"
        print " |   |"
        print "FREE!| "
        print "  O  | ()"
        print " /|\ |-[]-"
        print " / \ | /\ "
        print " ========"

# game play loop starts with word_select()
word_select(0)
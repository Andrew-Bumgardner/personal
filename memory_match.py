"""
File: py_match.py
Aythor: Andrew Bumgardner
Date: 4/28/2022
Section: 21
E-mail: andrewb7@umd.edu
Description: This program allows the user to play a modified memory game!
"""

import random

def setup_board(rows, cols, symbols_list):
    # Takes the rows and columns parameter to create an 'answer' board with
    # symbols at each spot and also returns the blank board setup as well

    answers = []
    display = []
    answer_stats = {
        'A' : 0,
        'B' : 0,
        'C' : 0,
        'D' : 0,
        'E' : 0,
        'F' : 0,
        'G' : 0,
        'H' : 0,
        'I' : 0,
        'J' : 0,
        'K' : 0,
        'L' : 0,
        'M' : 0,
        'N' : 0,
        'O' : 0,
        'P' : 0,
        'Q' : 0,
        'R' : 0,
        'S' : 0,
        'T' : 0,
        'U' : 0,
        'V' : 0,
        'W' : 0,
        'X' : 0,
        'Y' : 0,
        'Z' : 0
    }

    for y in range(cols):
        answers.append([])
        display.append([])

    for y in range(cols):
        for x in range(rows):
            random_sym = random.choice(symbols_list)
            answers[y].append(random_sym)
            display[y].append('.')

    for y in range(cols):
        for x in range(rows):
            answer_stats[answers[y][x]] += 1

    return answers, display, answer_stats

    
def game(answers, display, stats, points, total):
    # Handles all of the game parameters, includes the game loop
    # and user inputs
    blank = '.'

    flag = True
    matching = False

    while flag:
        temp = []
        for i in range(len(display)):
            print(' '.join(display[i]))
            temp.append([])
        guess = input('Enter a position to guess: ')

        guessy, guessx = guess.split()

        posx = int(guessx)-1
        posy = int(guessy)-1

        if display[posy][posx] != blank:
            print('Already guessed this spot!')

        else:
            

            if stats[answers[posy][posx]] == 1:
                print('Found all of the {}!'.format(answers[posy][posx]))
                points += 1
                display[posy][posx] = answers[posy][posx]
            else:
                matching = True
                for y in range(len(display)):
                    for x in range(len(display[y])):
                        temp[y].append(display[y][x])
                temp[posy][posx] = answers[posy][posx]

                found = 1
                letter = answers[posy][posx]

            while matching:

                for i in range(len(temp)):
                    print(' '.join(temp[i]))

                guess = input('Enter position to guess that matches' + \
                    ' {}, there are {} remaining: '.format(letter, \
                        stats[letter]-found))

                guessy, guessx = guess.split()

                posx = int(guessx)-1
                posy = int(guessy)-1

                if temp[posy][posx] != blank:
                    print('Already guessed this spot!')

                else:
                    temp[posy][posx] = answers[posy][posx]
                    if answers[posy][posx] == letter:
                        found += 1

                        if stats[letter] == found:
                            print('You have found all of the {}'\
                                .format(letter))
                            display = temp
                            matching = False
                            points += found

                    else:
                        print('No match this time: ')

                        for i in range(len(temp)):
                            print(' '.join(temp[i]))
                        matching = False
                        print('Try again!')
        if points == total:
            for i in range(len(display)):
                print(' '.join(display[i]))
            print('You win!')
            flag = False




def main():
    # sets up and runs the game
    setup = input('Enter Row, Col, Seed: ')
    row, col, seed = setup.split(', ')
    random.seed(int(seed))

    file = input('What is the symbol file name? ')

    with open(file) as f:
        symbols_string = f.readlines()

    symbols = symbols_string[0].split()

    answers, display, stats = setup_board(int(row), int(col), symbols)

    points = 0
    total = int(row) * int(col)
    
    game(answers, display, stats, points, total)



if __name__ == '__main__':

    main()




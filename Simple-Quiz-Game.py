'''
Simple Trivia Game
Programmer: Daniel
This progam will demonstrate a simple trivia game and show score right and wrong at the end. 
'''

while True:
    Incorrect = 0
    correct = 0 
    answer1 = input('Where is China capital located: ')
    if answer1  != 'Beijing':
        print('Incorrect!')
        Incorrect += 1
    else:
        print('Correct!')
        correct += 1 
        continue
    answer2 = input('Where is the nations capital in the united states: ')
    if answer2  != 'Washington D.C':
        print('Incorrect!')
        Incorrect += 1
    else:
        print('Correct!')
        correct += 1 
        continue
    answer3 = input('Who won the revolutionary war: ')
    if answer3 != 'The 13 original colonies':
        print('Incorrect!')
        Incorrect += 1
    else:
        print('Correct!')
        correct += 1 
        continue
    answer4 = input('Who is the best chess player in the world as of 2020: ')
    if answer4 != 'Magnus Carlson':
        print('Incorrect!')
        Incorrect += 1
    elif answer4 == "Magnus Carlsen":
        print('Correct!')
        correct += 1 
        break
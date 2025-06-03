'''
Simple Log in System
Programmer:Daniel
This project is about a user logging into a Account.
'''

username = "bob34"
password = "chiquita123"
limit = 3
while True:
    entered_username = input('Enter Username: ')
    if entered_username != username:
        print('Incorrect username')
        limit -= 1
        print('incorrect log in.', limit, 'Attempts remaining.')
        if limit == 0:
            print('You have reached the maximum amount of attempts. Try again later.')
            break
    entered_password= input('Enter password:')
    if entered_password != password:
        print('Incorrect password')
        limit -= 1
        print('incorrect log in.', limit, 'Attempts remaining.')
        if limit == 0:
            print('You have reached the maximum amount of attempts. Try again later.')
            break
    if entered_username == username and entered_password == password:
        print('Welcome to your account.')
        break
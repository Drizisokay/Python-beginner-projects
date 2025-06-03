'''
Simple Log in System
Programmer:Daniel
This project is about a user logging into a Account.
'''

username = "bob121"
password = "chiquita190"
limit = 3
while True:
    print(limit)
    entered_username = input('Enter Username: ')
    if entered_username != username:
        print('Incorrect username')
        limit -= 1
        print('incorrect log in.', limit, 'Attempts remaining.')
        if limit == 0:
            print('You have reached the maximum amount of attempts. Try again later.')
            break
        continue
    entered_password= input('Enter password:')
    if entered_password != password:
        print('Incorrect password')
        limit -= 1
        print('incorrect log in.', limit, 'Attempts remaining.')
        if limit == 0:
            print('You have reached the maximum amount of attempts. Try again later.')
            break
        continue
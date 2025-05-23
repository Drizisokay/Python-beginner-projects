'''
Password Checker
Programmer: Daniel
Prompts the user for a password and checks if it matches the secret password.
'''
secret_password = "bananas"
while True:
    password = input('Enter a password: ')
    if password != secret_password:
        print("You are not worthy to Enter.")
    else:
        print('You are worthy.')
        break
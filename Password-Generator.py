'''
Developer: Drizisokay

'''

import random
import string
import hashlib


def generate_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    return any(suffix == hash_suffix for hash_suffix, _ in hashes)

if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print(f"Generated password: {password}")
    if check_pwned(password):
        print("Warning: This password has been found in data breaches!")
    else:
        print("This password is safe to use.")


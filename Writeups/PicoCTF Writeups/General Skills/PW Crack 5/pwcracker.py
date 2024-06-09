import hashlib

pos_pw_list = open('dictionary.txt', 'r').read().splitlines()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

def hash_pw(pw_str):
    m = hashlib.md5()
    m.update(pw_str.encode())
    return m.digest()

def solve():
    for pw in pos_pw_list:
        if (hash_pw(pw) == correct_pw_hash):
            print(pw)
            return

solve()
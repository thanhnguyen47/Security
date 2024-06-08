import hashlib

correct_pw_hash = open("level3.hash.bin", "rb").read()

pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]

def hash_pw(pw_str):
    pw_bytes = bytearray() # initialize an empty bytearray (it's a mutable sequence of bytes)
    pw_bytes.extend(pw_str.encode()) # encode pw_str into bytes using UTF-8 (default) encoding and extends pw_bytes with these bytes.
    m = hashlib.md5() # create a new MD5 hash object `m` using hashlib.md5() fuction
    m.update(pw_bytes) # update the MD5 hash object `m` with bytes form `pw_bytes`. This processes the data and computes the hash
    return m.digest() # return the binary (non-hexadecimal) degest of the hash. it returns the hash value as a bytes object.

for pw in pos_pw_list:
    if (hash_pw(pw) == correct_pw_hash):
        print(pw, end='')
        break


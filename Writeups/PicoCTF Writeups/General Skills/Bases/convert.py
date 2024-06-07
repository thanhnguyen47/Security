import sys

s = sys.argv[1]
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
ans = 0
p = 1
try:
    for i in range(len(s) - 1, -1, -1):
        ans += int(s[i]) * p
        p*=2
    print(ans)
    print(base64_alphabet[ans], end='')
except:
    print('something went wrong')
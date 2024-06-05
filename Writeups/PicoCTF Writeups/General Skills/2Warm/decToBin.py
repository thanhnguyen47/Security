import sys 
# the command-line arguments are stored in sys.argv
# the first element (sys.argv[0]) is the script name
# the second element (sys.argv[1]) is the first argument passed after the script name

try:
    res = ''
    num = int(sys.argv[1])
    while num != 0:
        res = str(num%2) + res
        num //= 2 # use interget division instead of normal division
    print(res, end="")
except:
    print("something went wrong")

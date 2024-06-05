# 2Warm

## Overview

**Points:** 50\
**Tags:** General Skills

## Description

Can you convert the number 42 (base 10) to binary (base 2)?

## Hints

(none)

## Approach

We can write a python program named [decToBin.py](./decToBin.py) converting dec to bin like:

```python
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

```
Oke, now run it
![alt text](image.png)

## Flag

`picoCTF{101010}`

## Alternative Approach

You can use any other ways to convert it such as using online converter, manual calculating, ...\
I recommend using [CyberChef](https://cyberchef.org/) or [RapidTables](https://www.rapidtables.com/convert/number/). These things are both great websites.
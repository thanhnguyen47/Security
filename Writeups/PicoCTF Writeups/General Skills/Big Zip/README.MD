# Big Zip

## Overview

**Points:** 100\
**Tags:** General Skills

## Description

Unzip this archive and find the flag
- [Download zip file](./big-zip-files.zip)

## Hints

1. Can grep be instructed to look at every file in a directory and its subdirectories?

## Approach

Use `unzip -l` to see the content of `big-zip-files.zip`, you can see there are many things inside it.

Oke, I will extract it first:
```bash
$ unzip big-zip-files.zip
```

As the hint 1 says, i'm gonna try using `grep` to figure the flag out.

![alt text](image.png)

It's so easy, right?

## Flag 

`picoCTF{gr3p_15_m4g1c_ef8790dc}`
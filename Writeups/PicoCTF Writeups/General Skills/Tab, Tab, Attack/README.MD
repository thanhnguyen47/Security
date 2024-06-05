# Tab, Tab, Attack

## Overview

**Points:** 20\
**Tags:** General Skills

## Description

Using tabcomplete in the Terminal will add years to your life, esp. When dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](./Addadshashanammu.zip)

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Approach 

Copy the link and using `wget` to download the file name `Addadshashanammu.zip` from it:

```bash
wget https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip
```
Oke, now we see what file type it is
![alt text](image.png)

A zip file, it's called a ZIP archive. So what can we do now? Let's go ahead and unzip it. 
![alt text](image-5.png)
And we have a directory inside another directory inside another directory inside another directory ... These things make me crazy @@.
Just `cd` them until you can't
![alt text](image-6.png) 

Oh, I found a file, it's not a directory. Let's see what type of file it is:
![alt text](image-7.png)
It's an ELF excutable. 

Wanna see the readable strings inside it? Here you are
![alt text](image-8.png)

Done!

But i'm still curious about this file, I wanna run it:
![alt text](image-9.png)

LOL!

## Flag

`picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}`

## Extention

To zip files, we can use `zip` command. There is an example bellow:
![alt text](image-1.png)

Wanna unzip it in current directory, let's try it:
![alt text](image-2.png)

Wanna unzip a ZIP archive into a specific directory, using `-d` flag:
![alt text](image-3.png)

Or we can show the list of file in ZIP archive before unzip it by using `-l` option:
![alt text](image-4.png)

That's all you need to know. Wanna know more, see the manpage (`man`) of them or google.
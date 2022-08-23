# General skills: PW Crack 2
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/18/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level2.flag.txt.enc) in the same directory too.

## Solution
I acquired both files and then read the python script. It requests the user to enter a password and then decrypts the flag. The password entered by the user is compared to its correct value. This value is present in the script as a sequence of hexadecimal values. I looked these up in the [ascii chart](https://www.ascii-code.com/). The correct password is **39ce**.
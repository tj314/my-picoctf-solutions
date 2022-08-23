# General skills: PW Crack 5
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/80/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/80/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/80/level5.hash.bin) in the same directory too. Here's a [dictionary](https://artifacts.picoctf.net/c/80/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## Solution
I acquired both files and then read the python script. It requests the user to enter a password and then decrypts the flag. The password entered by the user is hashed using md5 and compared to the hash of the correct password. All the possible passwords are in the dictionary.txt file. I modified the script to load the possible passwords from this file and test all of these possibilities instead of requesting user input. The correct password was **7e5f**.
# General skills: PW Crack 3
Can you crack the password to get the flag?
Download the password checker [here](https://artifacts.picoctf.net/c/23/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/23/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/23/level3.hash.bin) in the same directory too.
There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Solution
I acquired both files and then read the python script. It requests the user to enter a password and then decrypts the flag. The password entered by the user is hashed using md5 and compared to the hash of the correct password. The source lists 7 possibilities for the correct password. I modified the script to test all of these possibilities instead of requesting user input. the correct password was **4b17**.
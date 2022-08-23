# Reverse engineering: crackme.py

[crackme.py](https://mercury.picoctf.net/static/8fc4e878bd6708031d67cb846f03c140/crackme.py)



## Solution

The script contains an encrypted flag and has a function to decrypt it. There is another function which is completely useless. The flag is encrypted using rot47. The docstring of the enryption/decryption function contains helpful information: the encryption and decryption in rot47 are the same operation.

So, I simply called this function and obtained the decrypted flag.













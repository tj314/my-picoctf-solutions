# Reverse engineering: keygenme.py

[keygenme-trial.py](https://mercury.picoctf.net/static/5a4198cd84f87c8a597cbd903d92fbf4/keygenme-trial.py)



## Solution

I downloaded the python script and glanced through it. It was not necessary to understand it in its entirety. The script implements a trial version of a product. User may enter a valid licence key to unlock the full version of the product.

The flag consists of two parts. There is a readable portion. I simply copied this part. To get the secopnd part I had to figure out the valid licence key. I found the function which performs the licence key validity check, `check_key`.

`check-key` function first checks the key length and then calculates sha256 hash of the trial username. Symbols of the hex digest of this hash are the symbols that must be present in the key in a specific order.

To calculate the key (and therefore the flag) I simply copied the checking logic and simply concatenated the expected characters. The solution is present in `main.py`.



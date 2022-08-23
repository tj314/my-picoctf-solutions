# General skills: Based
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.

## Solution
I connected to the above address. After a bit of poking around, it was clear that the challenge wants me to convert numeric values in several different bases to characters.

In the first part, I was presented with a word represented in binary. However, the correct answer to this representation was printed, probably as an example. I just had to copy and paste that.

In the second part, I was presented with octal numbers which I converted manually using the [ascii chart](https://www.ascii-code.com/). The time limit was only 45 seconds, however the word was only five characters.

In the last part, I was precented with hexadecimal numbers. I quickly googled 'hex to ascii', copied the hex string to [this tool](https://www.rapidtables.com/convert/number/hex-to-ascii.html) and copy-pasted the result.
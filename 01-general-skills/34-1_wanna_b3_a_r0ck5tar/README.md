# General skills: 1_wanna_b3_a_r0ck5tar
I wrote you another [song](https://jupiter.challenges.picoctf.org/static/96904d361d61fada5bd2d13536706f9a/lyrics.txt). Put the flag in the picoCTF{} flag format.

## Solution
Once again I attempted to run this program using the online interpreter, but the execution failed with the most useless error message ever. I tried reading the language reference and fell asleep.

The language's website mentions other implementations including a [python transpiler](https://codewithrockstar.com/code). Hey, I can read python. So I installed the transpiler and used it. I read the transpiled script. The result was somewhat messy. However, I noticed a sequence of `print` calls. I looked up the values to be printed in the [ascii chart](https://www.ascii-code.com/). The result was BONJVI. I tried to use it as the flag, it was incorrect.

Then I guessed, the correct flag would be BONJOVI. This time, I was correct.
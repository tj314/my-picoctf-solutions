# General skills: plumbing
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 14291`.

## Solution
```bash
$ nc jupiter.challenges.picoctf.org 14291 > out.txt # ctrl+d after that
$ cat out.txt | grep pico
```
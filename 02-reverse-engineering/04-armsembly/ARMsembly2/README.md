# Reverse engineering: ARMsembly 2

What integer does this program print with argument `2610164910`? File: [chall_2.S](https://mercury.picoctf.net/static/44f2f0e6f503fc6aac95e45390275e09/chall_2.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution

The point of this exercise is to understand how loops work in assembly. Truth to be told, following the flow of loops in assembly is always a chore. So this time instead of walking through the code using pen and paper, I cross compiled the assembly to run on my computer.

```bash
$ wget https://mercury.picoctf.net/static/44f2f0e6f503fc6aac95e45390275e09/chall_2.S
$ aarch64-linux-gnu-as -o chall chall_2.S
$ aarch64-linux-gnu-gcc -static -o chall.exe chall
$ ./chall.exe 2610164910
```

The result was 3535527434. Converted to hex and put into picoCTF flag format, we get **picoCTF{D2BBDE0A}**.



































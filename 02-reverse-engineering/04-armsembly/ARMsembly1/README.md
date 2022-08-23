# Reverse engineering: ARMsembly 1

For what argument does this program print `win` with variables `81`, `0` and `3`? File: [chall_1.S](https://mercury.picoctf.net/static/7cc2b73e671f61f8dc2d40493fb62611/chall_1.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution

Once again, I read the source and wrote the flow of the program on a piece of paper. The source contains `func` label which performs most of the core functionality. Rough translation of this "function" into C looks like this:

```c
int func(int arg) {
    int tmp = 81 << 0; // tmp is 81
    tmp = tmp / 3; // tmp is 27
    return tmp - arg;
}
```

There is also `main` label. `main` loads an argument and jumps into `func`. It then compares the result of func to zero. If the result is zero, **You win!** message is printed. Therefore the argument must be 27. It follows that the flag is **picoCTF{0000001B}**.



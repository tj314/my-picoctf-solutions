# Reverse engineering: ARMsembly 0

What integer does this program print with arguments `4112417903` and `1169092511`? File: [chall.S](https://mercury.picoctf.net/static/55a414fdd81f39784d662e8023c5aeb8/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution

So far this has been the first time, I had to learn something new for picoCTF. I did not know anything about ARMv8 assembly beforehand, though I've had some familiarity with x86-64 assembly.

I tried reading the provided source file, but I had no luck. ARMv8 assembly proved to be sufficiently different from the x86-64 one to confuse me. I used [this](https://modexp.wordpress.com/2018/10/30/arm64-assembly/) reference to get a hang of the language. 

Then I tried reading the source code again. The core of the program was in the `func1` function. The remainder of the program was concerned with calling the `func1` with given arguments and then `printf` to print the result of `func1`.

I sketched the flow of the function on a piece of paper. I also tried using [godbolt](https://godbolt.org/) to reconstruct the given assembly by incrementally writing C code. This proved to be of no real use. The pen and paper method worked better.

The following C code is (mostly) equivalent to the the given assembly:

```c
int func1(int a, int b) {
    if (a == b) return b;
    else return a;
}
```

From here, we can see that `func1(4112417903, 1169092511) -> 4112417903`. The task requires the answer in hex, so I used an [online tool]([Decimal to Hexadecimal Converter](https://www.rapidtables.com/convert/number/decimal-to-hex.html)) to convert it. The flag was as follows: `picoCTF{F51E846F}`.



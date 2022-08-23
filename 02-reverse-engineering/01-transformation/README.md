# Reverse engineering: Transformation

I wonder what this really is... [enc](https://mercury.picoctf.net/static/1d8a5a2779c4dc24999f0358d7a1a786/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

## Solution

Let's think about the given piece of python code. It seems to be the used "encryption". Let's rewrite it into a slightly more readable form:

```python
s = ""
i = 0
while i < len(flag):
    c1 = ord(flag[i])
    c2 = ord(flag[i+1])
    c1 = c1 << 8
    s += chr(c1 + c2)
    i += 2
```

It is now obvious that this "encryption" reads two 8-bit chars and combines them into one 16-bit char (the first char being the high 8 bits and the second char being the low 8 bits). From this form, it is easy to see, how one must decrypt the encrypted flag:

```python
s = ""
i = 0
while i < len(enc):
    c = ord(enc[i])
    c2 = c & 0b11111111   # bit mask to get the lower 8 bits
    c1 = (c >> 8) & 0b11111111   # and the higher 8 bits
    s += chr(c1) + chr(c2)
    i += 1
```



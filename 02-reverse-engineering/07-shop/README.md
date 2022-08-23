# Reverse engineering: Shop

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/f7b8db17d0891fb38c01a716052d1c04/source). The shop is open for business at `nc mercury.picoctf.net 24851`.

## Solution

```bash
$ nc mercury.picoctf.net 24851
$ cat source
```

This produced a lot of strings and a buch of gibberish. The *source* file seemed to be a compiled binary. I tried using the following:

```bash
$ strings source | grep pico
$ strings source | grep flag
```

I had no success. The strings I saw in the binary seemed to indicate that this program was originaly written in Go. I knew, I could reverse engineer it, but I first attempted to connect to the provided address. I was presented with a shop and an account balance. This reminded me of another task I was working on in the **General skills** section of **picoCTF**. I immediatly thought the point of this exercise was also integer underflow.

The shop provided me with an option to buy *Quiet Quiches*, so I selected this option and simply attempted to buy -42 of those. It worked. My balance increased enough to buy a flag. So I bought one. The flag was presented to me as a sequence of decimal numbers, so I pasted those into [this online tool]([Convert Decimal to ASCII - Online ASCII Tools](https://onlineasciitools.com/convert-decimal-to-ascii)) to convert them to chars and get the flag.





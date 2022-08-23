# General skills: Nice netcat...
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 49039, but it doesn't speak English...

## Solution
I connected to the given address and port. The received output consisted of several lines of numbers. I noticed that the numbers were all in range of printable ASCII character's decimal codes. I wrote a simple python script to translate those to readable characters.
```bash
$ nc mercury.picoctf.net 49039 > out.txt  # close connection manually with ctrl+d
$ python main.py out.txt
```

Alternatively:
```bash
$ nc mercury.picoctf.net 49039 | python main1.py  # close connection manually with ctrl+d
```
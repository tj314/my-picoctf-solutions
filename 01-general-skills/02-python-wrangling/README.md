# Python Wrangling
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/ende.py) using [this password](https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/pw.txt) to get [the flag](https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/flag.txt.en)?

## Solution
First, acquire all files:
```bash
$ wget "https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/ende.py"
$ wget "https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/pw.txt"
$ wget "https://mercury.picoctf.net/static/2ac2139344d2e734d5d638ac928f1a8d/flag.txt.en"
```

I tried to run the program and it printed a help message. From that message, it was clear that the program can encrypt and decrypt given files. I tried decryption and was prompted for password. To obtain the flag:
```bash
$ cat pw.txt | python ende.py -d flag.txt.en
```
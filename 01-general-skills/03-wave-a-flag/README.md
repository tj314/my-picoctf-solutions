# General skills: Wave a flag
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/fc1d77192c544314efece5dd309092e3/warm) has extraordinarily helpful information...

## Solution
```bash
$ wget "https://mercury.picoctf.net/static/fc1d77192c544314efece5dd309092e3/warm"
$ strings warm | grep pico
```
# General skills: First Grep
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Solution
```bash
$ wget "https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file"
$ cat file | grep pico
```

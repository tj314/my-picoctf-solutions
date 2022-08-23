# General skills: Strings it
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) without running it?

## Solution
```bash
$ wget "https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings"
$ strings strings | grep pico
```
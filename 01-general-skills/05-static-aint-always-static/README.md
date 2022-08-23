# General skills: Static ain't always noise
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/static)? This [BASH script](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/ltdis.sh) might help!

## Solution
I did not run the provided script. I assumed that I could extract the flag from the executable simply by running `strings`. I was correct.

```bash
$ wget "https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/static"
$ strings static | grep pico
```
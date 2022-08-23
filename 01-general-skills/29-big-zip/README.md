# General skills: Big Zip
Unzip this archive and find the flag.
- [Download zip file](https://artifacts.picoctf.net/c/555/big-zip-files.zip)

## Solution
```bash
$ wget https://artifacts.picoctf.net/c/555/big-zip-files.zip
$ unzip big-zip-files
$ grep -R pico big-zip-files
```
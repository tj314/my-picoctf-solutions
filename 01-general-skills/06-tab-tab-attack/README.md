# General skills: Tab, Tab, Attack
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/a350754a299cb58988d6d47aed5be3ba/Addadshashanammu.zip)

## Solution
First, get the archive, unzip it and get a general idea of its structure:
```bash
$ wget "https://mercury.picoctf.net/static/a350754a299cb58988d6d47aed5be3ba/Addadshashanammu.zip"
$ unzip Addadshashanammu.zip
$ tree
```
Now simply execute the only executable file from this archive. Use tab plentifully.
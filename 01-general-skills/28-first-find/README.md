# General skills: First Find
Unzip this archive and find the file named 'uber-secret.txt'
- [Download zip file](https://artifacts.picoctf.net/c/552/files.zip)

## Solution
```bash
$ wget https://artifacts.picoctf.net/c/552/files.zip
$ unzip files-zip
$ find files -name uber-secret.txt | xargs cat
```
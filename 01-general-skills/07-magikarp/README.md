# General skills: Magikarp Ground Mission
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6dee9772`

## Solution
Simply follow the instructions.
1. `ssh ctf-player@venus.picoctf.net -p 52984`, enter password 6dee9772
2. `ls`, the directory contains two files. Instructions and the first third of the flag.
3. `cd /` as per the instructions, get the second third of the flag and read the instructions.
4. `cd ~` or simply `cd` as per the instructions. Get the remainder of the flag.
5. go get yourself a well deserved beer
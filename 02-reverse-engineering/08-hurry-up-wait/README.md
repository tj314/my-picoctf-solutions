# Reverse engineering: Hurry up! Wait!

[svchost.exe](https://mercury.picoctf.net/static/df4efca50acbb7c5e829f8fd472fb796/svchost.exe)

## Solution

I downloaded this executable and opened it in ghidra. Based on the name *svchost* and the extension *exe* I assumed this was a windows binary, but upon import ghidra informed me that was indeed good old ELF.

I ran the automatic analysis and then looked at the exported functions. I found the entry and followed the function calls from there. Soon I found the main function. It seemed a library was loaded, but this is largely unimportant to my analysis. There were 3 functions called from main, one of which contained many other function calls. I took a look at this function.

Each of the functions called from within this function simply printed a character on screen. The characters were stored in the data section of the binary. I simply inspected these functions one by one to find out which characters were to be printed. This gave me the flag **picoCTF{d15a5m_ftw_87e5ab1}**.
